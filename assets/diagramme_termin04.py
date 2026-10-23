"""Diagramme für den Foliensatz Termin 4 „Cyber-Bedrohungen und Resilienzstrategien“.

Aufruf im Projektordner:  python assets/diagramme_termin04.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-04/assets/.
Gestaltung wie die Diagramme in Termin 1 (Inter, Navy-Rahmen, helle Flächen).
Alle Darstellungen sind schematisch; Zahlen stammen aus den in quellen.qmd genannten Quellen.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Präsentationen" / "Termin-04" / "assets"

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




# --------------------------------------------------------------------------------------
def hsm_2025_wiederaufbau():
    """Hochschule Mainz ab 24.11.2025: Wiederaufbau nach Cyberangriff (nur veröffentlichte Angaben)."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    steps = [("24.11.2025", "IT-Systeme heruntergefahren", PINK, RED),
             ("sofort", "Krisenstab, Präsenzlehre läuft weiter,\nInfo über App und soziale Medien", CREAM, ORANGE),
             ("danach", "neue Zugangsdaten für alle", ICE, NAVY),
             ("schrittweise", "alle IT-Geräte eingesammelt, neue Images –\nkritische Bereiche zuerst", ICE, NAVY),
             ("vor Weih-\nnachten", "Zahlungsfähigkeit wiederhergestellt", MINT, GREEN),
             ("Feb. 2026", "eduroam wieder an allen Standorten", MINT, GREEN)]
    for i, (d, s, fc, ec) in enumerate(steps):
        y0 = 8.2 - i * 1.55
        text(ax, 1.3, y0 + 0.55, d, 9.5, ec, bold=True)
        box(ax, 2.85, y0, 7.05, 1.1, s, fc=fc, ec=ec, fs=9, bold=False)
        if i < len(steps) - 1:
            arrow(ax, (6.3, y0 - 0.02), (6.3, y0 - 0.42), color=GREY, lw=1.8, ms=13)
    box(ax, 10.2, 2.4, 2.75, 5.8, "", fc="#f8f8f8", ec=NAVY, lw=1.8)
    text(ax, 11.57, 7.5, "Muster", 12, NAVY, bold=True)
    text(ax, 11.57, 5.5, "neu\naufbauen\nstatt\nreparieren", 10.5, "#222222", bold=True)
    text(ax, 11.57, 3.3, "Kern-\nfunktionen\nzuerst", 10, GREEN, bold=True)
    save(fig, "hsm-2025-wiederaufbau.png")


