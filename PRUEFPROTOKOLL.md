# Prüfprotokoll

Stand: 29. September 2026. Quarto 1.10.18 unter Linux (Cloud-Umgebung).

## Renderfähigkeit

- 11 Foliensätze erfolgreich als RevealJS-HTML und als PowerPoint (HSM-Referenzvorlage) gerendert.
- Hauptprojekt erfolgreich gerendert: 15 HTML-Dokumente (Start, Konzept, Glossar, Quellen, 11 Terminkapitel), Foliensätze als Ressourcen übernommen.
- Dozentenprojekt erfolgreich gerendert: 2 HTML-Dokumente (Regie, Lösungen).
- Alle 198 Folien der HTML-Fassung automatisiert bei 1280 × 720 geprüft: kein Inhalt ragt über den Folienrand.
- PowerPoint-Stichproben (Termine 2, 6, 9) über LibreOffice als Bild kontrolliert: Tabellen im Layout „Content with Caption“, Abbildungen und Zweispalter korrekt.
- Alle lokalen Verweise in der gerenderten Ausgabe zeigen auf vorhandene Dateien; der Anker „Hinweise zur Aktualität“ existiert.

**Hinweis:** In der Renderumgebung war fonts.googleapis.com nicht erreichbar. Die Schrift „Source Sans Pro“ des Themes ist deshalb nicht eingebettet; die Seiten fallen auf eine Systemschrift zurück. Ein erneutes Rendern mit Internetzugang (`render-praesentationen.ps1 -Alle`, `quarto render`, `quarto render dozenten`) behebt das.

## Inhaltliche Vollständigkeit

- Für jeden Termin 1–10 wurden Foliensatz und Skript vollständig gelesen und übertragen; Termin 1 aus der PPTX einschließlich Sprechernotizen.
- Glossare der Sitzungen 3 und 4 sowie das OT-/KI-Glossar aus Skript 9 sind in `glossar.qmd` zusammengeführt.
- Übungsblatt Sitzung 8 (GameNova) vollständig mit Punkteverteilung in Termin 8.
- Probeklausur: alle 20 Fragen in Termin 11 automatisiert gegen den Quelltext geprüft (einzige Abweichung: Schreibweise „Disaster“ statt „Desaster“); Musterlösung vollständig im Dozentenprojekt.
- Prüfungsrelevante Leitfragen aus den Skripten stehen in den Kapiteln; für Termin 6 als Auswahl (das Skript enthält 40 Fragen). Für Termin 10 enthält das Skript keine Leitfragen; die im Kapitel genannten sind aus den Lernzielen abgeleitet und so gekennzeichnet.

## Bewusste Abweichungen vom Archiv

- Semesterplan folgt den tatsächlich gehaltenen Sitzungen, nicht der ursprünglichen Vorlesungsübersicht (siehe `konzept.qmd`). Ausblicksfolien auf Sitzung 9 und 10 entsprechend angepasst.
- OLAT-Kennwort des Vorsemesters entfernt.
- Gastvortragsfolien (KPMG) und Stock-/Symbolbilder nicht übernommen; inhaltliche Grafiken (Resilienzkurve, Resilienzzyklus, Eskalationsmodell, Purdue-Modell) neu gezeichnet, SOC-Tier-Grafik und Konfliktdarstellungen als Tabellen.
- NIS-2-Richtlinie mit korrekter Nummer (EU) 2022/2555 statt „EU 2023/2555“.
- Termin 7: Die sehr knappen Originalfolien wurden mit Kernaussagen aus dem Skript ergänzt.

## Fachliche Prüfhinweise für die nächste Überarbeitung

Die Kapitel übernehmen die Archivinhalte. Folgende Punkte sollten fachlich entschieden werden; Details in `quellen.qmd`, Abschnitt „Hinweise zur Aktualität“:

1. NIST SP 800-160 Vol. 2 Rev. 1: Ziele Anticipate, Withstand, Recover, Adapt statt „Resist, Recover, Re-Constitute, Adapt/Re-architect“.
2. ISO/IEC 27031:2025 als neue Ausgabe.
3. BSI-Standard 200-4 (Mai 2023): Stufen Reaktiv-, Aufbau-, Standard-BCMS; die fünfstufigen Reifegradskalen tragen in Folien und Skripten vier verschiedene Bezeichnungssätze.
4. BSIG nach NIS2UmsuCG (in Kraft seit 6. Dezember 2025): Verweise auf § 8b BSIG (alt) und § 30 BSIG prüfen.
5. NIST SP 800-61 Rev. 3 (April 2025) ersetzt Rev. 2.
6. NIST CSF 2.0 mit sechs Funktionen (Govern ergänzt).
7. NIST SP 800-82 Rev. 3: neuer Titel „Guide to Operational Technology (OT) Security“.
8. ISO/IEC 27035: Phasengliederung der Folien entspricht eher NIST SP 800-61 Rev. 2.
9. Nicht geprüfte Quellenangaben aus den Skripten: ENISA Good Practice Guide for Incident Management (2021), SANS Incident Response Survey (2024), ENISA Threat Landscape (2024).
10. Schreibweise des Gastreferenten: „Gronenwald“ (Referentenfolien) statt „Groenenwald“ (Vorlesungsfolien).
11. Skript 5, Kapitel 10.3 kündigt für Sitzung 6 „Messen, steuern, nachweisen“ an; gehalten wurde „Rollen und Verantwortlichkeiten“.

Die Prüfung umfasst Renderfähigkeit, Dateistruktur, Vollständigkeit der Übertragung und Verweise. Eine Erprobung mit Studierenden oder eine Prüfung gegen die Normtexte wurde nicht durchgeführt.
