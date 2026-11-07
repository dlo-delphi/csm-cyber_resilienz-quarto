"""Diagramme für den Foliensatz Termin 6 „Rollen und Verantwortlichkeiten“.

Aufruf im Projektordner:  python assets/diagramme_termin06.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-06/assets/.
Gestaltung wie die Diagramme in Termin 1–5 (Inter, Navy-Rahmen, helle Flächen).
Alle Darstellungen sind schematisch; Zahlen stammen aus den in quellen.qmd genannten Quellen.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Präsentationen" / "Termin-06" / "assets"

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
def target_2013_zeitleiste():
    """Target 2013: Alarme kamen an, Entscheidungen blieben aus."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "40 Mio. Karten · bis zu 70 Mio. Kundendatensätze", 12.5, RED, bold=True)
    marks = [(1.0, "27.11.", "Kassen-Malware\naktiv (Zugang über\nDienstleister)", RED, True),
             (3.6, "30.11.", "Alarm: Team in\nBangalore meldet\nan Minneapolis", ORANGE, False),
             (6.2, "2.12.", "weitere Alarme –\nkeine Reaktion", ORANGE, True),
             (8.9, "12.12.", "Justizministerium\ninformiert Target", NAVY, False),
             (11.9, "19.12.", "Target geht\nan die\nÖffentlichkeit", NAVY, True)]
    timeline(ax, 5.3, marks, band=(3.6, 8.9))
    box(ax, 0.4, 0.3, 12.2, 1.6, "Erkennen hat funktioniert – Eskalation und Entscheidung nicht.\nEinen CISO gab es nicht; Sicherheit war auf mehrere Führungskräfte verteilt",
        fc=CREAM, ec=NAVY, fs=8.8)
    save(fig, "target-2013-zeitleiste.png")


# --------------------------------------------------------------------------------------
def mandat_dreieck():
    """Mandat des CISO: Verantwortung, Befugnis, Ressourcen, Berichtsweg."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Ein Mandat hat drei Seiten", 13.5, NAVY, bold=True)
    ax.add_patch(plt.Polygon([(6.5, 8.0), (1.9, 2.6), (11.1, 2.6)], closed=True, fc=ICE, ec=NAVY, lw=2.2))
    box(ax, 4.6, 7.55, 3.8, 1.05, "Verantwortung", fc="white", ec=NAVY, fs=11, color=NAVY)
    box(ax, 0.3, 1.9, 3.8, 1.05, "Befugnis", fc="white", ec=ORANGE, fs=11, color=ORANGE)
    box(ax, 8.9, 1.9, 3.8, 1.05, "Ressourcen", fc="white", ec=GREEN, fs=11, color=GREEN)
    text(ax, 6.5, 4.9, "Berichtsweg zur\nGeschäftsleitung", 11.5, NAVY, bold=True)
    text(ax, 6.5, 3.55, "trägt das Dreieck", 9.5, GREY)
    box(ax, 0.3, 0.2, 12.4, 1.25, "Fehlt eine Seite: „Accountability without Authority“",
        fc=PINK, ec=RED, fs=10.5, color=RED)
    save(fig, "mandat-dreieck.png")


# --------------------------------------------------------------------------------------
def uber_2016_zeitleiste():
    """Uber 2016: Vertuschung eines Vorfalls und die strafrechtlichen Folgen für den CSO."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "57 Mio. Nutzerdatensätze · 600.000 Führerscheinnummern", 12, RED, bold=True)
    marks = [(1.0, "Nov. 2016", "Angreifer melden\nsich beim CSO,\nfordern Geld", RED, True),
             (3.6, "Dez. 2016", "100.000 USD als\n„Bug Bounty“,\nSchweigeerklärung", RED, False),
             (6.2, "Nov. 2017", "neue Leitung\ndeckt auf und\nveröffentlicht", NAVY, True),
             (8.9, "Okt. 2022", "CSO verurteilt:\nBehinderung, Ver-\nschleierung", ORANGE, False),
             (11.9, "Juni 2026", "Supreme Court\nnimmt Revision\nnicht an", ORANGE, True)]
    timeline(ax, 5.3, marks, band=(1.0, 6.2))
    box(ax, 0.4, 0.3, 12.2, 1.6, "Zur selben Zeit lief eine FTC-Untersuchung zu einem früheren Vorfall –\nder Vorfall wurde an Rechtsabteilung und Aufsicht vorbeigesteuert",
        fc=CREAM, ec=NAVY, fs=9.6)
    save(fig, "uber-2016-zeitleiste.png")


