"""Diagramme für den Foliensatz Termin 7 „Backup, Disaster Recovery, Notfalltests“.

Aufruf im Projektordner:  python assets/diagramme_termin07.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-07/assets/.
Gestaltung wie die Diagramme in Termin 1–6 (Inter, Navy-Rahmen, helle Flächen).
Alle Darstellungen sind schematisch; Zahlen stammen aus den in quellen.qmd genannten Quellen.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Präsentationen" / "Termin-07" / "assets"

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
def cloudnordic_2023():
    """CloudNordic/AzeroCloud 2023: Produktion und beide Backup-Ebenen im selben Netz."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "18.08.2023 · Ransomware bei CloudNordic / AzeroCloud",
        fc=PINK, ec=RED, fs=10, color=RED)
    box(ax, 0.3, 2.2, 12.4, 5.4, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 6.5, 7.15, "ein internes Netz – während eines Rechenzentrumsumzugs", 9.6, GREY, bold=True)
    items = [(0.7, "Kundenserver", "alle Platten\nverschlüsselt"),
             (4.75, "Primäres\nBackup", "verschlüsselt"),
             (8.8, "Sekundäres\nBackup", "verschlüsselt")]
    for x, t, s in items:
        box(ax, x, 3.9, 3.5, 2.6, "", fc=PINK, ec=RED)
        text(ax, x + 1.75, 5.65, t, 10.5, RED, bold=True)
        text(ax, x + 1.75, 4.45, s, 9, "#222222")
        cross(ax, x, 3.9, 3.5, 2.6)
    box(ax, 3.0, 2.45, 7.0, 1.0, "zentrale Verwaltung: Zugriff auf alles", fc=CREAM, ec=ORANGE, fs=9, bold=False)
    for x in (2.45, 6.5, 10.55):
        arrow(ax, (6.5, 3.45), (x, 3.9), color=ORANGE, lw=1.6, ms=11)
    box(ax, 0.3, 0.2, 12.4, 1.55, "Kein Lösegeld gezahlt · die meisten Kunden verlieren alle Daten.\nEin Backup im selben Netz ist nur eine weitere Kopie",
        fc=ICE, ec=NAVY, fs=9)
    save(fig, "cloudnordic-2023.png")


# --------------------------------------------------------------------------------------
def unisuper_2024():
    """UniSuper / Google Cloud 2024: zwei Standorte gelöscht, unabhängige Kopie hilft."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "Mai 2024 · Google Cloud löscht UniSupers Private Cloud",
        fc=PINK, ec=RED, fs=10, color=RED)
    box(ax, 0.3, 3.5, 7.6, 4.1, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 4.1, 7.15, "ein Vertrag, eine Steuerungsebene", 9.6, GREY, bold=True)
    for x, t in [(0.7, "Standort 1"), (4.3, "Standort 2")]:
        box(ax, x, 4.0, 3.2, 2.5, "", fc=PINK, ec=RED)
        text(ax, x + 1.6, 5.6, t, 10.5, RED, bold=True)
        text(ax, x + 1.6, 4.6, "gelöscht", 9.2, "#222222")
        cross(ax, x, 4.0, 3.2, 2.5)
    box(ax, 8.6, 3.5, 4.1, 4.1, "", fc=MINT, ec=GREEN)
    text(ax, 10.65, 6.75, "Backup bei\nanderem Anbieter", 10.5, GREEN, bold=True)
    text(ax, 10.65, 5.2, "nicht betroffen", 9.2, "#222222", bold=True)
    text(ax, 10.65, 4.2, "Grundlage der\nWiederherstellung", 9, "#222222")
    arrow(ax, (8.6, 4.4), (7.5, 4.4), color=GREEN, lw=2.4, ms=16)
    box(ax, 0.3, 1.75, 12.4, 1.3, "Ursache: leerer Parameter bei der Einrichtung 2023 → Laufzeit\nein Jahr → automatische Löschung, ohne Warnung an den Kunden",
        fc=CREAM, ec=ORANGE, fs=8.4, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.2, "Georedundanz schützt vor Standortausfall –\nnicht vor Löschung über die Steuerungsebene",
        fc=ICE, ec=NAVY, fs=9)
    save(fig, "unisuper-2024.png")


# --------------------------------------------------------------------------------------
def kyoto_2021():
    """Universität Kyoto 2021: Das Backup-Programm löscht die Daten, die es sichern soll."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Wenn das Backup-System selbst löscht", 13.5, NAVY, bold=True)
    steps = [("Update", "Hersteller ändert ein\nSkript im Backup-\nProgramm – während\nes läuft", CREAM, ORANGE),
             ("Fehler", "Löschbefehl für alte\nLogdateien trifft\ndas Dateisystem\n/LARGE0", PINK, RED),
             ("14.–16.12.2021", "rund 34 Mio. Dateien\nvon 14 Gruppen\ngelöscht – rund\n77 TB", PINK, RED)]
    for i, (t, s, fc, ec) in enumerate(steps):
        x = 0.3 + i * 4.25
        box(ax, x, 4.6, 3.9, 3.7, "", fc=fc, ec=ec)
        text(ax, x + 1.95, 7.7, t, 10.5, ec, bold=True)
        text(ax, x + 1.95, 6.0, s, 9, "#222222")
        if i < 2:
            arrow(ax, (x + 3.9, 6.45), (x + 4.25, 6.45), color=GREY, lw=2, ms=13)
    box(ax, 0.3, 2.3, 6.0, 1.85, "10 Gruppen:\naus dem Backup\nwiederhergestellt", fc=MINT, ec=GREEN, fs=9.4, color=GREEN)
    box(ax, 6.7, 2.3, 6.0, 1.85, "4 Gruppen:\nrund 28 TB ohne Backup –\nendgültig verloren", fc=PINK, ec=RED, fs=9.4, color=RED)
    box(ax, 0.3, 0.2, 12.4, 1.65, "Ein Backup-System hat Löschrechte auf Produktivdaten.\nÄnderungen daran gehören ins Change-Management",
        fc=ICE, ec=NAVY, fs=9)
    save(fig, "kyoto-2021.png")