# --------------------------------------------------------------------------------------
def bedrohungsklassen():
    """Sechs Bedrohungsklassen und was sie dem System nehmen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    tiles = [("Ransomware", "nimmt Daten\nund Systeme", PINK, RED),
             ("DDoS", "nimmt\nKapazität", CREAM, ORANGE),
             ("RZ-/Provider-\nAusfall", "nimmt die\nUmgebung", ICE, NAVY),
             ("Identity-\nAusfall", "nimmt den\nZugang", LILAC, NAVY),
             ("Human\nFailure", "nimmt die\nKontrolle", ROSE, ORANGE),
             ("Supply\nChain", "nimmt das\nVertrauen", MINT, GREEN)]
    for i, (t, eff, fc, ec) in enumerate(tiles):
        col, row = i % 3, i // 3
        x, y = 0.3 + col * 4.25, 5.3 - row * 3.6
        box(ax, x, y, 3.95, 3.2, "", fc=fc, ec=ec)
        text(ax, x + 1.97, y + 2.25, t, 12, ec, bold=True)
        text(ax, x + 1.97, y + 0.9, eff, 10.5, "#222222")
    text(ax, 6.5, 9.2, "Was geht verloren?", 14, NAVY, bold=True)
    text(ax, 6.5, 0.85, "Der Effekt – nicht die Ursache – bestimmt das Resilienzprinzip", 11.5, NAVY, bold=True)
    save(fig, "bedrohungsklassen.png")


# --------------------------------------------------------------------------------------
def dyn_2016_abhaengigkeit():
    """Dyn 21.10.2016: Mirai-Botnetz trifft den DNS-Anbieter, die Websites selbst sind intakt."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 7.5, 5.2, 1.5, "Mirai-Botnetz\n(Kameras, Router …)", fc=CREAM, ec=ORANGE, fs=11, color=ORANGE)
    for k in range(3):
        arrow(ax, (1.6 + k * 1.3, 7.45), (2.2 + k * 0.6, 5.85), color=ORANGE, lw=1.8, ms=13)
    box(ax, 0.8, 4.3, 4.2, 1.5, "DNS-Anbieter Dyn\nüberlastet", fc=PINK, ec=RED, fs=11.5)
    for k, s in enumerate(["Site A", "Site B", "Site C"]):
        x = 0.1 + k * 1.95
        arrow(ax, (2.9, 4.25), (x + 0.85, 3.15), color=RED, lw=1.6, ms=12)
        box(ax, x, 2.0, 1.75, 1.1, s, fc="white", ec=LGREY, fs=9.5, color=GREY, bold=False)
    text(ax, 2.9, 1.2, "Server intakt – Namen\nnicht auflösbar", 10.5, RED, bold=True)
    ax.plot([6.5, 6.5], [0.3, 9.0], color="#cccccc", ls="--", lw=2)
    text(ax, 9.8, 8.6, "Gegenprinzip: Diversität", 13, NAVY, bold=True)
    box(ax, 6.9, 5.6, 2.8, 1.5, "DNS-\nAnbieter 1", fc=PINK, ec=RED, fs=10.5)
    cross(ax, 6.9, 5.6, 2.8, 1.5)
    box(ax, 10.0, 5.6, 2.8, 1.5, "DNS-\nAnbieter 2", fc=MINT, ec=GREEN, fs=10.5, color=GREEN)
    box(ax, 8.4, 2.6, 2.9, 1.3, "Website", fc=MINT, ec=GREEN, fs=10.5, color=GREEN)
    arrow(ax, (11.4, 5.55), (10.4, 3.95), color=GREEN, lw=2)
    text(ax, 9.8, 1.4, "✔ zweiter, unabhängiger\nAnbieter beantwortet Anfragen", 10.5, GREEN, bold=True)
    save(fig, "dyn-2016-abhaengigkeit.png")


# --------------------------------------------------------------------------------------
def zidkor_2026_konzentration():
    """KDZ Mainz / KGRZ Koblenz 27.–29.09.2026: vorsorgliche Abschaltung, 194 Verwaltungen betroffen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 1.5, 8.0, 10.0, 1.1, "kritische Sicherheitslücke in einem Herstellerprodukt", fc=CREAM, ec=ORANGE, fs=10.5, bold=False)
    arrow(ax, (6.5, 7.95), (6.5, 7.35), color=GREY)
    box(ax, 1.6, 5.8, 4.4, 1.5, "KDZ Mainz", fc=PINK, ec=RED, fs=12)
    box(ax, 7.0, 5.8, 4.4, 1.5, "KGRZ Koblenz", fc=PINK, ec=RED, fs=12)
    text(ax, 6.5, 6.55, "+", 18, RED, bold=True)
    text(ax, 6.5, 5.25, "vorsorglich abgeschaltet · 27.–29.09.2026", 11, RED, bold=True)
    arrow(ax, (6.5, 4.95), (6.5, 4.45), color=RED)
    box(ax, 0.3, 2.3, 12.4, 2.1, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 6.5, 3.95, "194 Städte, Gemeinden und Kreise in Rheinland-Pfalz", 11.5, NAVY, bold=True)
    services = ["Melde-\namt", "Pass,\nAusweis", "Kfz-Zu-\nlassung", "Standes-\namt", "Waffen-\nbehörde", "Schul-\nverwaltung"]
    for i, s in enumerate(services):
        x = 0.55 + i * 2.03
        box(ax, x, 2.45, 1.85, 1.15, s, fc=PINK, ec=RED, fs=8.5, color="#222222", bold=False, lw=1.5)
    box(ax, 0.3, 0.3, 12.4, 1.4, "Ein gemeinsamer Dienstleister bündelt Effizienz –\nund das Ausfallrisiko (Konzentrationsrisiko)",
        fc=ICE, ec=NAVY, fs=11)
    save(fig, "zidkor-2026-konzentration.png")


# --------------------------------------------------------------------------------------
def abschalten_abwaegung():
    """Vorsorgliche Abschaltung als Resilienzentscheidung: geplanter statt ungeplanter Ausfall."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.1, "Kritische Lücke bekannt – was nun?", 14, NAVY, bold=True)
    box(ax, 0.3, 3.4, 5.9, 4.9, "", fc=PINK, ec=RED)
    text(ax, 3.25, 7.6, "Weiterlaufen lassen", 12.5, RED, bold=True)
    text(ax, 3.25, 5.6, "• Dienst bleibt verfügbar\n• Risiko: Einbruch,\n  Datenabfluss\n• Folge offen: Tage\n  bis Monate", 10.5, "#222222")
    box(ax, 6.8, 3.4, 5.9, 4.9, "", fc=MINT, ec=GREEN)
    text(ax, 9.75, 7.6, "Vorsorglich abschalten", 12.5, GREEN, bold=True)
    text(ax, 9.75, 5.6, "• Dienst fällt geplant aus\n• kein Zugriff für\n  Angreifer\n• Folge absehbar:\n  Stunden bis Tage", 10.5, "#222222")
    box(ax, 0.3, 0.3, 12.4, 2.6, "", fc=ICE, ec=NAVY)
    text(ax, 6.5, 2.3, "Voraussetzung: Notbetrieb ist vorbereitet", 11.5, NAVY, bold=True)
    text(ax, 6.5, 1.0, "Stadt Mainz 21.10.2026: Website vom Netz –\nÄmter, Telefon und E-Mail laufen weiter", 10, "#222222")
    save(fig, "abschalten-abwaegung.png")


