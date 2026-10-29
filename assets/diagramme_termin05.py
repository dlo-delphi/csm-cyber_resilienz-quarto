"""Diagramme für den Foliensatz Termin 5 „Resilienz als Organisationsfähigkeit“.

Aufruf im Projektordner:  python assets/diagramme_termin05.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-05/assets/.
Gestaltung wie die Diagramme in Termin 1–4 (Inter, Navy-Rahmen, helle Flächen).
Alle Darstellungen sind schematisch; Zahlen stammen aus den in quellen.qmd genannten Quellen.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Präsentationen" / "Termin-05" / "assets"

NAVY = "#1f3a5f"
RED = "#c0392b"
GREEN = "#2e7d4f"
GREY = "#555555"
LGREY = "#9a9a9a"
CREAM = "#fbf6e6"
ICE = "#eef3f8"
ROSE = "#f8efe9"
MINT = "#ecf5ef"
PINK = "#f9e9e9"
LILAC = "#f0edf6"
ORANGE = "#d9822b"

_inter = [f.name for f in font_manager.fontManager.ttflist if f.name == "Inter"]
plt.rcParams.update({
    # DejaVu Sans als Fallback für Symbole wie ✔ und ✘, die Inter nicht enthält
    "font.family": ["Inter", "DejaVu Sans"] if _inter else ["DejaVu Sans"],
    "font.size": 12,
    "axes.edgecolor": "#222222",
})


def save(fig, name):
    OUT.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / name, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.25)
    plt.close(fig)


def canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, xl)
    ax.set_ylim(0, yl)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text="", fc=ICE, ec=NAVY, fs=12, color="#222222", bold=True, lw=2.2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0,rounding_size=0.18",
                                fc=fc, ec=ec, lw=lw))
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color,
                fontweight="bold" if bold else "normal", linespacing=1.35)


def text(ax, x, y, s, size=12, color="#222222", bold=False, ha="center", va="center", **kw):
    ax.text(x, y, s, ha=ha, va=va, fontsize=size, color=color,
            fontweight="bold" if bold else "normal", linespacing=1.35, **kw)


def arrow(ax, a, b, color=GREY, rad=0.0, lw=2.2, style="-|>", ms=18):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=ms, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}"))


def cross(ax, x, y, w, h, color=RED):
    ax.plot([x + 0.05, x + w - 0.05], [y + 0.05, y + h - 0.05], color=color, lw=3, alpha=0.35)
    ax.plot([x + 0.05, x + w - 0.05], [y + h - 0.05, y + 0.05], color=color, lw=3, alpha=0.35)


def timeline(ax, yt, marks, x0=0.4, x1=12.6, band=None):
    """Waagerechte Zeitleiste; marks = (x, Zeit, Text, Farbe, oben?)."""
    ax.plot([x0, x1], [yt, yt], color="#222222", lw=2)
    if band:
        bx0, bx1 = band
        ax.add_patch(FancyBboxPatch((bx0, yt - 0.18), bx1 - bx0, 0.36, boxstyle="round,pad=0,rounding_size=0.1",
                                    fc=PINK, ec=RED, lw=1.5))
    for x, d, lab, c, up in marks:
        ax.plot([x, x], [yt - 0.25, yt + 0.25], color=c, lw=3.5)
        if up:
            text(ax, x, yt + 0.75, d, 11, c, bold=True)
            text(ax, x, yt + 2.0, lab, 9.2, "#222222")
        else:
            text(ax, x, yt - 0.75, d, 11, c, bold=True)
            text(ax, x, yt - 2.0, lab, 9.2, "#222222")


# --------------------------------------------------------------------------------------
def norsk_hydro_2019():
    """Norsk Hydro 19.03.2019: IT verschlüsselt, Organisation arbeitet weiter."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 7.9, 12.4, 1.4, "19.03.2019 · Ransomware LockerGoga\nrund 35.000 Beschäftigte in 40 Ländern betroffen",
        fc=PINK, ec=RED, fs=10.5, color=RED)
    text(ax, 3.25, 7.15, "Was ausfiel", 12.5, RED, bold=True)
    text(ax, 9.75, 7.15, "Was trug", 12.5, GREEN, bold=True)
    lost = ["Arbeitsplatzrechner\nund Server", "Verbindung zu\nProduktionssystemen", "Teile der Fertigung\n(Strangpressen)"]
    held = ["Anlagen isoliert, Arbeit\nmanuell weitergeführt", "Pressekonferenz am\nersten Tag, laufend Updates", "kein Lösegeld –\nWiederaufbau aus Backups"]
    for i, (a, b) in enumerate(zip(lost, held)):
        y = 5.35 - i * 1.5
        box(ax, 0.3, y, 5.9, 1.25, a, fc=PINK, ec=RED, fs=9.8, bold=False)
        box(ax, 6.8, y, 5.9, 1.25, b, fc=MINT, ec=GREEN, fs=9.8, bold=False)
    box(ax, 0.3, 0.3, 12.4, 1.5, "Technik fiel – Entscheidungen, Rollen und Kommunikation trugen\n(Gesamtkosten nach Hydro rund 800 Mio. NOK)",
        fc=ICE, ec=NAVY, fs=10.5)
    save(fig, "norsk-hydro-2019.png")