# --------------------------------------------------------------------------------------
def rto_bestandteile():
    """Die RTO umfasst mehr als die reine Rückspielzeit."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Die RTO ist mehr als die Restore-Zeit", 13.5, NAVY, bold=True)
    segs = [("Erkennen", 2.0, ICE, NAVY), ("Entscheiden,\nfreigeben", 2.5, CREAM, ORANGE),
            ("Bereinigen,\nInfrastruktur", 2.7, PINK, RED), ("Daten zurück-\nspielen", 2.7, MINT, GREEN),
            ("Prüfen,\nfreigeben", 2.2, LILAC, NAVY)]
    x = 0.45
    for t, w, fc, ec in segs:
        box(ax, x, 5.9, w, 1.9, t, fc=fc, ec=ec, fs=8.2, color="#222222")
        x += w
    ax.annotate("", xy=(12.55, 5.3), xytext=(0.45, 5.3), arrowprops=dict(arrowstyle="<|-|>", color=NAVY, lw=2.2))
    text(ax, 6.5, 4.75, "RTO – vom Ausfall bis zum freigegebenen Betrieb", 10.5, NAVY, bold=True)
    ax.annotate("", xy=(10.35, 8.25), xytext=(7.65, 8.25), arrowprops=dict(arrowstyle="<|-|>", color=GREEN, lw=2))
    text(ax, 9.0, 8.55, "nur das misst der Restore-Test", 8.4, GREEN, bold=True)
    box(ax, 0.3, 2.3, 6.0, 1.7, "Nach Ransomware: Ist die\nKopie sauber? Seit wann\nsind die Angreifer im Netz?", fc=PINK, ec=RED, fs=9, bold=False)
    box(ax, 6.7, 2.3, 6.0, 1.7, "Wohin zurückspielen?\nServer, Netz und Identitäten\nmüssen zuerst stehen", fc=CREAM, ec=ORANGE, fs=9, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.65, "Eine RTO ist erst belegt, wenn die ganze Kette\ngeübt und gemessen wurde",
        fc=ICE, ec=NAVY, fs=9.6)
    save(fig, "rto-bestandteile.png")


# --------------------------------------------------------------------------------------
def wiederanlauf_reihenfolge():
    """Wiederherstellungsreihenfolge: Abhängigkeiten von unten nach oben."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Wiederanlauf folgt den Abhängigkeiten", 13.5, NAVY, bold=True)
    layers = [("1", "Strom, Netz, Storage, Virtualisierung", ICE, NAVY),
              ("2", "Identität und Namensdienste: AD, DNS, IAM, PKI", CREAM, ORANGE),
              ("3", "Datenbanken und Fileservices", MINT, GREEN),
              ("4", "Anwendungen: E-Mail, Lernplattform, Prüfungsverwaltung", LILAC, NAVY),
              ("5", "Öffnung für Nutzer – mit neuen Zugangsdaten", "#f8f8f8", LGREY)]
    for i, (n, t, fc, ec) in enumerate(layers):
        y = 1.95 + i * 1.32
        box(ax, 2.0, y, 10.7, 1.08, t, fc=fc, ec=ec, fs=9.2, color="#222222")
        box(ax, 0.3, y, 1.3, 1.08, n, fc="white", ec=ec, fs=12, color=ec)
    arrow(ax, (1.8, 2.0), (1.8, 8.3), color=GREY, lw=2, ms=14)
    box(ax, 0.3, 0.2, 12.4, 1.35, "Auch das Backup-System braucht Identitäten, Netz und Schlüssel –\naußerhalb der Produktion",
        fc=PINK, ec=RED, fs=8.8, color=RED)
    save(fig, "wiederanlauf-reihenfolge.png")


