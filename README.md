# Einführung in die Cyber-Resilienz – Quarto-Projekt

Lehrveranstaltung „Grundlagen der Resilienz“ im Studiengang Cyber Security
Management (B.Sc.), 1. Semester, Hochschule Mainz. Zehn Lehrtermine,
Termin 11 Klausur.

Das Projekt überführt die Unterlagen aus dem Wintersemester 2025/26
(Foliensätze, Vorlesungsskripte, Glossare, Übungsblatt, Probeklausur) in die
Quarto-Struktur des Projekts `csm-geschaeftsprozesse-quarto`. Die Inhalte
wurden übernommen, nicht didaktisch neu konzipiert. Es gibt keine fiktive
Fallorganisation; die Übungsszenarien stammen aus den Archivunterlagen.

## Sofort lesen

Die fertige Ausgabe liegt unter `_output/index.html`. Die Kapitel sind
untereinander und mit den Foliensätzen verlinkt. Die Folien liegen je Termin
als HTML (`Präsentationen/Termin-NN/_output/main.html`) und als bearbeitbare
PowerPoint mit HSM-Vorlage (`Präsentationen/Termin-NN/_powerpoint/main.pptx`)
vor. Das Dozentenpaket beginnt bei `dozenten/_output/regie.html`.

## Voraussetzungen und Rendern

Benötigt wird Quarto (getestete Version siehe PRUEFPROTOKOLL.md). Keine
Python-, R- oder LaTeX-Installation nötig. Nur zum Neuerzeugen der Abbildungen
wird Python mit matplotlib gebraucht (`python assets/abbildungen.py`).

Reihenfolge: zuerst die Foliensätze, dann die Website, dann das
Dozentenprojekt. Die Website übernimmt die fertigen Folien-HTML-Dateien.

Windows (PowerShell):

```powershell
.\render-praesentationen.ps1 -Alle -Format Beide
quarto render
quarto render dozenten
```

Linux/macOS:

```sh
./render-alles.sh
```

Einzelne Kapitel in der Vorschau: `quarto preview termine/05.qmd`.

## Skripte als PDF und Word

`quarto render` erzeugt jedes Terminkapitel und das Glossar zusätzlich als
PDF und als Word-Datei (`_output/termine/01.pdf`, `01.docx` …,
`_output/glossar.pdf`, `glossar.docx`). Die HTML-Seiten verlinken beide unter
„Andere Formate“. Layout wie bei den bisherigen Skripten: Logo „Wirtschaft –
Hochschule Mainz“ oben rechts, Fußzeile mit blauer Linie, Autor, Titel und
Seitenzahl, Vorbemerkung zu Beginn. Die Navigationszeile der Webseite
erscheint nur in HTML.

- **PDF** entsteht über Typst, das in Quarto enthalten ist; LaTeX wird nicht
  benötigt. Seitenlayout, Logo und Fußzeile: `vorlagen/page.typ`.
  Schrift Calibri (Ersatz: Carlito, DejaVu Sans).
- **Word** nutzt `vorlagen/skript-vorlage.docx` als Referenzvorlage. Kopf- und
  Fußzeile sowie Formatvorlagen lassen sich direkt in Word ändern; alternativ
  `python vorlagen/erzeuge_word_vorlage.py` (python-docx) neu ausführen.
- Formate der Terminkapitel stehen in `termine/_metadata.yml`, die
  Vorbemerkung in `termine/_vorbemerkung.md`.
- Nur ein Format rendern: `quarto render termine/05.qmd --to typst` bzw.
  `--to docx`.
Details zum PowerPoint-Export stehen in [POWERPOINT.md](POWERPOINT.md).

## Struktur

- `_quarto.yml`: Sprache, HTML-Format, Renderliste, Ressourcen.
- `index.qmd`: Start und Terminübersicht.
- `konzept.qmd`: Aufbau, Semesterplan, Übungsformate, Kernaussagen.
- `glossar.qmd`: zusammengeführtes Glossar (Sitzungen 3, 4 und 9).
- `quellen.qmd`: Normen, Literatur und **Hinweise zur Aktualität**.
- `termine/01.qmd` bis `11.qmd`: Leitfrage, Lernziele, Fachinhalte aus dem
  Skript, normativer Bezug, Übung, prüfungsrelevante Leitfragen, Material.
- `Präsentationen/Termin-01` bis `Termin-11`: je ein Foliensatz `main.qmd`
  für RevealJS und PowerPoint; `shared/` enthält Theme, Lua-Filter und
  HSM-Referenzvorlage.
- `assets/`: gemeinsame Abbildungen und das Skript, das sie erzeugt.
- `vorlagen/`: HSM-Logo, Typst-Seitenlayout und Word-Referenzvorlage für die Skripte.
- `dozenten/`: Dozentenregie (Sprechernotizen, didaktische Hinweise) und die
  Musterlösung der Probeklausur.
- `literatur.bib`: bibliografische Datensätze.
- `styles.css`: Stil analog zum Projekt Geschäftsprozesse & Organisation.

## Verteilung

An Studierende ausschließlich den Ordner `_output` aus dem Hauptprojekt
verteilen. Er enthält Kapitel und Folien, aber keine Dozentenregie und keine
Musterlösung. Die Trennung erfolgt auf Dateiebene.

## Bewusst nicht übernommen

- Die Folien des Gastvortrags (KPMG, Termin 9) sind Material des Referenten.
- Stock- und Illustrationsbilder der Originalfolien (Campusfotos, Symbolbilder).
  Inhaltliche Grafiken wurden als eigene Abbildungen neu gezeichnet oder als
  Tabellen umgesetzt.
- Das OLAT-Zugangskennwort des Vorsemesters.

Die Originaldateien liegen weiterhin in der Seafile-Bibliothek unter
`Vorlesungen/Cyber Resilienz/Archive WS2526`.

## Offene Punkte vor dem nächsten Semester

Die inhaltlichen Prüfhinweise (NIST-Terminologie, Reifegradskalen, BSIG nach
NIS-2-Umsetzung u. a.) stehen in `quellen.qmd` und im PRUEFPROTOKOLL.md.
Kalenderdaten und das aktuelle OLAT-Kennwort sind noch einzutragen.