# --------------------------------------------------------------------------------------
def vier_komponenten():
    """Vier Kernkomponenten organisationaler Resilienz über der technischen Basis."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Organisation aktiviert das Potenzial", 13.5, NAVY, bold=True)
    tiles = [("Strukturen", "Rollen und\nVerantwortung", ICE, NAVY),
             ("Prozesse", "erkennen, reagieren,\nwiederanlaufen", CREAM, ORANGE),
             ("Menschen", "Ausbildung, Training,\nEntscheidungsfähigkeit", LILAC, NAVY),
             ("Kultur", "Fehleroffenheit,\nLernfähigkeit", MINT, GREEN)]
    for i, (t, s, fc, ec) in enumerate(tiles):
        col, row = i % 2, i // 2
        x, y = 0.3 + col * 6.3, 5.6 - row * 2.75
        box(ax, x, y, 6.1, 2.5, "", fc=fc, ec=ec)
        text(ax, x + 3.05, y + 1.75, t, 13, ec, bold=True)
        text(ax, x + 3.05, y + 0.8, s, 10, "#222222")
    box(ax, 0.3, 0.3, 12.4, 1.9, "Technik schafft Potenzial:\nRedundanz · Diversität · Wiederherstellbarkeit · Adaptivität",
        fc="#f2f2f2", ec=LGREY, fs=10.5, color=GREY)
    for x in (3.35, 9.65):
        arrow(ax, (x, 2.25), (x, 2.8), color=LGREY, lw=1.8, ms=13)
    save(fig, "vier-komponenten.png")


# --------------------------------------------------------------------------------------
def anhalt_bitterfeld_2021():
    """Landkreis Anhalt-Bitterfeld 2021: Katastrophenfall und Krisenstab nach Ransomware."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    steps = [("6.7.2021", "Ransomware verschlüsselt die IT\nder Kreisverwaltung", PINK, RED),
             ("9.7.2021", "Katastrophenfall ausgerufen – der erste\nnach einem Cyberangriff in Deutschland", CREAM, ORANGE),
             ("danach", "Krisenstab mit Bundeswehr, BSI, LKA,\nCERT Nord und Landesverwaltung", ICE, NAVY),
             ("Folgen", "Sozialhilfe, Eltern- und Kindergeld\nzeitweise nicht auszahlbar", PINK, RED),
             ("März 2022", "40 von 159 Fachanwendungen laufen wieder", MINT, GREEN)]
    for i, (d, s, fc, ec) in enumerate(steps):
        y0 = 8.0 - i * 1.85
        text(ax, 1.3, y0 + 0.6, d, 9.5, ec, bold=True)
        box(ax, 2.6, y0, 7.3, 1.25, s, fc=fc, ec=ec, fs=9, bold=False)
        if i < len(steps) - 1:
            arrow(ax, (6.25, y0 - 0.02), (6.25, y0 - 0.55), color=GREY, lw=1.8, ms=13)
    box(ax, 10.2, 1.8, 2.75, 6.4, "", fc="#f8f8f8", ec=NAVY, lw=1.8)
    text(ax, 11.57, 7.6, "Muster", 12, NAVY, bold=True)
    text(ax, 11.57, 5.5, "Entschei-\ndungs-\nkompetenz\nauf Zeit", 10.5, "#222222", bold=True)
    text(ax, 11.57, 3.1, "kein\nLösegeld", 10, GREEN, bold=True)
    save(fig, "anhalt-bitterfeld-2021.png")