# --------------------------------------------------------------------------------------
def ciso_haftung():
    """Uber und SolarWinds: zwei Verfahren gegen Sicherheitschefs, zwei Ergebnisse."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    cols = [("Uber · Joe Sullivan", "Strafverfahren (DOJ)", PINK, RED,
             ["Vorfall verschwiegen,\nZahlung getarnt", "verurteilt 2022,\nbestätigt 2025", "rechtskräftig seit\nJuni 2026"]),
            ("SolarWinds · Tim Brown", "Zivilverfahren (SEC)", CREAM, ORANGE,
             ["Vorwurf: öffentliche Aus-\nsagen ≠ interne Kenntnis", "2024 größtenteils\nabgewiesen", "Nov. 2025 eingestellt,\nkein Schuldeingeständnis"])]
    for i, (t, s, fc, ec, rows) in enumerate(cols):
        x = 0.3 + i * 6.5
        box(ax, x, 2.4, 5.9, 6.9, "", fc=fc, ec=ec)
        text(ax, x + 2.95, 8.65, t, 11.5, ec, bold=True)
        text(ax, x + 2.95, 7.95, s, 9.5, GREY)
        for j, r in enumerate(rows):
            box(ax, x + 0.35, 5.9 - j * 1.65, 5.2, 1.35, r, fc="white", ec=ec, fs=9.3, bold=False, lw=1.5)
    box(ax, 0.3, 0.2, 12.4, 1.75, "Gemeinsame Lehre: Eskalation dokumentieren,\nMeldeentscheidungen nicht allein treffen",
        fc=ICE, ec=NAVY, fs=10.5)
    save(fig, "ciso-haftung.png")


# --------------------------------------------------------------------------------------
def cert_landschaft():
    """CERT-Landschaft: von der eigenen Organisation bis zur nationalen Ebene."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "Wer hilft wem? CERT-Ebenen", 13.5, NAVY, bold=True)
    box(ax, 4.4, 3.9, 4.2, 2.0, "eigenes CERT\n(Internal CERT)", fc=ICE, ec=NAVY, fs=11, color=NAVY)
    outer = [(0.3, 6.6, "national", "CERT-Bund (BSI),\nMobile Incident\nResponse Teams", CREAM, ORANGE),
             (8.7, 6.6, "Land / Kommune", "z. B. kommunales\nCERT Rheinland-Pfalz", MINT, GREEN),
             (0.3, 0.6, "Wissenschaft", "DFN-CERT für Hoch-\nschulen und\nForschung", LILAC, NAVY),
             (8.7, 0.6, "Branche", "sektorale CERTs,\nz. B. Finanzen,\nEnergie", PINK, RED)]
    for x, y, t, s, fc, ec in outer:
        box(ax, x, y, 4.0, 2.2, "", fc=fc, ec=ec)
        text(ax, x + 2.0, y + 1.75, t, 10.5, ec, bold=True)
        text(ax, x + 2.0, y + 0.8, s, 8.6, "#222222")
    for a, b in [((4.3, 7.2), (5.2, 5.95)), ((8.7, 7.2), (7.8, 5.95)),
                 ((4.3, 2.2), (5.2, 3.85)), ((8.7, 2.2), (7.8, 3.85))]:
        arrow(ax, a, b, color=LGREY, lw=1.8, ms=13, style="<|-|>")
    text(ax, 6.5, 7.7, "Austausch über\nFIRST, TF-CSIRT,\nCERT-Verbund", 8.6, GREY)
    save(fig, "cert-landschaft.png")


