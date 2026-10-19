#!/usr/bin/env python3
"""Build timestamped visual references and maintain a Claude-assisted effect library."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import re
import secrets
import shutil
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path



ROOT = Path(__file__).resolve().parent
WORK = ROOT / "work"
CATALOG = ROOT / "library" / "effects.json"
INDEXES = {"en": ROOT / "library" / "EFFECTS.md", "he": ROOT / "library" / "EFFECTS.he.md"}
LANGUAGES = {"en": "English", "he": "Hebrew"}
# Personal data (your analyses and settings) lives here and is never committed.
LOCAL = Path(os.environ.get("REEL_EFFECTS_LOCAL_DIR") or ROOT / "local")
ANALYSES = LOCAL / "analyses.json"
ANALYSES_INDEX = LOCAL / "ANALYSES.md"
SETTINGS = LOCAL / "settings.json"
COLS, ROWS = 4, 4
TILE_W, TILE_H, LABEL_H = 320, 205, 28


def language() -> str:
    """REEL_EFFECTS_LANG wins, then local/settings.json, then English."""
    lang = os.environ.get("REEL_EFFECTS_LANG", "").strip().lower()
    if not lang:
        try:
            lang = str(json.loads(SETTINGS.read_text(encoding="utf-8")).get("lang", "")).lower()
        except (OSError, json.JSONDecodeError, AttributeError):
            lang = ""
    return lang if lang in LANGUAGES else "en"


def set_language(lang: str) -> None:
    LOCAL.mkdir(parents=True, exist_ok=True)
    try:
        settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        settings = {}
    settings["lang"] = lang
    SETTINGS.write_text(json.dumps(settings, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_starters() -> list[dict]:
    return json.loads(CATALOG.read_text(encoding="utf-8")).get("starter_effects", [])


def localize(effect: dict, lang: str) -> dict:
    """English fields are the base; a language block (e.g. "he") overrides whatever it translates."""
    view = {key: value for key, value in effect.items() if key not in LANGUAGES}
    if lang != "en":
        view.update(effect.get(lang) or {})
    return view


def load_analyses() -> list[dict]:
    try:
        data = json.loads(ANALYSES.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    return data.get("analyses", []) if isinstance(data, dict) else []


@contextmanager
def analyses_lock():
    """Serialize analysis writes between the CLI, the web server and its threads."""
    LOCAL.mkdir(parents=True, exist_ok=True)
    with open(LOCAL / ".lock", "a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def write_analyses(analyses: list[dict]) -> None:
    tmp = ANALYSES.with_name(f".{ANALYSES.name}.{os.getpid()}.{secrets.token_hex(4)}.tmp")
    tmp.write_text(json.dumps({"analyses": analyses}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(ANALYSES)
    ANALYSES_INDEX.write_text(render_analyses(analyses, language()), encoding="utf-8")


def append_analysis(record: dict) -> None:
    with analyses_lock():
        analyses = load_analyses()
        analyses.append(record)
        write_analyses(analyses)


def import_analyses(path: Path) -> int:
    """Move analyses from an older effects.json (or another analyses file) into the private local store."""
    data = json.loads(path.read_text(encoding="utf-8"))
    incoming = data.get("analyses", []) if isinstance(data, dict) else []
    with analyses_lock():
        analyses = load_analyses()
        known = {item.get("id") for item in analyses}
        added = [item for item in incoming if isinstance(item, dict) and item.get("id") not in known]
        if added:
            write_analyses(analyses + added)
    return len(added)


def extract_json(text: str) -> dict:
    """Parse Claude's answer even when the JSON object is wrapped in a code fence or short prose."""
    text = text.strip()
    candidates = [text]
    fenced = re.search(r"```(?:json)?\s*(.*?)\s*```", text, flags=re.S)
    if fenced:
        candidates.append(fenced.group(1))
    if "{" in text and "}" in text:
        candidates.append(text[text.index("{"):text.rindex("}") + 1])
    for candidate in candidates:
        try:
            data = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            return data
    raise ValueError("no JSON object found")


def as_seconds(value: object, fallback: float) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return fallback
    return number if number >= 0 else fallback


def as_text_list(value: object) -> list[str]:
    if isinstance(value, str):
        value = [value]
    if not isinstance(value, list):
        return []
    return [str(item) for item in value if item not in (None, "")]


def ffmpeg() -> str:
    found = shutil.which("ffmpeg")
    if found:
        return found
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception as exc:
        raise RuntimeError("FFmpeg is unavailable.") from exc


