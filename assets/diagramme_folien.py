"""Zusätzliche Folien-Diagramme (erklärende Grafiken, keine Messwerte).

Aufruf im Projektordner:  python assets/diagramme_folien.py
Nutzt Farben und Hilfsfunktionen aus abbildungen.py.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle, Wedge  # noqa: E402

from abbildungen import BLUE, GREY, LIGHT, NAVY, RED, arrow, box, save  # noqa: E402

GREEN = "#2e7d4f"
ORANGE = "#d9822b"


def canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(0, xl)
    ax.set_ylim(0, yl)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def label(ax, x, y, text, size=12, color=NAVY, bold=False, ha="center", va="center"):
    ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color, fontweight="bold" if bold else "normal")


# ---------------------------------------------------------------- Termin 1/3
def vier_prinzipien():
    fig, ax = canvas(8, 6.4, 10, 8)
    tiles = [(0.2, 4.1, "Redundanz", "keine einzelnen\nBruchpunkte"),
             (5.1, 4.1, "Diversität", "keine gemeinsamen\nFehlerquellen"),
             (0.2, 0.1, "Wiederherstell-\nbarkeit", "geübte, getestete\nRückkehr"),
             (5.1, 0.1, "Adaptivität", "dynamisch statt\nstatisch")]
    for x, y, t, s in tiles:
        box(ax, x, y, 4.7, 3.7, "", fc="white")
        label(ax, x + 2.35, y + 1.05, t, 14, bold=True)
        label(ax, x + 2.35, y + 0.35, s, 9.5, GREY)
    # Redundanz: zwei parallele Pfade, einer unterbrochen
    x0, y0 = 0.9, 6.6
    ax.add_patch(Circle((x0, y0 - 0.5), 0.28, color=NAVY))
    ax.add_patch(Circle((x0 + 3.3, y0 - 0.5), 0.28, color=NAVY))
    ax.plot([x0 + 0.3, x0 + 3.0], [y0 - 0.1, y0 - 0.1], color=GREEN, lw=4)
    ax.plot([x0 + 0.3, x0 + 1.4], [y0 - 0.9, y0 - 0.9], color=RED, lw=4)
    ax.plot([x0 + 1.9, x0 + 3.0], [y0 - 0.9, y0 - 0.9], color=RED, lw=4)
    label(ax, x0 + 1.65, y0 - 0.9, "✕", 16, RED, bold=True)
    # Diversität: verschiedene Formen
    ax.add_patch(Circle((6.2, 6.1), 0.45, color=BLUE))
    ax.add_patch(Rectangle((7.1, 5.65), 0.9, 0.9, color=ORANGE))
    ax.add_patch(plt.Polygon([[8.5, 5.65], [9.5, 5.65], [9.0, 6.55]], color=GREEN))
    # Wiederherstellbarkeit: Kreispfeil
    ax.add_patch(Wedge((2.55, 2.4), 0.9, 40, 330, width=0.22, color=BLUE))
    ax.add_patch(plt.Polygon([[3.2, 2.85], [3.55, 3.35], [3.75, 2.7]], color=BLUE))
    # Adaptivität: wachsende Balken
    for i, hgt in enumerate([0.5, 0.9, 1.4, 1.1, 0.7]):
        ax.add_patch(Rectangle((5.9 + i * 0.65, 1.55), 0.45, hgt, color=BLUE if i != 2 else ORANGE))
    save(fig, "vier-prinzipien.png")


def redundanz_isolation():
    fig, ax = canvas(8, 5.2, 10, 6.5)
    for x0, title, ok in [(0.2, "Redundanz ohne Isolation", False), (5.2, "Redundanz mit Isolation", True)]:
        label(ax, x0 + 2.3, 6.1, title, 12.5, NAVY, bold=True)
        if not ok:
            ax.add_patch(FancyBboxPatch((x0, 0.9), 4.6, 4.5, boxstyle="round,pad=0.02", fc="#fbe9e9", ec=RED, lw=2))
            label(ax, x0 + 2.3, 5.05, "ein Brandabschnitt", 10, RED)
            box(ax, x0 + 0.4, 2.3, 1.7, 1.6, "USV A")
            box(ax, x0 + 2.5, 2.3, 1.7, 1.6, "USV B")
            label(ax, x0 + 2.3, 0.45, "ein Brand → beide weg", 10, RED)
        else:
            for dx, n in [(0, "A"), (2.45, "B")]:
                ax.add_patch(FancyBboxPatch((x0 + dx, 0.9), 2.15, 4.5, boxstyle="round,pad=0.02", fc="#e7f3ec", ec=GREEN, lw=2))
                label(ax, x0 + dx + 1.07, 5.05, f"Abschnitt {n}", 10, GREEN)
                box(ax, x0 + dx + 0.2, 2.3, 1.75, 1.6, f"USV {n}")
            label(ax, x0 + 2.3, 0.45, "ein Brand → eine bleibt", 10, GREEN)
    save(fig, "redundanz-isolation.png")


def hybrid_spof():
    fig, ax = canvas(8, 6, 10, 7.5)
    ax.add_patch(FancyBboxPatch((0.1, 0.3), 3.6, 6.2, boxstyle="round,pad=0.05", fc=LIGHT, ec=NAVY, lw=1.5))
    ax.add_patch(FancyBboxPatch((6.3, 0.3), 3.6, 6.2, boxstyle="round,pad=0.05", fc="#eef6fb", ec=BLUE, lw=1.5))
    label(ax, 1.9, 6.95, "On-Prem", 13, NAVY, bold=True)
    label(ax, 8.1, 6.95, "Cloud", 13, BLUE, bold=True)
    for i, t in enumerate(["ERP", "Fileserver", "Produktion"]):
        box(ax, 0.5, 4.7 - i * 1.7, 2.8, 1.1, t, fc="white", fs=11)
    for i, t in enumerate(["Analytics", "SaaS-Apps", "Backups"]):
        box(ax, 6.7, 4.7 - i * 1.7, 2.8, 1.1, t, fc="white", ec=BLUE, fs=11)
    for i, t in enumerate(["IdP /\nAD", "VPN /\nSD-WAN", "CI/CD"]):
        y = 4.7 - i * 1.7
        ax.add_patch(Circle((5, y + 0.55), 0.8, fc="#fbe9e9", ec=RED, lw=2.5))
        label(ax, 5, y + 0.55, t, 9, RED, bold=True)
        arrow(ax, (3.3, y + 0.55), (4.2, y + 0.55), GREY, style="-")
        arrow(ax, (5.8, y + 0.55), (6.7, y + 0.55), GREY, style="-")
    label(ax, 5, -0.3, "zentrale Kopplungspunkte = Hybrid-SPOFs", 10.5, RED)
    ax.set_ylim(-0.7, 7.5)
    save(fig, "hybrid-spof.png")


# ---------------------------------------------------------------- Termin 4
def threat_mapping():
    threats = ["Ransomware", "DDoS", "Cloud-Ausfall", "Identity-Ausfall", "Human Failure", "Supply Chain"]
    prin = ["Redundanz", "Diversität", "Wiederherstell-\nbarkeit", "Adaptivität"]
    links = [(0, 2), (0, 1), (1, 3), (2, 0), (3, 1), (3, 2), (4, 2), (5, 1)]
    fig, ax = canvas(8.5, 6, 10, 7)
    ty = [6.2 - i * 1.1 for i in range(6)]
    py = [5.6 - i * 1.5 for i in range(4)]
    cols = [RED, BLUE, NAVY, GREEN]
    for (t, p) in links:
        ax.plot([3.4, 6.6], [ty[t] + 0.3, py[p] + 0.35], color=cols[p], lw=2.5, alpha=0.75)
    for i, t in enumerate(threats):
        box(ax, 0.2, ty[i], 3.2, 0.6, t, fc="white", fs=11)
    for i, p in enumerate(prin):
        box(ax, 6.6, py[i], 3.2, 0.7 if "\n" not in p else 0.9, p, fc=LIGHT, ec=cols[i], fs=11, color=cols[i])
    label(ax, 1.8, 6.95, "Bedrohung", 11, GREY)
    label(ax, 8.2, 6.95, "Resilienzprinzip", 11, GREY)
    save(fig, "threat-mapping.png")


# ---------------------------------------------------------------- Termin 5
def cccc():
    fig, ax = canvas(7, 7, 8, 8)
    items = [("Clear", "eindeutig", NAVY), ("Concise", "kurz", BLUE), ("Confirmed", "Readback", GREEN), ("Coordinated", "ein Lagebild", ORANGE)]
    pos = [(0.2, 4.1), (4.1, 4.1), (0.2, 0.2), (4.1, 0.2)]
    for (t, s, c), (x, y) in zip(items, pos):
        ax.add_patch(FancyBboxPatch((x, y), 3.7, 3.7, boxstyle="round,pad=0.02,rounding_size=0.3", fc=c, ec="white", lw=3))
        label(ax, x + 1.85, y + 2.3, "C", 54, "white", bold=True)
        label(ax, x + 1.85, y + 1.05, t, 15, "white", bold=True)
        label(ax, x + 1.85, y + 0.45, s, 11, "white")
    save(fig, "cccc.png")


def incident_command():
    fig, ax = canvas(8, 6, 10, 7.4)
    box(ax, 3.2, 5.5, 3.6, 1.2, "Command")
    label(ax, 5, 7.05, "priorisiert · entscheidet auf Zeit", 10, GREY)
    box(ax, 0.3, 1.9, 4.2, 1.3, "Operations", fc="white")
    label(ax, 2.4, 1.5, "handelt: eindämmen, wiederherstellen", 9.5, GREY)
    box(ax, 5.5, 1.9, 4.2, 1.3, "Support", fc="white")
    label(ax, 7.6, 1.5, "dokumentiert · kommuniziert", 9.5, GREY)
    arrow(ax, (4.4, 5.5), (2.6, 3.2))
    arrow(ax, (5.6, 5.5), (7.4, 3.2))
    label(ax, 5, 0.5, "Unity of Command · Span of Control 5–7 · Delegation", 10, RED)
    save(fig, "incident-command.png")


# ---------------------------------------------------------------- Termin 8
def zero_trust_vergleich():
    fig, ax = canvas(9, 4.8, 12, 6.2)
    for x0, title in [(0.2, "Perimeter"), (6.2, "Zero Trust")]:
        label(ax, x0 + 2.8, 5.85, title, 14, NAVY, bold=True)
    # Perimeter: eine Mauer, innen alles grün
    ax.add_patch(FancyBboxPatch((0.4, 0.6), 5.2, 4.6, boxstyle="round,pad=0.02", fc="#e7f3ec", ec=NAVY, lw=5))
    for i in range(3):
        for j in range(2):
            ax.add_patch(Circle((1.4 + i * 1.6, 1.8 + j * 2.0), 0.42, fc=GREEN))
    ax.plot([1.4, 3.0, 4.6], [1.8, 3.8, 1.8], color=RED, lw=2, ls="--")
    label(ax, 3.0, 0.2, "innen = vertraut → laterale Bewegung", 10, RED)
    # Zero Trust: jede Ressource eigener Prüfpunkt
    for i in range(3):
        for j in range(2):
            cx, cy = 7.4 + i * 1.6, 1.8 + j * 2.0
            ax.add_patch(Circle((cx, cy), 0.62, fc="white", ec=BLUE, lw=3))
            ax.add_patch(Circle((cx, cy), 0.36, fc=NAVY))
    label(ax, 9.0, 0.2, "jeder Zugriff geprüft → Schaden bleibt lokal", 10, GREEN)
    save(fig, "zero-trust-vergleich.png")


def microseg_zellen():
    fig, ax = canvas(9, 4.8, 12, 6.2)
    label(ax, 3.0, 5.85, "flaches Netz", 14, NAVY, bold=True)
    label(ax, 9.0, 5.85, "microsegmentiert", 14, NAVY, bold=True)
    import itertools
    for i, j in itertools.product(range(4), range(3)):
        x, y = 0.9 + i * 1.4, 1.2 + j * 1.5
        ax.add_patch(Circle((x, y), 0.4, fc=RED))
    ax.add_patch(FancyBboxPatch((0.3, 0.5), 5.4, 4.8, boxstyle="round,pad=0.02", fc="none", ec=NAVY, lw=2))
    label(ax, 3.0, 0.1, "ein Einbruch → alles betroffen", 10, RED)
    for i, j in itertools.product(range(4), range(3)):
        x, y = 6.9 + i * 1.4, 1.2 + j * 1.5
        ax.add_patch(FancyBboxPatch((x - 0.6, y - 0.6), 1.2, 1.2, boxstyle="round,pad=0.01", fc="none", ec=BLUE, lw=1.8))
        ax.add_patch(Circle((x, y), 0.4, fc=RED if (i, j) == (1, 1) else GREEN))
    label(ax, 9.0, 0.1, "Angriff bleibt in seiner Zelle", 10, GREEN)
    save(fig, "microseg-zellen.png")


def shared_responsibility():
    fig, ax = canvas(7, 6.2, 9, 8)
    rows = [("Daten & Klassifizierung", "k"), ("Identitäten & IAM", "k"), ("Konfiguration & Netzregeln", "k"),
            ("Backups & Restore-Tests", "k"), ("Plattformdienste", "a"), ("Rechenzentrum, Hardware, Netz", "a")]
    for i, (t, who) in enumerate(rows):
        y = 6.6 - i * 1.1
        c = BLUE if who == "k" else GREY
        ax.add_patch(FancyBboxPatch((1.9, y), 6.9, 0.9, boxstyle="round,pad=0.02", fc=c, ec="white", lw=2))
        label(ax, 5.35, y + 0.45, t, 11.5, "white", bold=True)
    ax.add_patch(Rectangle((0.2, 3.3), 0.25, 4.2, color=BLUE))
    ax.text(0.95, 5.4, "Kunde", rotation=90, ha="center", va="center", fontsize=13, color=BLUE, fontweight="bold")
    ax.add_patch(Rectangle((0.2, 1.1), 0.25, 2.0, color=GREY))
    ax.text(0.95, 2.1, "Anbieter", rotation=90, ha="center", va="center", fontsize=13, color=GREY, fontweight="bold")
    label(ax, 4.5, 0.45, "Cloud-Anbieter ≠ Datensicherung", 11, RED, bold=True)
    save(fig, "shared-responsibility.png")


def integration_schichten():
    fig, ax = canvas(8, 5.8, 10, 7.2)
    layers = [("Zero Trust", "Schadensbegrenzung", NAVY), ("Microsegmentation", "Bewegungskontrolle", BLUE),
              ("Cloud Resilience", "skalierbare Wiederherstellung", GREEN), ("Network Design", "stabile Grundlage", GREY)]
    for i, (t, s, c) in enumerate(layers):
        y = 5.4 - i * 1.55
        inset = i * 0.0
        ax.add_patch(FancyBboxPatch((0.3 + inset, y), 9.4 - 2 * inset, 1.3, boxstyle="round,pad=0.02", fc=c, ec="white", lw=2))
        label(ax, 3.2, y + 0.65, t, 14, "white", bold=True)
        label(ax, 7.4, y + 0.65, s, 11.5, "white")
    label(ax, 5, 0.25, "Umsetzung von unten nach oben", 10.5, RED)
    save(fig, "integration-schichten.png")


# ---------------------------------------------------------------- Termin 9
def wallet_dos():
    fig, ax = canvas(9.5, 4.6, 12.8, 6)
    for i in range(5):
        box(ax, 0.2, 0.6 + i * 1.0, 1.9, 0.75, "Anfrage", fc="#fbe9e9", ec=RED, fs=9, color=RED)
        arrow(ax, (2.1, 0.95 + i * 1.0), (4.0, 2.9), RED)
    box(ax, 4.0, 2.1, 2.6, 1.6, "KI-API", fc=LIGHT)
    arrow(ax, (6.6, 2.9), (8.0, 2.9), NAVY)
    # Guthaben-Balken leert sich
    ax.add_patch(Rectangle((8.2, 0.8), 1.2, 4.2, fc="white", ec=NAVY, lw=2))
    ax.add_patch(Rectangle((8.2, 0.8), 1.2, 0.7, fc=RED))
    label(ax, 8.8, 5.4, "Guthaben", 11, NAVY, bold=True)
    label(ax, 11.4, 4.1, "Gegenmaßnahmen", 11, GREEN, bold=True)
    label(ax, 11.4, 3.4, "Schlüssel\nje Mandant", 9.5, GREEN)
    label(ax, 11.4, 2.4, "Rate Limits\n& Monitoring", 9.5, GREEN)
    label(ax, 11.4, 1.4, "Budget\nje Mandant", 9.5, GREEN)
    save(fig, "wallet-dos.png")


# ---------------------------------------------------------------- Termin 10
def harvest_now():
    fig, ax = canvas(9.5, 3.6, 12, 4.4)
    ax.annotate("", xy=(11.7, 2), xytext=(0.3, 2), arrowprops=dict(arrowstyle="-|>", color=NAVY, lw=3))
    pts = [(1.2, "heute", "verschlüsselte Daten\nwerden abgegriffen", BLUE),
           (5.5, "Jahre", "Daten liegen\ngespeichert", GREY),
           (9.8, "Q-Day", "Quantencomputer\nentschlüsselt", RED)]
    for x, t, s, c in pts:
        ax.add_patch(Circle((x, 2), 0.32, fc=c, ec="white", lw=2, zorder=3))
        label(ax, x, 2.75, t, 13, c, bold=True)
        label(ax, x, 1.05, s, 10, GREY)
    label(ax, 6, 4.1, "Harvest now, decrypt later", 14, NAVY, bold=True)
    save(fig, "harvest-now.png")


def crypto_agility():
    fig, ax = canvas(8, 5.6, 10, 7)
    box(ax, 0.4, 3.7, 9.2, 2.8, "", fc=LIGHT)
    label(ax, 5, 6.05, "Anwendung / Vertrauenskette", 12.5, NAVY, bold=True)
    box(ax, 3.6, 4.0, 2.8, 1.5, "Krypto-\nSchnittstelle", fc="white", fs=11)
    box(ax, 0.6, 0.6, 2.6, 1.3, "RSA / ECC", fc="#fbe9e9", ec=RED, color=RED, fs=11)
    box(ax, 6.8, 0.6, 2.6, 1.3, "Post-Quantum", fc="#e7f3ec", ec=GREEN, color=GREEN, fs=11)
    arrow(ax, (4.2, 4.0), (2.2, 1.9), GREY, style="-")
    label(ax, 2.2, 2.9, "✕", 20, RED, bold=True)
    arrow(ax, (5.8, 4.0), (7.9, 1.9), GREEN)
    label(ax, 5, 1.25, "austauschen ·\nSchlüssel erneuern", 10, GREY)
    save(fig, "crypto-agility.png")


FUNKTIONEN = [vier_prinzipien, redundanz_isolation, hybrid_spof, threat_mapping, cccc, incident_command,
              zero_trust_vergleich, microseg_zellen, shared_responsibility, integration_schichten,
              wallet_dos, harvest_now, crypto_agility]

if __name__ == "__main__":
    for f in FUNKTIONEN:
        f()
    print(len(FUNKTIONEN), "Folien-Diagramme erzeugt")