# --------------------------------------------------------------------------------------
def atlassian_2022_zeitleiste():
    """Atlassian April 2022: Löschskript, Kommunikationslücke und zwei Wochen Wiederherstellung."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "883 Sites von 775 Kunden gelöscht · April 2022", 12.5, RED, bold=True)
    marks = [(1.0, "5.4. 07:38", "Skript löscht Sites\nstatt einer App\n(falsche ID-Art)", RED, True),
             (3.6, "5.4. 09:03", "erste Meldung\nauf der\nStatusseite", ORANGE, False),
             (6.2, "7.4.", "erste breite\nöffentliche\nStellungnahme", ORANGE, True),
             (8.8, "8.4.", "erste Kunden\nwiederhergestellt", NAVY, False),
             (11.9, "18.4.", "alle Kunden\nwiederhergestellt", GREEN, True)]
    timeline(ax, 5.3, marks, band=(1.0, 11.9))
    box(ax, 0.4, 0.3, 12.2, 1.6, "Die Kontaktdaten der Kunden lagen in den gelöschten Instanzen –\nKommunikation braucht eine Ablage außerhalb des Systems",
        fc=CREAM, ec=NAVY, fs=9.8)
    save(fig, "atlassian-2022-zeitleiste.png")


# --------------------------------------------------------------------------------------
def ir_phasen():
    """Incident-Management-Prozess nach ISO/IEC 27035-1:2023 mit operativer Feingliederung."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "ISO/IEC 27035-1:2023 – fünf Phasen", 13, NAVY, bold=True)
    phases = [("Planen und\nvorbereiten", ICE, NAVY), ("Erkennen\nund melden", CREAM, ORANGE),
              ("Bewerten,\nentscheiden", CREAM, ORANGE), ("Reagieren", PINK, RED),
              ("Lehren\nziehen", MINT, GREEN)]
    w, gap = 2.3, 0.22
    for i, (s, fc, ec) in enumerate(phases):
        x = 0.3 + i * (w + gap)
        box(ax, x, 6.3, w, 1.9, s, fc=fc, ec=ec, fs=9.2, color=ec)
        if i < len(phases) - 1:
            arrow(ax, (x + w + 0.01, 7.25), (x + w + gap - 0.01, 7.25), color=GREY, lw=1.6, ms=11)
    arrow(ax, (11.6, 6.25), (1.45, 6.25), color=GREEN, rad=-0.18, lw=1.8, ms=14)
    text(ax, 6.5, 4.75, "Lessons Learned fließen in die Vorbereitung zurück", 9.5, GREEN, bold=True)
    xr = 0.3 + 3 * (w + gap) + w / 2
    arrow(ax, (xr, 4.4), (xr, 3.55), color=RED, lw=1.6, ms=12, style="-")
    box(ax, 0.3, 1.9, 12.4, 1.6, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 6.5, 3.05, "operativ verfeinert (wie NIST SP 800-61 Rev. 2)", 9.5, GREY, bold=True)
    for i, s in enumerate(["Eindämmen", "Beseitigen", "Wiederherstellen"]):
        box(ax, 1.0 + i * 3.9, 2.05, 3.3, 0.75, s, fc=PINK, ec=RED, fs=9.5, bold=False, lw=1.5)
    box(ax, 0.3, 0.2, 12.4, 1.3, "Jede Phase braucht Owner, Playbooks\nund Kommunikationskanäle",
        fc=ICE, ec=NAVY, fs=10)
    save(fig, "ir-phasen.png")