# --------------------------------------------------------------------------------------
def azure_ad_2021_kette():
    """Azure AD 15.03.2021: Automatik entfernt einen noch benötigten Signierschlüssel."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 7.6, 12.4, 1.4, "automatischer Prozess entfernt einen Signierschlüssel,\nder als „behalten“ markiert war",
        fc=CREAM, ec=ORANGE, fs=11, color="#222222", bold=False)
    arrow(ax, (6.5, 7.55), (6.5, 6.85), color=GREY)
    box(ax, 1.3, 5.3, 10.4, 1.5, "Anwendungen verwerfen damit signierte Tokens\n(ab ca. 19:00 UTC)",
        fc=PINK, ec=RED, fs=11, bold=False, color="#222222")
    effects = ["Teams, Exchange,\nSharePoint, Xbox", "Azure-Portal,\nKey Vault", "Drittanwendungen\nmit Azure-AD-Login"]
    for i, e in enumerate(effects):
        x = 0.3 + i * 4.2
        arrow(ax, (6.5, 5.25), (x + 1.95, 4.15), color=RED, lw=1.8, ms=14)
        box(ax, x, 2.6, 3.9, 1.5, e, fc=PINK, ec=RED, fs=10.5, bold=False, color="#222222")
    box(ax, 0.3, 0.3, 12.4, 1.6, "Systeme intakt, Anmeldung unmöglich –\nRollback 21:05 UTC, Restwirkungen bis zum Folgetag",
        fc=ICE, ec=NAVY, fs=11.5)
    save(fig, "azure-ad-2021-kette.png")


# --------------------------------------------------------------------------------------
def s3_2017_zeitleiste():
    """AWS S3 28.02.2017: ein Eingabefehler und gut vier Stunden Wiederanlauf (Zeiten PST)."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    yt = 5.4
    ax.plot([0.4, 12.6], [yt, yt], color="#222222", lw=2)
    marks = [(1.0, "09:37", "Befehl mit falscher\nEingabe entfernt zu\nviele Server", RED, True),
             (4.4, "11:37", "Status-Dashboard\nwieder aktualisierbar\n(hing an S3)", ORANGE, False),
             (6.5, "12:26", "Lesen und Löschen\nteilweise wieder\nmöglich", NAVY, True),
             (9.0, "13:18", "Index-Subsystem\nvoll da", NAVY, False),
             (11.9, "13:54", "S3 wieder\nnormal", GREEN, True)]
    for x, d, lab, c, up in marks:
        ax.plot([x, x], [yt - 0.25, yt + 0.25], color=c, lw=3.5)
        if up:
            text(ax, x, yt + 0.75, d, 11.5, c, bold=True)
            text(ax, x, yt + 2.05, lab, 9.5, "#222222")
        else:
            text(ax, x, yt - 0.75, d, 11.5, c, bold=True)
            text(ax, x, yt - 2.0, lab, 9.5, "#222222")
    ax.add_patch(FancyBboxPatch((1.0, yt - 0.18), 10.9, 0.36, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=PINK, ec=RED, lw=1.5))
    box(ax, 0.4, 0.3, 12.2, 1.6, "Konsequenz: Werkzeug entfernt langsamer und nie unter\nMindestkapazität – Leitplanken statt Schuldzuweisung",
        fc=CREAM, ec=NAVY, fs=11)
    save(fig, "s3-2017-zeitleiste.png")


