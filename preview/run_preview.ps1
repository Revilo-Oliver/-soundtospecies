# Starts the preview static server in a new cmd window and opens the default browser
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Push-Location $scriptDir
Start-Process -FilePath cmd -ArgumentList "/c start ""PreviewServer"" python -m http.server 8001"
Start-Sleep -Seconds 1
Start-Process "http://127.0.0.1:8001/"
Pop-Location
