$ErrorActionPreference = "Stop"
$env:PYTHONUNBUFFERED="1"
$env:PYTHONDONTWRITEBYTECODE="1"
Write-Host "Starting Lowlife dev runner (Ctrl+C to stop)`n" -ForegroundColor Cyan
while ($true) {
  python -X dev bot.py
  Write-Host "`n--- bot exited; restarting in 2s ---`n" -ForegroundColor Yellow
  Start-Sleep -Seconds 2
}