# --------------------------------------------------------------------------------------
def countcare_2022_kunden():
    """Count+Care Juni 2022: Ransomware beim IT-Dienstleister trifft mehrere Versorger zugleich."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.25, "Ransomware beim Dienstleister · Juni 2022", 12.5, RED, bold=True)
    box(ax, 4.6, 4.0, 3.8, 1.8, "IT-Dienstleister\nCount+Care\n(Darmstadt)", fc=PINK, ec=RED, fs=11)
    clients = [(0.3, 6.6, "Entega\n(Darmstadt)", (4.6, 5.6), (3.0, 6.55)),
               (8.8, 6.6, "Mainzer Stadtwerke\ninkl. Nahverkehr", (8.4, 5.6), (10.0, 6.55)),
               (0.3, 2.2, "FES\n(Frankfurt)", (4.6, 4.2), (3.0, 3.65)),
               (8.8, 2.2, "HEAG\n(Darmstadt)", (8.4, 4.2), (10.0, 3.65)),
               (4.55, 7.1, "Kommunen\nin Südhessen", (6.5, 5.85), (6.5, 7.05))]
    for x, y, s, a, b in clients:
        box(ax, x, y, 3.9, 1.4, s, fc=CREAM, ec=ORANGE, fs=10, color="#222222", bold=False)
        arrow(ax, a, b, color=RED, lw=1.8, ms=13)
    box(ax, 0.3, 0.2, 6.0, 1.3, "✘ E-Mail, Websites,\nOnline-Dienste, Tickets", fc=PINK, ec=RED, fs=10, color=RED)
    box(ax, 6.7, 0.2, 6.0, 1.3, "✔ Strom, Gas, Wasser\nliefen weiter", fc=MINT, ec=GREEN, fs=10, color=GREEN)
    save(fig, "countcare-2022-kunden.png")


# --------------------------------------------------------------------------------------
def notkommunikation():
    """Kommunikation als Resilienzfähigkeit: Ersatzkanäle unabhängig von der eigenen IT."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 3.2, 9.0, "Primärkanäle", 13.5, RED, bold=True)
    text(ax, 9.8, 9.0, "Ersatzkanäle", 13.5, GREEN, bold=True)
    for i, s in enumerate(["E-Mail", "Website", "Intranet"]):
        y = 6.9 - i * 1.9
        box(ax, 0.8, y, 4.8, 1.4, s, fc=PINK, ec=RED, fs=11.5)
        cross(ax, 0.8, y, 4.8, 1.4)
    alts = [("Ersatzdomain\n(Mainzer Stadtwerke 2022)", 6.9), ("App, Instagram, LinkedIn\n(Hochschule Mainz 2025)", 5.0),
            ("Presse, Telefon, Aushang", 3.1)]
    for s, y in alts:
        box(ax, 7.2, y, 5.5, 1.4, s, fc=MINT, ec=GREEN, fs=10, color="#222222", bold=False)
    arrow(ax, (5.75, 5.7), (7.05, 5.7), color=GREY, lw=2.6, ms=20)
    box(ax, 0.3, 0.3, 12.4, 1.9, "vorbereitet, außerhalb der eigenen IT,\nmit bekannten Absendern",
        fc=ICE, ec=NAVY, fs=11.5)
    save(fig, "notkommunikation.png")