# --------------------------------------------------------------------------------------
def rpk_2022_verlauf():
    """Rhein-Pfalz-Kreis ab Ende Oktober 2022: Ransomware, Datenveröffentlichung, Notbetrieb."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    steps = [("Ende Okt.\n2022", "Ransomware – nachts zieht ein Beschäftigter\nden Stecker und begrenzt den Schaden", PINK, RED),
             ("danach", "Rechner offline, weder E-Mail\nnoch Durchwahlen erreichbar", PINK, RED),
             ("Lösegeld", "nicht gezahlt – ab 11.11. rund\n20.000 Dateien im Darknet", CREAM, ORANGE),
             ("Betroffene", "Warnung und Verhaltenshinweise,\nrund 2.550 Briefe", ICE, NAVY),
             ("Notbetrieb", "Laptop und Drucker, Excel-Listen,\nzentrale Rufnummer, Kontaktformular", MINT, GREEN)]
    for i, (d, s, fc, ec) in enumerate(steps):
        y0 = 8.0 - i * 1.85
        text(ax, 1.3, y0 + 0.6, d, 9.5, ec, bold=True)
        box(ax, 2.6, y0, 7.3, 1.25, s, fc=fc, ec=ec, fs=9, bold=False)
        if i < len(steps) - 1:
            arrow(ax, (6.25, y0 - 0.02), (6.25, y0 - 0.55), color=GREY, lw=1.8, ms=13)
    box(ax, 10.2, 1.8, 2.75, 6.4, "", fc="#f8f8f8", ec=NAVY, lw=1.8)
    text(ax, 11.57, 7.6, "Muster", 12, NAVY, bold=True)
    text(ax, 11.57, 5.6, "jede\nPhase\nhat eine\nRolle", 10.5, "#222222", bold=True)
    text(ax, 11.57, 3.1, "Landes-\nhilfe in\n3 Stufen", 10, GREEN, bold=True)
    save(fig, "rpk-2022-verlauf.png")


# --------------------------------------------------------------------------------------
def uebungsformen():
    """Übungsformen nach Aufwand und Realitätsnähe, verbunden durch das After-Action Review."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    forms = [("Tabletop", "Planspiel am Tisch:\nRollen, Entscheidungen,\nKommunikation", ICE, NAVY, 0.3, 2.6),
             ("Funktionstest", "einzelne Abläufe real:\nRestore, Alarmierung,\nNotfallkanal", CREAM, ORANGE, 4.55, 4.0),
             ("Live-Simulation", "Systeme werden\nwirklich gestört:\nRed Team, Failover", PINK, RED, 8.8, 5.4)]
    for t, s, fc, ec, x, h in forms:
        box(ax, x, 2.3, 3.9, h, "", fc=fc, ec=ec)
        text(ax, x + 1.95, 2.3 + h - 0.55, t, 11.5, ec, bold=True)
        text(ax, x + 1.95, 2.3 + h - 1.75, s, 9, "#222222")
    arrow(ax, (0.4, 8.6), (12.6, 8.6), color=GREY, lw=2, ms=16)
    text(ax, 6.5, 9.15, "Aufwand und Realitätsnähe steigen", 10.5, GREY, bold=True)
    box(ax, 0.3, 0.2, 12.4, 1.5, "nach jeder Übung: After-Action Review ohne Schuldzuweisung\nErgebnisse in Playbooks und Schulungen",
        fc=MINT, ec=GREEN, fs=10.5, color="#222222")
    save(fig, "uebungsformen.png")


