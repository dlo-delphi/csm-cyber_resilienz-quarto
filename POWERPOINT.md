# Präsentationen als HTML und PowerPoint

Alle 11 Termine verwenden jeweils dieselbe `main.qmd` für die Browserpräsentation und eine bearbeitbare PowerPoint. Die Inhalte stammen aus den Foliensätzen des Wintersemesters 2025/26. Den inhaltlichen Stand zeigt [PRAESENTATIONSSTATUS.md](PRAESENTATIONSSTATUS.md).

## Gesamtes Semester

```powershell
.\render-praesentationen.ps1 -Alle -Format Beide
.\render-praesentationen.ps1 -Termin 3,5,7 -Format PowerPoint -Arbeitskopie
```

Der Export stoppt bei einem Fehler und nennt den betroffenen Termin. Termin 11 enthält den Prüfungsrahmen.

Unter Linux oder macOS rendert `./render-alles.sh` alle Foliensätze, die Kapitel-Website und das Dozentenprojekt in der richtigen Reihenfolge.

## Der normale Ablauf

Im Hauptordner des jeweiligen Repositorys PowerShell öffnen:

```powershell
.\render-praesentationen.ps1 -Termin 1 -Format Beide
```

Nur PowerPoint erzeugen und zusätzlich eine neue Arbeitskopie für eigene Ergänzungen anlegen:

```powershell
.\render-praesentationen.ps1 -Termin 1 -Format PowerPoint -Arbeitskopie
```

Benötigt wird Quarto. Microsoft PowerPoint ist zum Rendern nicht erforderlich, aber zum nachträglichen Bearbeiten sinnvoll. Die PowerShell-Ausführungsrichtlinie muss lokale Skripte erlauben. Alternativ funktionieren die direkten Quarto-Befehle ohne Hilfsskript.

| Datei/Ordner unter `Präsentationen/Termin-01` | Verwendung |
|---|---|
| `main.qmd` | Gemeinsame Inhalte und Formatoptionen |
| `_output/main.html` | Generierte Browserpräsentation |
| `_powerpoint/main.pptx` | Generierte PowerPoint; wird beim nächsten Export ersetzt |
| `bearbeitet/` | Eigene Arbeitskopien mit Visuals und manuellen Anpassungen |
| `assets/` | Bilder, die in beiden Ausgabeformaten erscheinen sollen |

Gemeinsame Abbildungen für Kapitel und Folien (Resilienzkurve, Resilienzzyklus, Eskalationsmodell, Purdue-Modell) liegen im Projektordner `assets/`. Sie werden mit `python assets/abbildungen.py` neu erzeugt (benötigt matplotlib).

Manuelle Änderungen in PowerPoint werden nicht nach QMD zurückübertragen. Für zusätzliche Visuals die Arbeitskopie in `bearbeitet/` verwenden. Der Export schreibt nie in diesen Ordner; der Schalter `-Arbeitskopie` legt lediglich eine neue Datei mit Zeitstempel an.

## Vorlage und Folienmaster

Unter `Präsentationen/shared/` liegen:

- `hsm-wirtschaft-quarto-original.pptx`: unveränderte Kopie der bereitgestellten Vorlage.
- `hsm-wirtschaft-reference.pptx`: für den Quarto-Export vorbereitete Arbeitsfassung.

Die Arbeitsfassung behält HSM-Farben, Schriftvorgaben, Logos und das Seitenformat 16:9. Bereinigt wurden zwei Bearbeitungsprotokoll-Verweise, die Pandoc ohne ihre Zieldateien weitergab. Platzhalter-Fußzeilen wurden durch „Cyber Security Management“ und „Fachbereich Wirtschaft“ ersetzt; Fremdlogo-Musterfelder auf dem Titel entfallen. Der Untertitelplatzhalter ist höher. Im Layout „Content with Caption“ nutzen Tabellen die volle Inhaltsbreite; der Hinweis darüber verwendet eine kleinere, passende Schriftgröße.

Zum Ändern der Gestaltung `hsm-wirtschaft-reference.pptx` in PowerPoint öffnen und unter **Ansicht → Folienmaster** bearbeiten. Quarto übernimmt Layouts und Master, nicht die Beispielinhalte der Vorlage. Die Namen `Title Slide`, `Title and Content`, `Section Header`, `Two Content`, `Comparison`, `Content with Caption` und `Blank` beibehalten. Für Quarto genutzte Platzhalter nicht löschen. Eine andere Vorlage kann über `reference-doc` eingetragen werden; danach die Ausgabe erneut prüfen. Nicht nur den Dateinamen austauschen und ungeprüft verteilen.

