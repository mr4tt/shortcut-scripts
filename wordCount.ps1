Get-Clipboard | Write-Output 
Get-Clipboard | Measure-Object -Line -Character -Word | Out-String
Read-Host "("