# Lowlife Society — Bot

Discord-first MMORPG sandbox.

## Quickstart (Windows PowerShell)
```powershell
# 1) Create and activate virtual env
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2) Install deps
pip install -r requirements.txt

# 3) Create .env from template
copy .env.example .env
# Edit .env and fill: DISCORD_BOT_TOKEN, GUILD_ID, UPDATELOG_CHANNEL_ID

# 4) Run dev loop (auto-restart)
.\scripts\dev.ps1
```

## One-off run
```powershell
python bot.py
```

## Scripts
- `scripts/dev.ps1` — dev runner with auto-restart.
- `scripts/sync_commands.py` — optional: force re-sync slash commands to a guild.

## Tests
```powershell
pytest -q
```

## Versioning
The runtime version lives in `version.py`. Embed posts (e.g., updatelogs) should import `__version__` to stamp messages.

## Structure (flat for now; migrate to src/ later)
- Core modules at repo root (`bot.py`, `embeds.py`, `rules.py`, etc.).
- Assets in `assets/` (images, tilesets).

## Notes
- The default tileset background uses the braille blank `U+2800` to avoid Discord trimming.
- Keep secrets out of git. Commit `.env.example`, **not** `.env`.