# --------------------------------------------------------------------------------------
def bedrohung_venn():
    """Klassisches Bedrohungsmodell: Angriff gelingt, wo Anfälligkeit, Erreichbarkeit und Fähigkeit zusammenkommen."""
    from matplotlib.patches import Circle
    import numpy as np
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    r = 2.75
    centers = [(4.8, 5.85), (8.2, 5.85), (6.5, 3.05)]
    fills = [ICE, CREAM, LILAC]
    edges = [NAVY, ORANGE, NAVY]
    for (cx, cy), fc in zip(centers, fills):
        ax.add_patch(Circle((cx, cy), r, fc=fc, ec="none", alpha=0.7))
    # Schnittmenge aller drei Kreise rot füllen
    xs, ys = np.meshgrid(np.linspace(3, 10, 700), np.linspace(1, 9, 700))
    inside = np.ones_like(xs, dtype=bool)
    for cx, cy in centers:
        inside &= (xs - cx) ** 2 + (ys - cy) ** 2 <= r ** 2
    ax.contourf(xs, ys, inside.astype(float), levels=[0.5, 1.5], colors=[RED], alpha=0.85)
    for (cx, cy), ec in zip(centers, edges):
        ax.add_patch(Circle((cx, cy), r, fc="none", ec=ec, lw=2.2))
    text(ax, 6.5, 4.95, "Angriff\nmöglich", 9.5, "white", bold=True)
    text(ax, 3.95, 7.0, "1. Anfälligkeit\ndes Systems", 11, NAVY, bold=True)
    text(ax, 3.4, 5.55, "Schwach-\nstellen, Wert\nfür Angreifer", 9, "#222222")
    text(ax, 9.3, 7.0, "2. Erreich-\nbarkeit", 11, ORANGE, bold=True)
    text(ax, 9.6, 5.55, "Angriffs-\nfläche, logisch\nund physisch", 9, "#222222")
    text(ax, 6.5, 2.15, "3. Fähigkeit des\nAngreifers", 11, NAVY, bold=True)
    text(ax, 6.5, 1.05, "Werkzeuge, Techniken,\nRessourcen", 9, "#222222")
    text(ax, 6.5, 9.2, "Resilienz fragt weiter: Was passiert, wenn der Angriff gelingt?", 11, NAVY, bold=True)
    save(fig, "bedrohung-venn.png")


# --------------------------------------------------------------------------------------
def identity_spof():
    """Identity als versteckter SPOF: zentraler IdP fällt aus, Break-Glass-Zugang als Rückfallebene."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 4.3, 2.4, 1.5, "Nutzer", fc=ICE, ec=NAVY, fs=11.5)
    arrow(ax, (2.75, 5.05), (4.05, 5.05), color=GREY)
    box(ax, 4.1, 4.0, 3.2, 2.1, "zentraler\nIdentity\nProvider", fc=PINK, ec=RED, fs=11)
    cross(ax, 4.1, 4.0, 3.2, 2.1)
    text(ax, 5.7, 3.55, "Anmeldung, Tokens (z. B. SAML)", 9.5, GREY)
    apps = ["E-Mail", "ERP", "Cloud-Dienst"]
    for i, a in enumerate(apps):
        y = 7.1 - i * 2.05
        box(ax, 9.3, y, 3.4, 1.4, a, fc=MINT, ec=GREEN, fs=11, color=GREEN)
        arrow(ax, (7.35, 5.05), (9.25, y + 0.7), color=RED, lw=1.8, ms=13, style="-")
        text(ax, 8.3, 5.05 + (y + 0.7 - 5.05) * 0.5 + 0.25, "✘", 12, RED, bold=True)
    text(ax, 11.0, 8.85, "Anwendungen laufen", 11, GREEN, bold=True)
    ax.plot([0.3, 12.7], [2.55, 2.55], color="#cccccc", ls="--", lw=1.5)
    box(ax, 0.3, 0.4, 4.4, 1.6, "Break-Glass-Konto\n(lokal, offline)", fc=MINT, ec=GREEN, fs=10.5, color=GREEN)
    arrow(ax, (4.75, 1.2), (9.25, 2.75), color=GREEN, lw=2.2, rad=-0.15)
    text(ax, 8.9, 0.95, "Notzugang ohne zentralen IdP", 10.5, GREEN, bold=True)
    text(ax, 2.0, 7.6, "Systeme intakt –\nniemand kommt hinein", 11, RED, bold=True)
    save(fig, "identity-spof.png")


if __name__ == "__main__":
    hsm_2025_wiederaufbau()
    bedrohungsklassen()
    dyn_2016_abhaengigkeit()
    zidkor_2026_konzentration()
    abschalten_abwaegung()
    azure_ad_2021_kette()
    s3_2017_zeitleiste()
    countcare_2022_kunden()
    notkommunikation()
    bedrohung_venn()
    identity_spof()
    print("Diagramme erzeugt in", OUT)
