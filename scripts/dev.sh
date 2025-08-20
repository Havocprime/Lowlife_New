#!/usr/bin/env bash
set -euo pipefail
export PYTHONUNBUFFERED=1
export PYTHONDONTWRITEBYTECODE=1
echo "Starting Lowlife dev runner (Ctrl+C to stop)"
while true; do
  python -X dev bot.py || true
  echo
  echo "--- bot exited; restarting in 2s ---"
  sleep 2
done
