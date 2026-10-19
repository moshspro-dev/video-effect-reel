#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
printf '\nSetup complete. Make sure FFmpeg and Claude Code are installed, then authenticate with: claude\n'