# --------------------------------------------------------------------------------------
def giessen_2019_zeitleiste():
    """Universität Gießen 2019/20: Wiederanlauf in Etappen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.2, "#JLUoffline: drei Monate, bis alle Netze wieder laufen", 12, RED, bold=True)
    marks = [(0.9, "8.12.2019", "Angriff erkannt,\nalle Server\nheruntergefahren", RED, True),
             (3.2, "12.12.", "38.000 Passwörter\nzurückgesetzt,\nAusgabe persönlich", ORANGE, False),
             (5.5, "20.12.", "E-Mail\nläuft wieder", GREEN, True),
             (7.8, "6.1.2020", "Website und\nLernplattform\nwieder online", GREEN, False),
             (10.0, "17.2.", "Verwaltungs-\nnetz wieder\nonline", GREEN, True),
             (12.1, "6.3.", "alle großen\nTeilnetze\nonline", NAVY, False)]
    timeline(ax, 5.3, marks)
    box(ax, 0.3, 0.2, 12.4, 1.6, "Daten durch frühes Herunterfahren geschützt – Zeit kostete der\nWiederaufbau: Identitäten, Endgeräte, Netze · bis Mai 2020 rund 1,7 Mio. €",
        fc=CREAM, ec=NAVY, fs=8.4)
    save(fig, "giessen-2019-zeitleiste.png")


# --------------------------------------------------------------------------------------
def british_library_2023():
    """British Library 2023: Daten gesichert, aber keine Infrastruktur zum Zurückspielen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "28.10.2023 · Ransomware · rund 600 GB kopiert · kein Lösegeld",
        fc=PINK, ec=RED, fs=9.4, color=RED)
    box(ax, 0.3, 4.6, 5.9, 3.0, "", fc=MINT, ec=GREEN)
    text(ax, 3.25, 7.0, "Daten", 12, GREEN, bold=True)
    text(ax, 3.25, 5.7, "Sicherungskopien der\ndigitalen Sammlungen\nvorhanden", 9.2, "#222222")
    box(ax, 6.8, 4.6, 5.9, 3.0, "", fc=PINK, ec=RED)
    text(ax, 9.75, 7.0, "Infrastruktur", 12, RED, bold=True)
    text(ax, 9.75, 5.7, "Server zerstört · Altsysteme\nnicht wiederherstellbar:\nveraltet, ohne Support", 9.2, "#222222")
    text(ax, 6.5, 6.1, "≠", 20, GREY, bold=True)
    steps = [("15.1.2024", "Katalog wieder\ndurchsuchbar", ICE, NAVY),
             ("6 Monate", "Übergangs-\nlösungen", CREAM, ORANGE),
             ("18 Monate", "neue Infra-\nstruktur", CREAM, ORANGE)]
    for i, (d, s, fc, ec) in enumerate(steps):
        x = 0.3 + i * 4.25
        box(ax, x, 2.2, 3.9, 1.95, "", fc=fc, ec=ec)
        text(ax, x + 1.95, 3.6, d, 10.5, ec, bold=True)
        text(ax, x + 1.95, 2.75, s, 8.8, "#222222")
    box(ax, 0.3, 0.2, 12.4, 1.55, "Ein Backup braucht ein Ziel: ohne lauffähige Umgebung kein Restore",
        fc=ICE, ec=NAVY, fs=10)
    save(fig, "british-library-2023.png")


