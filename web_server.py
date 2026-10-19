#!/usr/bin/env python3
"""LAN/loopback upload UI and single-worker queue for Video Effect Reel."""

from __future__ import annotations

import json
import os
import queue
import re
import subprocess
import sys
import threading
import uuid
from email import policy
from email.parser import BytesParser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote

from reel_effects import append_analysis, language, load_analyses, load_starters, localize


ROOT = Path(__file__).resolve().parent
WEB = ROOT / "web"
WORK = ROOT / "work"
UPLOADS = WORK / "uploads"
JOBS = WORK / "web-jobs"
CLI = ROOT / "reel_effects.py"
MAX_UPLOAD = 500 * 1024 * 1024
ALLOWED_EXTENSIONS = {".mp4", ".mov", ".m4v", ".mkv", ".webm", ".avi"}
tasks: queue.Queue[tuple[str, str, float, float, float | None] | None] = queue.Queue()
names_lock = threading.Lock()

# (English, Hebrew) for every message the page shows; the language comes from `reel-effects lang`.
MESSAGES = {
    "restarted": ("The server restarted before the analysis finished. Please submit the video again.", "השרת הופעל מחדש לפני שהניתוח הסתיים. שלח את הסרטון שוב."),
    "running": ("Extracting frames and sending them to Claude Code…", "מנתח פריימים ומעביר ל-Claude Code…"),
    "failed": ("The analysis failed.", "הניתוח נכשל."),
    "ready": ("Analysis ready. Review the names and library matches before saving.", "הניתוח מוכן. בדוק שמות והתאמות לספרייה לפני השמירה."),
    "too_big": ("The upload is empty or larger than the 500 MB limit.", "הקובץ ריק או גדול מהמותר (500MB)."),
    "use_form": ("Please submit using the upload form.", "נדרשת שליחה מטופס העלאה."),
    "bad_link": ("The link is not valid.", "הקישור אינו תקין."),
    "one_source": ("Choose exactly one link or one file.", "יש לבחור קישור אחד או קובץ אחד."),
    "bad_times": ("Check the frame rate and the start/end times.", "בדוק את קצב הפריימים ואת זמני הקטע."),
    "bad_type": ("Unsupported file type. Use MP4, MOV, M4V, MKV, WEBM or AVI.", "סוג הקובץ אינו נתמך. השתמש ב-MP4, MOV, M4V, MKV, WEBM או AVI."),
    "queued": ("The video was added to the queue.", "הסרטון נוסף לתור."),
    "bad_request": ("Invalid request.", "הבקשה לא תקינה."),
    "no_review": ("The analysis was not found, has not finished, or was already saved.", "הניתוח לא נמצא, עדיין לא הסתיים או כבר נשמר."),
    "names_mismatch": ("The list of names does not match the analysis.", "רשימת השמות לא תואמת לניתוח."),
    "name_length": ("Each name must be 1–80 characters.", "כל שם צריך להכיל 1–80 תווים."),
    "bad_form": ("Invalid form data: {detail}", "נתוני הטופס אינם תקינים: {detail}"),
    "save_failed": ("Could not save names: {detail}", "לא ניתן לשמור שמות: {detail}"),
    "saved": ("The names were saved to your private library.", "השמות נשמרו בספרייה הפרטית שלך."),
}


def msg(key: str, **values: object) -> str:
    english, hebrew = MESSAGES[key]
    return (hebrew if language() == "he" else english).format(**values)


def save_job(job_id: str, data: dict) -> None:
    tmp = JOBS / f"{job_id}.tmp"
    tmp.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    tmp.replace(JOBS / f"{job_id}.json")


def read_job(job_id: str) -> dict | None:
    path = JOBS / f"{job_id}.json"
    if not re.fullmatch(r"[a-f0-9]{16}", job_id) or not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def fail_interrupted_jobs() -> None:
    """The queue lives in memory, so jobs left queued/running by a restart would otherwise poll forever."""
    if not JOBS.exists():
        return
    for file in JOBS.glob("[a-f0-9]" * 16 + ".json"):
        job = read_job(file.stem)
        if job and job.get("status") in {"queued", "running"}:
            job.update(status="failed", message=msg("restarted"))
            save_job(file.stem, job)