# --------------------------------------------------------------------------------------
def luekex_23():
    """LÜKEX 23: Krisenmanagementübung von Bund und Ländern zu einem Cyberangriff."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 7.2, 12.4, 1.9, "LÜKEX 23 · 27.–28. September 2023\nSzenario: Cyberangriff auf das Regierungshandeln",
        fc=ICE, ec=NAVY, fs=11.5)
    tiles = [("> 50", "Behörden"), ("> 1.000", "Mitwirkende"), ("8", "Länder voll\nbeteiligt")]
    for i, (n, s) in enumerate(tiles):
        x = 0.3 + i * 4.2
        box(ax, x, 4.2, 3.9, 2.4, "", fc=CREAM, ec=ORANGE)
        text(ax, x + 1.95, 5.85, n, 17, ORANGE, bold=True)
        text(ax, x + 1.95, 4.85, s, 10, "#222222")
    text(ax, 6.5, 3.55, "Federführung BBK · keine Einsatzkräfte, keine Bevölkerung", 9.5, GREY)
    box(ax, 0.3, 0.3, 12.4, 2.6, "", fc=MINT, ec=GREEN)
    text(ax, 6.5, 2.35, "Geübt wurden vor allem", 11, GREEN, bold=True)
    text(ax, 6.5, 1.15, "Melde- und Kommunikationswege · Zusammenspiel von\nKrisen- und IT-Notfallmanagement · Krisenkommunikation", 10, "#222222")
    save(fig, "luekex-23.png")


# --------------------------------------------------------------------------------------
def schuld_oder_lernen():
    """Zwei Fragen nach einem Vorfall – und was sie in der Organisation bewirken."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 2.6, 5.9, 6.5, "", fc=PINK, ec=RED)
    text(ax, 3.25, 8.3, "„Wer war schuld?“", 13, RED, bold=True)
    for i, s in enumerate(["Fehler werden versteckt", "Meldungen kommen spät", "derselbe Fehler kehrt\nzurück"]):
        text(ax, 3.25, 6.7 - i * 1.45, s, 10.5, "#222222")
    box(ax, 6.8, 2.6, 5.9, 6.5, "", fc=MINT, ec=GREEN)
    text(ax, 9.75, 8.3, "„Was verbessern wir?“", 13, GREEN, bold=True)
    for i, s in enumerate(["Fehler werden gemeldet", "Ursachen im System\nstatt bei Personen", "Leitplanken verhindern\nWiederholung"]):
        text(ax, 9.75, 6.7 - i * 1.45, s, 10.5, "#222222")
    box(ax, 0.3, 0.3, 12.4, 1.8, "Psychologische Sicherheit ist die Voraussetzung\nfür ehrliche Post-Mortems",
        fc=ICE, ec=NAVY, fs=11)
    save(fig, "schuld-oder-lernen.png")


# --------------------------------------------------------------------------------------
def cloudflare_2019_zeitleiste():
    """Cloudflare 02.07.2019: eine WAF-Regel legt das Netz 27 Minuten lahm (Zeiten UTC)."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "bis zu 82 % weniger Verkehr · 27 Minuten · 2. Juli 2019", 12, RED, bold=True)
    marks = [(1.0, "13:42", "neue WAF-Regel\nweltweit auf\neinmal ausgerollt", RED, True),
             (3.4, "13:45", "erster Alarm,\n502-Fehler\nweltweit", ORANGE, False),
             (6.2, "14:00", "WAF als Ursache\nerkannt, Angriff\nausgeschlossen", NAVY, True),
             (8.9, "14:07", "WAF global\nabgeschaltet\n(Notzugang nötig)", NAVY, False),
             (11.9, "14:09", "Verkehr\nwieder normal", GREEN, True)]
    timeline(ax, 5.3, marks, band=(1.0, 11.9))
    box(ax, 0.4, 0.3, 12.2, 1.6, "Post-Mortem nach zehn Tagen: Prozess- und Testlücken benannt,\nkeine Schuldigen – gestufter Rollout als Leitplanke",
        fc=CREAM, ec=NAVY, fs=9.8)
    save(fig, "cloudflare-2019-zeitleiste.png")


if __name__ == "__main__":
    norsk_hydro_2019()
    vier_komponenten()
    anhalt_bitterfeld_2021()
    atlassian_2022_zeitleiste()
    ir_phasen()
    rpk_2022_verlauf()
    uebungsformen()
    luekex_23()
    schuld_oder_lernen()
    cloudflare_2019_zeitleiste()
    print("Diagramme erzeugt in", OUT)