# --------------------------------------------------------------------------------------
def delta_2016():
    """Delta Air Lines 2016: Umschaltung auf Reservestrom mit unentdeckter Lücke."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "8.8.2016 · Stromausfall im Rechenzentrum von Delta Air Lines",
        fc=PINK, ec=RED, fs=9.4, color=RED)
    box(ax, 0.3, 4.3, 7.6, 3.3, "", fc=MINT, ec=GREEN)
    text(ax, 4.1, 6.95, "rund 6.700 Server", 12, GREEN, bold=True)
    text(ax, 4.1, 5.5, "an beide Stromwege\nangeschlossen –\nlaufen wieder an", 9.4, "#222222")
    box(ax, 8.3, 4.3, 4.4, 3.3, "", fc=PINK, ec=RED)
    text(ax, 10.5, 6.95, "rund 300 Server", 12, RED, bold=True)
    text(ax, 10.5, 5.5, "nicht an den\nReservestrom\nangeschlossen", 9.4, "#222222")
    cross(ax, 8.3, 4.3, 4.4, 3.3)
    box(ax, 0.3, 2.2, 12.4, 1.65, "Folge: Die 300 Server antworten nicht – das Gesamtsystem fällt aus.\nRund 2.300 Flüge gestrichen, rund 100 Mio. USD weniger Umsatz",
        fc=CREAM, ec=ORANGE, fs=9, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.55, "Redundanz, die nie unter Last umgeschaltet wurde,\nist eine Annahme",
        fc=ICE, ec=NAVY, fs=9.8)
    save(fig, "delta-2016.png")


# --------------------------------------------------------------------------------------
def backup_isolation():
    """Zero-Trust-Backup: Was das Backup von der Produktion trennen muss."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Was das Backup von der Produktion trennt", 13.5, NAVY, bold=True)
    box(ax, 0.3, 2.3, 4.6, 6.2, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 2.6, 7.95, "Produktion", 11.5, GREY, bold=True)
    for i, t in enumerate(["Server und\nAnwendungen", "Verzeichnisdienst\n(AD)", "Administratoren"]):
        box(ax, 0.7, 6.05 - i * 1.65, 3.8, 1.3, t, fc="white", ec=LGREY, fs=9, bold=False, lw=1.4)
    box(ax, 8.1, 2.3, 4.6, 6.2, "", fc=MINT, ec=GREEN)
    text(ax, 10.4, 7.95, "Backup-Umgebung", 11.5, GREEN, bold=True)
    for i, t in enumerate(["eigene Konten,\nMFA, Vier-Augen", "eigenes\nNetzsegment", "unveränderbare\nKopie / Air-Gap"]):
        box(ax, 8.5, 6.05 - i * 1.65, 3.8, 1.3, t, fc="white", ec=GREEN, fs=9, bold=False, lw=1.4)
    ax.plot([6.5, 6.5], [2.4, 8.4], color=RED, lw=3, linestyle=(0, (4, 3)))
    text(ax, 6.5, 6.6, "kein\ngemeinsames\nKonto", 8.6, RED, bold=True, bbox=dict(fc="white", ec="none", pad=2))
    arrow(ax, (4.9, 3.9), (8.1, 3.9), color=NAVY, lw=2, ms=14)
    text(ax, 6.5, 3.05, "nur Sicherung,\nkein Löschen", 8.4, NAVY, bold=True, bbox=dict(fc="white", ec="none", pad=2))
    box(ax, 0.3, 0.2, 12.4, 1.65, "Prüffrage: Kann ein kompromittierter Domänen-Admin\ndie Backups löschen?",
        fc=ICE, ec=NAVY, fs=9.8)
    save(fig, "backup-isolation.png")


if __name__ == "__main__":
    cloudnordic_2023()
    unisuper_2024()
    kyoto_2021()
    rto_bestandteile()
    wiederanlauf_reihenfolge()
    giessen_2019_zeitleiste()
    british_library_2023()
    delta_2016()
    backup_isolation()
    print("Diagramme erzeugt in", OUT)