def download(url: str, job: Path, browser: str | None) -> Path:
    template = str(job / "source.%(ext)s")
    cmd = [sys.executable, "-m", "yt_dlp", "--no-playlist", "--merge-output-format", "mp4", "-o", template]
    if browser:
        cmd += ["--cookies-from-browser", browser]
    cmd.append(url)
    subprocess.run(cmd, check=True)
    candidates = [p for p in job.glob("source.*") if p.suffix.lower() not in {".json", ".part", ".ytdl"}]
    if not candidates:
        raise RuntimeError("yt-dlp did not produce a video. Try saving the Reel locally and pass its file path.")
    return max(candidates, key=lambda p: p.stat().st_mtime)


def contact_sheet(frames: list[Path], fps: float, out: Path, offset: float) -> list[Path]:
    # Imported here so `check`/`index` run with the standard library only.
    from PIL import Image, ImageDraw, ImageFont

    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 17)
    except OSError:
        font = ImageFont.load_default()
    sheets: list[Path] = []
    per_sheet = COLS * ROWS
    for page_no, start in enumerate(range(0, len(frames), per_sheet), 1):
        sheet = Image.new("RGB", (COLS * TILE_W, ROWS * (TILE_H + LABEL_H) + 48), "white")
        draw = ImageDraw.Draw(sheet)
        draw.text((12, 10), f"Frames at {fps:g} fps · sheet {page_no}", fill="#111827", font=font)
        for j, frame in enumerate(frames[start:start + per_sheet]):
            idx = start + j
            x = (j % COLS) * TILE_W
            y = 36 + (j // COLS) * (TILE_H + LABEL_H)
            with Image.open(frame) as im:
                im = im.convert("RGB")
                im.thumbnail((TILE_W - 8, TILE_H - 8), Image.Resampling.LANCZOS)
                sheet.paste(im, (x + (TILE_W - im.width) // 2, y + (TILE_H - im.height) // 2))
            draw.text((x + 8, y + TILE_H + 3), f"{offset + idx / fps:.3f}s", fill="#111827", font=font)
        path = out / f"sheet-{page_no:04d}.jpg"
        sheet.save(path, quality=88)
        sheets.append(path)
    if not sheets:
        raise RuntimeError("No frames were extracted.")
    return sheets


def skill_instructions() -> str:
    return (ROOT / ".claude/skills/reel-effect-librarian/SKILL.md").read_text(encoding="utf-8")


def ask_claude(job: Path, sheets: list[Path], source_label: str, start: float, fps: float) -> dict:
    claude = shutil.which("claude")
    if not claude:
        raise RuntimeError("Claude Code CLI not found. Install it and run `claude` once to sign in.")
    lang = language()
    starters = [localize(effect, lang) for effect in load_starters()]
    known_effects = []
    for starter in starters:
        known_effects.append({"id": starter.get("id"), "type": "starter", "name": starter.get("name"), "aliases": starter.get("aliases", []), "category": starter.get("category"), "summary": starter.get("summary"), "tags": starter.get("tags", [])})
    for analysis in load_analyses():
        for index, effect in enumerate(analysis.get("effects", [])):
            known_effects.append({"id": f"{analysis.get('id', 'analysis')}-{index + 1}", "type": "observed", "name": effect.get("name"), "category": effect.get("category"), "description": effect.get("description"), "tags": effect.get("tags", [])})
    starter_count = len(starters)
    known = json.dumps(known_effects[:starter_count] + known_effects[starter_count:][-60:], ensure_ascii=False, indent=2)
    sheet_paths = "\n".join(str(p.resolve()) for p in sheets)
    prompt = f"""You are analyzing one reference video for an accumulating visual-effects library.

Instructions:
{skill_instructions()}

Video label: {source_label}
Frame rate: {fps:g} sampled frames/second
Start offset: {start:g} seconds
Read all contact-sheet image files below in order; each tile has its timestamp:
{sheet_paths}

Known effects already in this library (starter recipes and effects observed in previous videos):
{known}

Return only a valid JSON object with this schema:
{{"title": string, "summary": string, "editing_rhythm": string, "effects": [{{"name": string, "category": string, "start_s": number, "end_s": number, "description": string, "evidence_frames": [string], "confidence": "high"|"medium"|"low", "recreation": string, "tags": [string]}}], "library_matches": [{{"effect_id": string, "kind": "same"|"similar", "video_effect": string, "reason": string}}]}}

Include only techniques visible in this video. Compare each visible technique against the known library and return a library_matches entry only for a genuine same or meaningfully similar technique; effect_id must exactly match an id above, and reason must briefly explain the visual/technical match in {LANGUAGES[lang]}. Do not report a match merely because two effects are both transitions. If no match exists, return an empty array. If no discrete effect is clearly visible, return an empty effects array and explain the limits in summary. Answer all text values in {LANGUAGES[lang]}. Do not edit files.
"""
    result = subprocess.run(
        [claude, "-p", "--output-format", "json", "--allowedTools", "Read", "--max-turns", "30"],
        input=prompt, text=True, capture_output=True, cwd=ROOT,
    )
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"Claude Code failed ({result.returncode}). Check `claude auth status`. {detail[:600]}")
    try:
        wrapper = json.loads(result.stdout)
        text = wrapper.get("result", "") if isinstance(wrapper, dict) else result.stdout
    except json.JSONDecodeError:
        text = result.stdout
    try:
        data = extract_json(text)
    except ValueError as exc:
        (job / "claude-raw-response.txt").write_text(result.stdout, encoding="utf-8")
        raise RuntimeError(f"Claude's response was not valid JSON; raw response saved in {job / 'claude-raw-response.txt'}") from exc
    if not isinstance(data.get("effects"), list):
        raise RuntimeError("Claude response is missing the expected effects list.")
    for key in ("title", "summary", "editing_rhythm"):
        data[key] = str(data.get(key) or "")
    known_names = {item.get("id"): item.get("name", "Library effect") for item in known_effects if item.get("id")}
    matches = data.get("library_matches", [])
    if not isinstance(matches, list):
        matches = []
    data["library_matches"] = [
        match for match in matches
        if isinstance(match, dict) and match.get("effect_id") in known_names and match.get("kind") in {"same", "similar"}
    ]
    for match in data["library_matches"]:
        match["effect_name"] = known_names[match["effect_id"]]
    for effect in data["effects"]:
        if not isinstance(effect, dict):
            raise RuntimeError("Claude response contains an effect that is not an object.")
        for key in ("name", "category", "description", "recreation", "confidence"):
            if not effect.get(key):
                raise RuntimeError(f"Claude response contains an effect missing {key!r}.")
        if effect["confidence"] not in {"high", "medium", "low"}:
            effect["confidence"] = "low"
        effect["start_s"] = as_seconds(effect.get("start_s"), start)
        effect["end_s"] = max(effect["start_s"], as_seconds(effect.get("end_s"), effect["start_s"]))
        effect["evidence_frames"] = as_text_list(effect.get("evidence_frames"))
        effect["tags"] = as_text_list(effect.get("tags"))
    return data


LABELS = {
    "en": {"title": "# Effect Library", "count": "Starter recipes: {n}", "intro": "General reusable techniques, not claims that these appeared in an analyzed video.",
           "when": "When to use", "recipe": "Recipe", "tags": "Tags", "reference": "Reference", "other": "Other languages: [עברית](EFFECTS.he.md)",
           "analyses": "# My analyzed videos", "none": "No videos analyzed yet. Add one with `./reel-effects add <URL-or-file>`.",
           "source": "Source", "analyzed": "Analyzed", "summary": "Summary", "rhythm": "Editing rhythm", "confidence": "confidence",
           "evidence": "Evidence", "recreate": "Recreate"},
    "he": {"title": "# ספריית אפקטים", "count": "מתכונים בסיסיים: {n}", "intro": "טכניקות כלליות לשימוש חוזר; הן לא בהכרח הופיעו בסרטון שנותח.",
           "when": "מתי מתאים", "recipe": "מתכון", "tags": "תגיות", "reference": "מקור", "other": "English: [EFFECTS.md](EFFECTS.md)",
           "analyses": "# הסרטונים שניתחתי", "none": "עדיין לא נותחו סרטונים. מוסיפים עם `./reel-effects add <URL-or-file>`.",
           "source": "מקור", "analyzed": "נותח", "summary": "סיכום", "rhythm": "קצב עריכה", "confidence": "ביטחון",
           "evidence": "ראיות", "recreate": "לשחזור"},
}


def render_index(starters: list[dict], lang: str) -> str:
    t = LABELS[lang]
    lines = [t["title"], "", t["count"].format(n=len(starters)) + "  ", t["other"], "", t["intro"], ""]
    for raw in starters:
        effect = localize(raw, lang)
        lines += [f"### {effect['name']} — {effect['category']}", "", effect["summary"], "", f"{t['when']}: {effect['when_to_use']}", "",
                  f"{t['recipe']}: {effect['recipe']}", "", f"{t['tags']}: {', '.join(effect.get('tags', []))}  ", f"{t['reference']}: {effect.get('reference', '')}", ""]
    return "\n".join(lines).rstrip() + "\n"


def render_analyses(analyses: list[dict], lang: str) -> str:
    t = LABELS[lang]
    lines = [t["analyses"], ""]
    if not analyses:
        lines.append(t["none"])
    for analysis in analyses:
        lines += [f"## {analysis.get('title') or 'Untitled'}", "", f"{t['source']}: {analysis.get('source', '')}  ", f"{t['analyzed']}: {analysis.get('analyzed_at', '')}  ",
                  f"{t['summary']}: {analysis.get('summary', '')}  ", f"{t['rhythm']}: {analysis.get('editing_rhythm', '')}", ""]
        for effect in analysis.get("effects", []):
            lines += [f"### {effect['name']} ({effect['start_s']:.2f}–{effect['end_s']:.2f}s) — {effect['category']} · {t['confidence']}: {effect['confidence']}", "",
                      effect["description"], "", f"{t['evidence']}: {', '.join(effect.get('evidence_frames', []))}", "", f"{t['recreate']}: {effect['recreation']}", "",
                      f"{t['tags']}: {', '.join(effect.get('tags', []))}", ""]
    return "\n".join(lines).rstrip() + "\n"


def refresh_index() -> None:
    starters = load_starters()
    for lang, path in INDEXES.items():
        path.write_text(render_index(starters, lang), encoding="utf-8")


def _terms(query: list[str]) -> list[str]:
    return [term for term in " ".join(query).lower().split() if term]


def find_effects(query: list[str], lang: str, limit: int = 8) -> list[tuple[int, str, dict]]:
    """Search both languages at once: every term must match; id/name/alias hits rank highest."""
    terms = _terms(query)
    hits: list[tuple[int, str, dict]] = []
    if not terms:
        return hits
    for raw in load_starters():
        he = raw.get("he") or {}
        strong = " ".join([raw["id"], raw["name"], he.get("name", ""), *raw.get("aliases", [])]).lower()
        medium = " ".join([raw["category"], he.get("category", ""), *raw.get("tags", []), *he.get("tags", [])]).lower()
        weak = " ".join([raw["summary"], raw["when_to_use"], raw["recipe"], he.get("summary", ""), he.get("when_to_use", ""), he.get("recipe", "")]).lower()
        if not all(term in strong or term in medium or term in weak for term in terms):
            continue
        score = sum(3 * (term in strong) + 2 * (term in medium) + (term in weak) for term in terms)
        hits.append((score, "starter", localize(raw, lang)))
    for analysis in load_analyses():
        for effect in analysis.get("effects", []):
            blob = " ".join([analysis.get("title", ""), effect.get("name", ""), effect.get("category", ""), effect.get("description", ""), effect.get("recreation", ""), *effect.get("tags", [])]).lower()
            if all(term in blob for term in terms):
                hits.append((sum(2 * (term in effect.get("name", "").lower()) + 1 for term in terms), "observed", {**effect, "video": analysis.get("title", "")}))
    hits.sort(key=lambda hit: -hit[0])
    return hits[:limit]


def format_hit(kind: str, effect: dict, lang: str) -> str:
    t = LABELS[lang]
    if kind == "starter":
        return "\n".join([f"## {effect['name']} ({effect['id']}) — {effect['category']}", effect["summary"], f"{t['when']}: {effect['when_to_use']}", f"{t['recipe']}: {effect['recipe']}", f"{t['reference']}: {effect.get('reference', '')}"])
    return "\n".join([f"## {effect['name']} — {effect['category']} [{effect['video']}, {effect.get('start_s', 0):.1f}–{effect.get('end_s', 0):.1f}s]", effect.get("description", ""), f"{t['recreate']}: {effect.get('recreation', '')}"])


STARTER_TEXT_FIELDS = ("id", "name", "category", "summary", "when_to_use", "recipe", "reference")
TRANSLATED_TEXT_FIELDS = ("category", "summary", "when_to_use", "recipe")
TRANSLATABLE_FIELDS = {"name", "category", "summary", "when_to_use", "recipe", "reference", "tags"}
HEBREW = re.compile(r"[\u0590-\u05FF]")


def check_library() -> list[str]:
    """Validate library/effects.json and confirm the EFFECTS indexes were regenerated from it."""
    try:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"{CATALOG.name}: cannot be read as JSON ({exc})"]
    problems: list[str] = []
    starters = catalog.get("starter_effects")
    if not isinstance(starters, list):
        return ["effects.json must contain a 'starter_effects' list"]
    if "analyses" in catalog:
        problems.append("effects.json must not contain 'analyses'; personal analyses belong in local/ (see ./reel-effects import-analyses)")
    seen: set[str] = set()
    for number, effect in enumerate(starters, 1):
        label = f"starter #{number} ({effect.get('id', '?') if isinstance(effect, dict) else '?'})"
        if not isinstance(effect, dict):
            problems.append(f"{label}: must be an object")
            continue
        for key in STARTER_TEXT_FIELDS:
            if not isinstance(effect.get(key), str) or not effect[key].strip():
                problems.append(f"{label}: '{key}' must be a non-empty string")
            elif key != "id" and HEBREW.search(effect[key]):
                problems.append(f"{label}: '{key}' should be in English; put the Hebrew text in the 'he' block")
        for key in ("aliases", "tags"):
            if not isinstance(effect.get(key), list) or not all(isinstance(item, str) and item.strip() for item in effect[key]):
                problems.append(f"{label}: '{key}' must be a list of non-empty strings")
        if not effect.get("tags"):
            problems.append(f"{label}: add at least one tag")
        effect_id = effect.get("id")
        if isinstance(effect_id, str):
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", effect_id):
                problems.append(f"{label}: id must be lowercase kebab-case, e.g. 'zoom-blur'")
            if effect_id in seen:
                problems.append(f"{label}: duplicate id")
            seen.add(effect_id)
        translation = effect.get("he")
        if translation is not None:
            if not isinstance(translation, dict):
                problems.append(f"{label}: 'he' must be an object")
            else:
                for key in TRANSLATED_TEXT_FIELDS:
                    if not isinstance(translation.get(key), str) or not translation[key].strip():
                        problems.append(f"{label}: 'he.{key}' must be a non-empty string (or leave out the whole 'he' block)")
                extra = set(translation) - TRANSLATABLE_FIELDS
                if extra:
                    problems.append(f"{label}: unknown field(s) in 'he': {', '.join(sorted(extra))}")
        unknown = set(effect) - set(STARTER_TEXT_FIELDS) - {"aliases", "tags", "he"}
        if unknown:
            problems.append(f"{label}: unknown field(s) {', '.join(sorted(unknown))}")
    if not problems:
        for lang, path in INDEXES.items():
            try:
                current = path.read_text(encoding="utf-8")
            except OSError:
                current = ""
            if current != render_index(starters, lang):
                problems.append(f"library/{path.name} is out of date; run ./reel-effects index")
    return problems


def add(args: argparse.Namespace) -> int:
    src = args.source
    is_url = src.startswith(("https://", "http://"))
    local = Path(src).expanduser()
    if not is_url and not local.is_file():
        raise RuntimeError(f"Video file not found: {local}")
    WORK.mkdir(exist_ok=True)
    stamp = f"{datetime.now().strftime('%Y%m%d-%H%M%S')}-{secrets.token_hex(2)}"
    job = WORK / f"{stamp}-job"
    job.mkdir()
    try:
        video = download(src, job, args.cookies_from_browser) if is_url else local.resolve()
        frames_dir = job / "frames"
        frames_dir.mkdir()
        pattern = str(frames_dir / "frame-%07d.jpg")
        vf = f"fps={args.fps:g},scale=640:640:force_original_aspect_ratio=decrease"
        # Seek before -i so long videos are not decoded from the start; frame 0 is then at --start.
        cmd = [ffmpeg(), "-hide_banner", "-loglevel", "error", "-ss", str(args.start), "-i", str(video)]
        if args.end is not None:
            cmd += ["-t", str(args.end - args.start)]
        cmd += ["-vf", vf, "-q:v", "3", pattern]
        subprocess.run(cmd, check=True)
        frames = sorted(frames_dir.glob("frame-*.jpg"))
        sheets = contact_sheet(frames, args.fps, job, args.start)
        data = ask_claude(job, sheets, video.name if not is_url else src, args.start, args.fps)
        record = {
            "id": stamp,
            "source": src,
            "analyzed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sampling": {"fps": args.fps, "start_s": args.start, "end_s": args.end, "frame_count": len(frames)},
            **data,
        }
        if args.defer_to:
            pending = Path(args.defer_to)
            pending.parent.mkdir(parents=True, exist_ok=True)
            pending.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            print(f"Analysis ready for review: {len(data['effects'])} effects from {record['title']}.")
        else:
            append_analysis(record)
            print(f"Added {len(data['effects'])} effects from {record['title']}.")
            print(f"Your analyses: {ANALYSES_INDEX}")
        return 0
    except Exception:
        print(f"Analysis files retained for recovery: {job}", file=sys.stderr)
        raise


def main() -> int:
    parser = argparse.ArgumentParser(prog="reel-effects", description="Analyze video effects with Claude Code and grow a local effects library.")
    sub = parser.add_subparsers(dest="command", required=True)
    p_add = sub.add_parser("add", help="Analyze an Instagram URL or local video and add its effects")
    p_add.add_argument("source", help="Instagram URL or local video path")
    p_add.add_argument("--fps", type=float, default=12, help="samples per second (default 12; use up to 30 for fast effects)")
    p_add.add_argument("--start", type=float, default=0)
    p_add.add_argument("--end", type=float)
    p_add.add_argument("--cookies-from-browser", metavar="BROWSER", help="optional browser session for yt-dlp, e.g. chrome")
    p_add.add_argument("--defer-to", help=argparse.SUPPRESS)
    sub.add_parser("list", help="Show the effect library and your analyses")
    sub.add_parser("index", help="Regenerate library/EFFECTS.md and EFFECTS.he.md from library/effects.json")
    sub.add_parser("check", help="Validate library/effects.json and the EFFECTS indexes (used by CI)")
    p_find = sub.add_parser("find", help="Search effects in English or Hebrew and print matching recipes (handy for agents and editing skills)")
    p_find.add_argument("query", nargs="+", help="words to look for, e.g. speed ramp / רמפת מהירות")
    p_find.add_argument("--lang", choices=sorted(LANGUAGES), help="language of the printed recipes (default: your setting)")
    p_find.add_argument("--limit", type=int, default=8)
    p_find.add_argument("--json", action="store_true", help="print machine-readable JSON")
    p_lang = sub.add_parser("lang", help="Show or set the language for the web page and Claude's analyses (en, he)")
    p_lang.add_argument("code", nargs="?", choices=sorted(LANGUAGES))
    p_import = sub.add_parser("import-analyses", help="Move analyses from an older effects.json into the private local/ folder")
    p_import.add_argument("file", type=Path)
    args = parser.parse_args()
    if args.command == "index":
        refresh_index()
        print("Updated " + ", ".join(str(path) for path in INDEXES.values()))
        return 0
    if args.command == "find":
        lang = args.lang or language()
        hits = find_effects(args.query, lang, max(1, args.limit))
        if args.json:
            print(json.dumps([{"kind": kind, **effect} for _, kind, effect in hits], ensure_ascii=False, indent=2))
        elif not hits:
            print("No matches." if lang == "en" else "לא נמצאו התאמות.")
            return 1
        else:
            print("\n\n".join(format_hit(kind, effect, lang) for _, kind, effect in hits))
        return 0 if hits else 1
    if args.command == "lang":
        if args.code:
            set_language(args.code)
        print(f"Language: {language()} ({LANGUAGES[language()]})")
        return 0
    if args.command == "import-analyses":
        count = import_analyses(args.file)
        print(f"Imported {count} analyses into {ANALYSES}.")
        return 0
    if args.command == "check":
        problems = check_library()
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        print("Library OK." if not problems else f"{len(problems)} problem(s) found.")
        return 1 if problems else 0
    if args.command == "add":
        if args.fps <= 0 or args.fps > 30:
            parser.error("--fps must be greater than 0 and no more than 30")
        if args.start < 0 or (args.end is not None and args.end <= args.start):
            parser.error("time bounds must be non-negative and --end must be greater than --start")
        try:
            return add(args)
        except (RuntimeError, OSError, subprocess.CalledProcessError) as exc:
            print(f"Error: {exc}", file=sys.stderr)
            return 1
    lang = language()
    print(render_index(load_starters(), lang))
    print(render_analyses(load_analyses(), lang))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