# --------------------------------------------------------------------------------------
def ukd_2020_akteure():
    """Uniklinik Düsseldorf 2020: viele Rollen von außen rund um einen Vorfall."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 7.9, 12.4, 1.4, "10.09.2020 · 30 Server verschlüsselt · 13 Tage von der\nNotfallversorgung abgemeldet · Einfallstor: Citrix-Lücke von Anfang 2020",
        fc=PINK, ec=RED, fs=8.8, color=RED)
    box(ax, 4.5, 3.9, 4.0, 2.1, "Uniklinik\nKrisenstab und IT", fc=ICE, ec=NAVY, fs=10.5, color=NAVY)
    sats = [(0.3, 5.3, "BSI", "Meldung nach BSIG,\nmobiles Einsatzteam", CREAM, ORANGE),
            (8.7, 5.3, "Polizei / ZAC Köln", "Ermittlungen, Kontakt\nzu den Tätern", LILAC, NAVY),
            (0.3, 2.3, "Rettungsdienst", "Umleitung in andere\nKliniken", MINT, GREEN),
            (8.7, 2.3, "Land NRW", "Berichte an den\nLandtag", MINT, GREEN)]
    for x, y, t, s, fc, ec in sats:
        box(ax, x, y, 4.0, 2.0, "", fc=fc, ec=ec)
        text(ax, x + 2.0, y + 1.45, t, 10, ec, bold=True)
        text(ax, x + 2.0, y + 0.6, s, 8.6, "#222222")
    box(ax, 0.3, 0.2, 12.4, 1.65, "Erpresserschreiben an die Universität gerichtet: Nach Hinweis der Polizei\ngaben die Täter den Schlüssel heraus",
        fc="#f8f8f8", ec=LGREY, fs=9.4, color="#222222", bold=False)
    save(fig, "ukd-2020-akteure.png")


# --------------------------------------------------------------------------------------
def hskl_2023():
    """Hochschule Kaiserslautern 2023: vom Vorfall zur landesweiten Rollenstruktur."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    steps = [("8.6.2023", "Angriff auf die IT – früh abgeschaltet,\nKrisenstab, LKA informiert", PINK, RED),
             ("Juni", "Austausch mit BSI, DFN-CERT, VCRP, ZIT\nund den Rechenzentren Mainz und KL", CREAM, ORANGE),
             ("Juli", "erbeutete Daten im Darknet\nveröffentlicht und geprüft", PINK, RED),
             ("Jan. 2025", "Landesstrategie aller 12 Hochschulen\nmit dem Wissenschaftsministerium", ICE, NAVY),
             ("Struktur", "ISB an jeder Hochschule, direkt beim\nPräsidium · Servicezentrum RARP-SIS", MINT, GREEN)]
    for i, (d, s, fc, ec) in enumerate(steps):
        y0 = 8.0 - i * 1.85
        text(ax, 1.3, y0 + 0.6, d, 9.5, ec, bold=True)
        box(ax, 2.6, y0, 7.3, 1.25, s, fc=fc, ec=ec, fs=9, bold=False)
        if i < len(steps) - 1:
            arrow(ax, (6.25, y0 - 0.02), (6.25, y0 - 0.55), color=GREY, lw=1.8, ms=13)
    box(ax, 10.2, 1.8, 2.75, 6.4, "", fc="#f8f8f8", ec=NAVY, lw=1.8)
    text(ax, 11.57, 7.6, "Muster", 12, NAVY, bold=True)
    text(ax, 11.57, 5.5, "aus dem\nVorfall\nwird eine\nRolle", 10.5, "#222222", bold=True)
    text(ax, 11.57, 3.0, "rund\n5 Mio. €\n2025/26", 10, GREEN, bold=True)
    save(fig, "hskl-2023.png")


