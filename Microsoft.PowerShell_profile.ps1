function sudo
{
	Start-Process -verb runas
}

function profile
{
	notepad C:\Users\$env:USERNAME\Documents\WindowsPowerShell\Microsoft.PowerShell_profile.ps1
}

function etchosts
{
	Start-Process notepad -Verb runAs "C:\Windows\System32\Drivers\etc\hosts"
}

function rmrf
{
	Param(
		[Parameter(Mandatory=$true)]
		[string[]]$Target
	)
	Remove-Item -Recurse -Force $Target
}
