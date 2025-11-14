#!/usr/bin/env bash
# macOS: double-click to run in a new Terminal window
set -euo pipefail
cd "$(cd "$(dirname "$0")" && pwd)"

# Clear screen and scrollback so our banner is the first visible line
# (works in Terminal.app and most terminals)
printf '\e[3J\e[H\e[2J'

# Prefer local venv if present
if [[ -x .venv/bin/python ]]; then
  PY=.venv/bin/python
elif command -v python3 >/dev/null 2>&1; then
  PY=python3
else
  PY=python
fi

"$PY" main.py
status=$?

echo
read -n 1 -s -r -p "Press any key to close..."
exit $status