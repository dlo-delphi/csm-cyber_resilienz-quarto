param(
 [ValidateRange(1,11)][int[]]$Termin = @(1),
 [switch]$Alle,
 [ValidateSet('Beide','PowerPoint','HTML')][string]$Format = 'Beide',
 [switch]$Arbeitskopie
)
$ErrorActionPreference = 'Stop'
if ($Alle -and $PSBoundParameters.ContainsKey('Termin')) { throw 'Entweder -Alle oder -Termin angeben.' }
if ($Alle) { $Termin = 1..11 }
$command = Get-Command quarto -ErrorAction SilentlyContinue
if ($command) { $quarto = $command.Source } else {
 $quarto = Join-Path $env:USERPROFILE 'Tools\quarto\bin\quarto.exe'
 if (-not (Test-Path -LiteralPath $quarto)) { throw 'Quarto installieren oder zum PATH hinzufügen.' }
}
if ($Arbeitskopie -and $Format -eq 'HTML') { throw 'Eine Arbeitskopie benötigt den PowerPoint-Export.' }
foreach ($nummer in ($Termin | Select-Object -Unique)) {
$folder = Join-Path $PSScriptRoot ('Präsentationen\Termin-{0:D2}' -f $nummer)
$source = Join-Path $folder 'main.qmd'
if (-not (Test-Path -LiteralPath $source)) { throw "Keine Präsentation gefunden: $source" }
Write-Output ('Termin {0:D2}: {1}' -f $nummer,$Format)
Push-Location $folder
try {
 if ($Format -in @('Beide','HTML')) {
  & $quarto render main.qmd --to revealjs --output-dir _output
  if ($LASTEXITCODE -ne 0) { throw 'HTML-Export fehlgeschlagen.' }
 }
 if ($Format -in @('Beide','PowerPoint')) {
  if ((Get-Content -LiteralPath $source -Raw) -notmatch '(?m)^  pptx:') { throw 'Dieser Termin ist noch nicht für PowerPoint eingerichtet. Siehe POWERPOINT.md.' }
  & $quarto render main.qmd --to pptx --output-dir _powerpoint
  if ($LASTEXITCODE -ne 0) { throw 'PowerPoint-Export fehlgeschlagen.' }
  Write-Output ('PowerPoint: ' + (Join-Path $folder '_powerpoint\main.pptx'))
  if ($Arbeitskopie) {
   $manual = Join-Path $folder 'bearbeitet'
   New-Item -ItemType Directory -Path $manual -Force | Out-Null
   $name = 'Termin-{0:D2}-{1}.pptx' -f $nummer,(Get-Date -Format 'yyyyMMdd-HHmmss-fff')
   $copy = Join-Path $manual $name
   if (Test-Path -LiteralPath $copy) { throw 'Arbeitskopie existiert bereits; bitte erneut starten.' }
   Copy-Item -LiteralPath (Join-Path $folder '_powerpoint\main.pptx') -Destination $copy
   Write-Output ('Arbeitskopie für eigene Visuals: ' + $copy)
  }
 }
} finally { Pop-Location }
}
