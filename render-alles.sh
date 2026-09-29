#!/usr/bin/env bash
# Rendert Foliensätze (HTML + PowerPoint), die Kapitel-Website und das Dozentenprojekt.
# Reihenfolge ist wichtig: Die Website übernimmt die fertigen Folien-HTML-Dateien als Ressourcen.
# Unter Windows entsprechend: .\render-praesentationen.ps1 -Alle -Format Beide ; quarto render ; quarto render dozenten
set -euo pipefail
cd "$(dirname "$0")"
for dir in Präsentationen/Termin-*/; do
  echo "== ${dir}"
  (cd "$dir" && quarto render main.qmd --to revealjs --output-dir _output \
             && quarto render main.qmd --to pptx --output-dir _powerpoint)
done
quarto render
quarto render dozenten
echo "Fertig: _output/index.html, dozenten/_output/regie.html"