# --------------------------------------------------------------------------------------
def meldefristen():
    """Meldefristen nach § 32 BSIG und Art. 33 DSGVO ab Kenntnis des Vorfalls."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "Uhr läuft ab Kenntnis", 13.5, NAVY, bold=True)
    ax.plot([0.6, 12.4], [6.0, 6.0], color="#222222", lw=2)
    ax.plot([0.6, 0.6], [5.7, 6.3], color=RED, lw=3.5)
    text(ax, 0.6, 6.75, "Kenntnis", 10, RED, bold=True)
    pts = [(3.2, "24 h", "Frühwarnung\nan das BSI", ORANGE),
           (6.2, "72 h", "Meldung an das BSI ·\nDSGVO-Meldung\nan die Aufsicht", ORANGE),
           (11.6, "1 Monat", "Abschlussbericht\nan das BSI", NAVY)]
    for x, d, s, c in pts:
        ax.plot([x, x], [5.7, 6.3], color=c, lw=3.5)
        text(ax, x, 6.75, d, 12, c, bold=True)
        text(ax, x, 4.65, s, 9.2, "#222222")
    box(ax, 0.3, 2.0, 6.0, 1.6, "§ 32 BSIG (seit 6.12.2025):\nwichtige und besonders wichtige\nEinrichtungen", fc=CREAM, ec=ORANGE, fs=9, bold=False)
    box(ax, 6.7, 2.0, 6.0, 1.6, "Art. 33 DSGVO: Verletzung des\nSchutzes personenbezogener Daten,\nVerantwortlicher meldet", fc=LILAC, ec=NAVY, fs=9, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.35, "Vorab festlegen: Wer stellt fest, wer entscheidet, wer meldet?",
        fc=ICE, ec=NAVY, fs=10.5)
    save(fig, "meldefristen.png")


# --------------------------------------------------------------------------------------
def mgm_caesars_2023():
    """MGM und Caesars 2023: gleiche Angreifer, zwei Entscheidungen der Leitung."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.0, 12.4, 1.3, "September 2023 · gleiche Angreifergruppe · Einstieg über\nSocial Engineering beim IT-Support",
        fc=ICE, ec=NAVY, fs=10.5)
    cols = [("Caesars", "zahlt – laut Medien\nrund 15 Mio. USD", MINT, GREEN,
             ["Betrieb der Häuser\nund Apps ungestört", "Kundendatenbank\nkopiert", "8-K: Schritte, damit die\nDaten gelöscht werden"]),
            ("MGM Resorts", "zahlt nicht", PINK, RED,
             ["rund 10 Tage Systeme\nabgeschaltet", "rund 100 Mio. USD\nweniger Ergebnis", "Versicherung soll\nden Schaden decken"])]
    for i, (t, s, fc, ec, rows) in enumerate(cols):
        x = 0.3 + i * 6.5
        box(ax, x, 1.75, 5.9, 5.9, "", fc=fc, ec=ec)
        text(ax, x + 2.95, 7.2, t, 12.5, ec, bold=True)
        text(ax, x + 2.95, 6.15, s, 9.2, "#222222", bold=True)
        for j, r in enumerate(rows):
            box(ax, x + 0.35, 4.35 - j * 1.2, 5.2, 1.0, r, fc="white", ec=ec, fs=8.8, bold=False, lw=1.4)
    box(ax, 0.3, 0.1, 12.4, 1.35, "Lösegeld entscheidet die Leitung – vorbereitet, nicht improvisiert",
        fc=CREAM, ec=NAVY, fs=9.8)
    save(fig, "mgm-caesars-2023.png")


if __name__ == "__main__":
    target_2013_zeitleiste()
    mandat_dreieck()
    uber_2016_zeitleiste()
    ciso_haftung()
    cert_landschaft()
    ukd_2020_akteure()
    hskl_2023()
    meldefristen()
    mgm_caesars_2023()
    print("Diagramme erzeugt in", OUT)
