# Reel Effect Lab

Analyze a Reel or local video with Claude Code and accumulate a searchable, evidence-linked effects library. The analyzer samples densely (12 fps by default; up to 30 fps) and makes timestamped contact sheets. Claude writes an analysis; the local CLI saves it to your private `local/` folder. The library includes a clearly separated starter pack of common editing recipes; these are references for applying effects to the user's footage, not claims that a technique appeared in a Reel.

The starter pack is based primarily on the documented Remotion transitions/effects and FFmpeg's built-in `xfade`/filter families. It currently contains 123 entries (including groups of directional variants), in English ([EFFECTS.md](library/EFFECTS.md)) with a full Hebrew translation ([EFFECTS.he.md](library/EFFECTS.he.md)). The catalog itself only analyzes and documents; it does not yet render/export a finished edit. Claude Code can use these recipes inside a video project that has the appropriate rendering/editing engine available. Review the engine's licensing before adding dependencies to a commercial project.

It also includes a phone-friendly local web page for pasting a Reel link or uploading a video. After Claude analyzes it, the page presents suggested effect names and any potential same/similar matches in the existing catalog for review; only then does it add the analysis to the library. Matches do not automatically suppress an entry. The server defaults to loopback (`127.0.0.1`); set `REEL_EFFECTS_HOST` to your LAN IP to open it to your home network.

This is a growing reference library, not model training. Future runs can read the accumulated library as examples. Each entry retains timestamps, evidence, confidence, and a practical recipe for applying the effect to your own footage.

## Use it from an editing agent or skill

The library only documents techniques; your editing tool (a Claude Code skill, an agent, HyperFrames, Remotion, FFmpeg) does the rendering. Give it a one-line lookup:

```bash
/path/to/reel-effect-lab/reel-effects find "speed ramp"            # English or Hebrew words
/path/to/reel-effect-lab/reel-effects find רמפת מהירות --lang he   # recipes printed in Hebrew
/path/to/reel-effect-lab/reel-effects find vhs --json              # structured output for scripts
```

`find` matches every word you give it against names, aliases, tags and recipes in both languages, plus your private analyses, and prints the best matches with their recipes. A ready-to-paste section for your editing skill is in [integrations/editing-skill-snippet.md](integrations/editing-skill-snippet.md). Typical wiring: add a line such as "Before choosing an effect or transition, run `/path/to/reel-effect-lab/reel-effects find <idea>` and follow the recipe it returns" to your editing skill or project `CLAUDE.md`. Alternatively start Claude Code in your video project with `claude --add-dir /path/to/reel-effect-lab` so it can read the library files directly.

## Language and privacy

The web page, the library and Claude's analyses work in English (default) or Hebrew:

```bash
./reel-effects lang he   # Hebrew interface, Hebrew library, analyses written in Hebrew
./reel-effects lang en   # back to English
```

The setting is stored in `local/settings.json` (or set `REEL_EFFECTS_LANG`). Restart the web server after changing it.

Everything personal stays in `local/`, which Git ignores: your analyses (`local/analyses.json`, readable as `local/ANALYSES.md`), the Reel links you analyzed and your settings. The shared library in `library/` holds only general recipes, so you can pull updates and contribute effects without publishing what you analyzed. Back up `local/` if you want to keep your analyses.

If you used an older version that stored analyses inside `library/effects.json`, copy that file somewhere safe before updating, then run `./reel-effects import-analyses <copy-of-old-effects.json>`.

## Requirements

- Python 3.10+
- FFmpeg
- Claude Code CLI installed and authenticated (`claude auth status`)
- `yt-dlp` available to the Python interpreter for Instagram URLs
- Pillow for contact sheets

For a fresh clone, run `./setup.sh` to install the Python dependencies into a project-local virtual environment.

## Use

```bash
./reel-effects add 'https://www.instagram.com/reel/…/'
./reel-effects add ~/Videos/reference.mp4
./reel-effects add --start 4 --end 7 --fps 30 ~/Videos/reference.mp4
./reel-effects list
./reel-effects check   # validate the library after editing it by hand
./reel-effects find zoom # search recipes (English or Hebrew)
./reel-effects lang he # switch the page and analyses to Hebrew
```

## Web page

```bash
.venv/bin/python web_server.py                                   # http://127.0.0.1:4319/ (this computer only)
REEL_EFFECTS_HOST=<your-LAN-IP> .venv/bin/python web_server.py   # reachable from your phone on the same Wi-Fi
```

To keep it running in the background, copy `deploy/reel-effect-lab.service` to `~/.config/systemd/user/`, edit the lines marked `EDIT`, and run `systemctl --user enable --now reel-effect-lab`.

**Security:** the page has no login. Anyone who can reach it can submit videos (which run Claude Code on your account) and view the catalog. Bind it only to `127.0.0.1` or a private home-network address. Never expose it to the public internet.

The web page runs Claude Code automatically in a fresh, non-interactive session for each submitted video. To work with Claude Code interactively instead:

```bash
cd reel-effect-lab
claude
```

Then invoke `/reel-effect-librarian` and ask it to use `library/EFFECTS.md` to suggest how to recreate an effect with your own footage. The repo-local skill is also selected automatically when Claude Code recognizes a relevant request.

If Instagram requires the logged-in browser session, add `--cookies-from-browser chrome` only if that browser profile is already logged in. Or save the video yourself and provide its local path.

`library/effects.json` is the machine-readable source of truth for the shared recipes; `library/EFFECTS.md` and `library/EFFECTS.he.md` are generated readable indexes (`./reel-effects index`). Your analyses live in `local/`, and generated frames, downloaded copies and prompts live in `work/`; both are excluded from Git.

## Claude Code skill

The repo-local skill at `.claude/skills/reel-effect-librarian/SKILL.md` defines the visual-analysis format. The CLI passes those instructions to Claude Code and restricts it to reading files; only the local CLI edits the catalog.

The CLI calls Claude Code in non-interactive print mode. Sign in once with `claude` if `claude auth status` reports `loggedIn: false`; no API key is stored in this repository.

## Notes

- A video file or extracted frames are sent to the user's configured Claude Code account for analysis. Instagram URL downloads use yt-dlp. Nothing is published by this tool.
- Frame sampling catches more rapid changes than a single thumbnail, but even 30 fps can miss sub-frame effects. The report distinguishes visible evidence from inference.
- Be mindful of rights and account/platform restrictions when processing videos.

## Contributing

New effects, recipe fixes and bug reports are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the effect format and checks.

## License

[MIT](LICENSE)