def worker() -> None:
    while True:
        task = tasks.get()
        if task is None:
            return
        job_id, source, fps, start, end = task
        job = read_job(job_id) or {}
        job.update(status="running", message=msg("running"))
        save_job(job_id, job)
        pending = JOBS / f"{job_id}.pending.json"
        cmd = [sys.executable, str(CLI), "add", source, "--fps", str(fps), "--start", str(start), "--defer-to", str(pending)]
        if end is not None:
            cmd += ["--end", str(end)]
        try:
            result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
            if result.returncode:
                detail = (result.stderr or result.stdout).strip()
                job.update(status="failed", message=(detail[-900:] if detail else msg("failed")))
            else:
                analysis = json.loads(pending.read_text(encoding="utf-8"))
                job.update(status="awaiting_names", message=msg("ready"), title=analysis.get("title", ""), effect_count=len(analysis.get("effects", [])), analysis_id=analysis.get("id"), analysis=analysis)
                upload = Path(source)
                if upload.is_relative_to(UPLOADS) and upload.exists():
                    upload.unlink()
            save_job(job_id, job)
        except Exception as exc:
            job.update(status="failed", message=str(exc)[:900])
            save_job(job_id, job)
        finally:
            tasks.task_done()


class Handler(BaseHTTPRequestHandler):
    server_version = "VideoEffectReel/1.0"

    def log_message(self, fmt: str, *args: object) -> None:
        print(f"{self.client_address[0]} - {fmt % args}", flush=True)

    def respond(self, status: int, data: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def json(self, status: int, data: dict) -> None:
        self.respond(status, json.dumps(data, ensure_ascii=False).encode(), "application/json; charset=utf-8")

    def do_GET(self) -> None:
        path = unquote(self.path.split("?", 1)[0])
        if path in {"/", "/index.html"}:
            page = (WEB / "index.html").read_text(encoding="utf-8")
            if language() == "he":
                page = page.replace('<html lang="en" dir="ltr">', '<html lang="he" dir="rtl">', 1)
            self.respond(200, page.encode("utf-8"), "text/html; charset=utf-8")
        elif path == "/api/health":
            self.json(200, {"ok": True})
        elif path == "/api/catalog":
            try:
                lang = language()
                self.json(200, {"lang": lang, "starter_effects": [localize(effect, lang) for effect in load_starters()], "analyses": load_analyses()})
            except Exception as exc:
                self.json(500, {"error": str(exc)})
        elif path == "/api/jobs":
            reviews = []
            if JOBS.exists():
                for file in JOBS.glob("[a-f0-9]" * 16 + ".json"):
                    job = read_job(file.stem)
                    if job and job.get("status") == "awaiting_names":
                        reviews.append(job)
            self.json(200, {"jobs": reviews})
        elif path.startswith("/api/jobs/"):
            job = read_job(path.rsplit("/", 1)[-1])
            if job is None:
                self.json(404, {"error": "job not found"})
            else:
                self.json(200, job)
        else:
            self.json(404, {"error": "not found"})

    def do_POST(self) -> None:
        if self.path.startswith("/api/jobs/") and self.path.endswith("/names"):
            self.save_names()
            return
        if self.path != "/api/submit":
            self.json(404, {"error": "not found"})
            return
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > MAX_UPLOAD:
                self.json(413, {"error": msg("too_big")})
                return
            content_type = self.headers.get("Content-Type", "")
            if not content_type.lower().startswith("multipart/form-data;"):
                self.json(415, {"error": msg("use_form")})
                return
            raw = self.rfile.read(length)
            message = BytesParser(policy=policy.default).parsebytes(
                f"Content-Type: {content_type}\r\nMIME-Version: 1.0\r\n\r\n".encode() + raw
            )
            values: dict[str, str] = {}
            upload: tuple[str, bytes] | None = None
            for part in message.iter_parts():
                key = part.get_param("name", header="content-disposition")
                payload = part.get_payload(decode=True) or b""
                filename = part.get_filename()
                if key == "video" and filename and payload:
                    upload = (Path(filename).name, payload)
                elif key in {"url", "fps", "start", "end"}:
                    values[key] = payload.decode("utf-8", "replace").strip()
            url = values.get("url", "")
            if url and not re.fullmatch(r"https?://[^\s]+", url, flags=re.I):
                self.json(400, {"error": msg("bad_link")})
                return
            if bool(url) == bool(upload):
                self.json(400, {"error": msg("one_source")})
                return
            fps = float(values.get("fps") or 12)
            start = float(values.get("start") or 0)
            end = float(values["end"]) if values.get("end") else None
            if fps < 1 or fps > 30 or start < 0 or (end is not None and end <= start):
                self.json(400, {"error": msg("bad_times")})
                return
            source = url
            if upload:
                filename, payload = upload
                extension = Path(filename).suffix.lower()
                if extension not in ALLOWED_EXTENSIONS:
                    self.json(415, {"error": msg("bad_type")})
                    return
                UPLOADS.mkdir(parents=True, exist_ok=True)
                source_path = UPLOADS / f"{uuid.uuid4().hex}{extension}"
                source_path.write_bytes(payload)
                source = str(source_path)
            JOBS.mkdir(parents=True, exist_ok=True)
            job_id = uuid.uuid4().hex[:16]
            save_job(job_id, {"id": job_id, "status": "queued", "message": msg("queued")})
            tasks.put((job_id, source, fps, start, end))
            self.json(202, {"id": job_id})
        except (ValueError, UnicodeDecodeError) as exc:
            self.json(400, {"error": msg("bad_form", detail=exc)})
        except Exception as exc:
            self.json(500, {"error": str(exc)[:500]})

    def save_names(self) -> None:
        job_id = self.path.split("?", 1)[0].split("/")[3]
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 16_000:
                self.json(413, {"error": msg("bad_request")})
                return
            body = json.loads(self.rfile.read(length))
            names = body.get("names") if isinstance(body, dict) else None
            if not isinstance(names, list):
                raise ValueError("names must be a list")
            # One save at a time, and re-check the job inside the lock so a double click cannot add it twice.
            with names_lock:
                job = read_job(job_id)
                pending_path = JOBS / f"{job_id}.pending.json"
                if not job or job.get("status") != "awaiting_names" or not pending_path.exists():
                    self.json(404, {"error": msg("no_review")})
                    return
                analysis = json.loads(pending_path.read_text(encoding="utf-8"))
                if len(names) != len(analysis.get("effects", [])):
                    self.json(400, {"error": msg("names_mismatch")})
                    return
                cleaned = [str(name).strip() for name in names]
                if any(not name or len(name) > 80 for name in cleaned):
                    self.json(400, {"error": msg("name_length")})
                    return
                for effect, name in zip(analysis["effects"], cleaned):
                    effect["name"] = name
                append_analysis(analysis)
                job["analysis"] = analysis
                job.update(status="completed", message=msg("saved"))
                save_job(job_id, job)
                pending_path.unlink(missing_ok=True)
            self.json(200, {"ok": True})
        except (ValueError, json.JSONDecodeError) as exc:
            self.json(400, {"error": msg("save_failed", detail=exc)})
        except Exception as exc:
            self.json(500, {"error": str(exc)[:500]})

def main() -> None:
    host = os.environ.get("REEL_EFFECTS_HOST", "127.0.0.1")
    port = int(os.environ.get("REEL_EFFECTS_PORT", "4319"))
    WORK.mkdir(exist_ok=True)
    fail_interrupted_jobs()
    threading.Thread(target=worker, name="effect-analysis", daemon=True).start()
    server = ThreadingHTTPServer((host, port), Handler)
    print(f"Video Effect Reel listening on http://{host}:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