Die Vorlage nennt die HSM-Schrift **SimpleStd**. Auf anderen Rechnern sollte diese Schrift verfügbar sein; PowerPoint kann andernfalls eine Ersatzschrift verwenden, wodurch sich Umbrüche ändern. Die Referenzvorlage wurde unverändert aus dem Projekt „Geschäftsprozesse & Organisation“ übernommen und wird in jedem Repository separat gepflegt.

## QMD für beide Formate

Der Kopf von `main.qmd` enthält weiterhin das bisherige `revealjs`-Format und zusätzlich:

```yaml
  pptx:
    reference-doc: ../shared/hsm-wirtschaft-reference.pptx
    slide-level: 2
```

Die Einrückung gehört unter `format:`. Jede Überschrift `##` beginnt eine Folie. Texte und Tabellen bleiben editierbar; Bilder sind separate Bildobjekte. HTML/CSS-Stile werden nicht auf PowerPoint übertragen: Dort steuert der Folienmaster die Gestaltung.

Bei Tabellenfolien steht ein erklärender Hinweis **vor** der Tabelle. Pandoc verwendet damit „Content with Caption“. Text nach einer Tabelle kann sonst eine zusätzliche Folie erzeugen. Eine Tabelle und nachfolgenden Text nicht in eine einzige Spalte einschließen: Dabei kann Text im PowerPoint-Export verloren gehen. Zwei echte Spalten eignen sich für Text neben einem Bild.

Ein Visual für beide Formate integrieren:

```markdown
## Beispiel mit Visual

::: columns
::: {.column width="60%"}
Die Kernaussage und der Arbeitsauftrag.
:::
::: {.column width="35%"}
![](assets/mein-visual.png){fig-alt="Aussagekräftige Beschreibung"}
:::
:::
```

In PowerPoint bestimmen die Platzhalter die Spaltengeometrie; Prozentangaben werden nicht zwingend wie in HTML umgesetzt. Nach Bildänderungen beide Formate kontrollieren. Relative Links zu Leseskript und Arbeitsblatt funktionieren in der Browserfassung; bei separat weitergegebener PPTX die Begleitmaterialien gesondert bereitstellen.

## Direkte Befehle

Im Ordner `Präsentationen/Termin-01`:

```powershell
quarto render main.qmd --to revealjs --output-dir _output
quarto render main.qmd --to pptx --output-dir _powerpoint
```

Bei normalem Rendern des gesamten Terminprojekts kann Quarto beide in `main.qmd` genannten Formate erzeugen. Für die getrennten Ausgabeordner die obigen Befehle oder das Hilfsskript verwenden. Anschließend bei Bedarf das Hauptprojekt rendern, damit die HTML-Kopie in der Semester-Gesamtausgabe aktuell ist.

Grundlage der Konfiguration: [Quarto – PowerPoint-Präsentationen](https://quarto.org/docs/presentations/powerpoint.html).

## Hinweise bei komplexen Folien

Der gemeinsame Filter `Präsentationen/shared/pptx-compatible.lua` wandelt Hinweisboxen beim PowerPoint-Export in bearbeitbaren Text um. Die Arbeitsvorlage verwendet außerdem Objektkennungen außerhalb des von Pandoc für neue Tabellen verwendeten Bereichs. Ein technisches Änderungsdatum wird nur in HTML ausgegeben: Auf der HSM-Titelfolie fehlt der dafür nötige Platzhalter; sonst kann Pandoc ein ungültiges leeres Objekt erzeugen. In HTML bleiben die Boxen erhalten. Diagramme werden von Quarto als Bilder eingebettet; ihre Struktur wird in QMD bearbeitet. Bei komplexen Folien kann PowerPoint zusätzliche Folien erzeugen, weshalb die Folienzahlen von HTML abweichen können. Nach neuen oder umfangreichen Inhalten beide Darstellungen kontrollieren.

Die Konfiguration des Filters folgt den [Quarto-Verarbeitungsphasen](https://quarto.org/docs/advanced/quarto-ast.html).
