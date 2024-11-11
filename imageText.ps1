Set-Location $PSScriptRoot
.\env/Scripts/Activate.ps1
$text = python imageText.py
deactivate
Write-Output $text
Set-Clipboard -Value $text
Read-Host "("