"""Diagramme für den Foliensatz Termin 3 „Resilienz-Architekturen“.

Aufruf im Projektordner:  python assets/diagramme_termin03.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-03/assets/.
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
OUT = ROOT / "Präsentationen" / "Termin-03" / "assets"

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
def crowdstrike_common_mode():
    """CrowdStrike 2024: drei redundante Server mit identischem Agenten fallen gemeinsam aus."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    ax.plot([6.5, 6.5], [0.3, 9.0], color="#cccccc", ls="--", lw=2)
    text(ax, 3.2, 8.8, "Redundant, aber gleich", 14, NAVY, bold=True)
    text(ax, 9.8, 8.8, "Redundant und divers", 14, NAVY, bold=True)
    # Links: drei identische Knoten
    box(ax, 0.9, 6.7, 4.6, 1.0, "fehlerhaftes Update", fc=CREAM, ec=ORANGE, fs=11, color=ORANGE)
    for i in range(3):
        x = 0.2 + i * 2.05
        arrow(ax, (3.2, 6.65), (x + 0.85, 5.55), color=ORANGE, lw=1.8, ms=14)
        box(ax, x, 3.5, 1.7, 2.0, "", fc=PINK, ec=RED)
        text(ax, x + 0.85, 4.95, f"Server {i + 1}", 9.5, RED, bold=True)
        text(ax, x + 0.85, 4.15, "Agent A", 9.5, "#222222")
        cross(ax, x, 3.5, 1.7, 2.0)
    text(ax, 3.2, 2.5, "✘ alle Kopien fallen\ngleichzeitig aus", 12.5, RED, bold=True)
    text(ax, 3.2, 1.0, "Common-Mode-Failure:\neine Ursache, alle Replikate", 10.5, GREY)
    # Rechts: diverse Knoten
    box(ax, 7.5, 6.7, 4.6, 1.0, "fehlerhaftes Update", fc=CREAM, ec=ORANGE, fs=11, color=ORANGE)
    labels = [("Agent A", False), ("Agent B", True), ("Linux", True)]
    for i, (lab, ok) in enumerate(labels):
        x = 6.9 + i * 2.05
        fc, ec = (MINT, GREEN) if ok else (PINK, RED)
        if not ok:
            arrow(ax, (9.8, 6.65), (x + 0.85, 5.55), color=ORANGE, lw=1.8, ms=14)
        box(ax, x, 3.5, 1.7, 2.0, "", fc=fc, ec=ec)
        text(ax, x + 0.85, 4.95, f"Server {i + 1}", 9.5, ec, bold=True)
        text(ax, x + 0.85, 4.15, lab, 9.5, "#222222")
        if not ok:
            cross(ax, x, 3.5, 1.7, 2.0)
    text(ax, 9.8, 2.5, "✔ Dienst läuft\neingeschränkt weiter", 12.5, GREEN, bold=True)
    text(ax, 9.8, 1.0, "gestaffelter Rollout wirkt\nwie zeitliche Diversität", 10.5, GREY)
    save(fig, "crowdstrike-common-mode.png")


# --------------------------------------------------------------------------------------
def redundanz_ebenen():
    """Redundanz On-Prem und Cloud auf drei Ebenen: Komponente, Standort, Region."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 4.55, 9.05, "On-Prem", 14, NAVY, bold=True)
    text(ax, 9.4, 9.05, "Cloud", 14, NAVY, bold=True)
    rows = [("Komponente", "USV · Netzteile ·\nCore-Switches", "Instanzen hinter\nLoad Balancer", ICE),
            ("Rechen-\nzentrum /\nZone", "Active/Passive-\nCluster im RZ", "Multi-AZ-\nDeployment", CREAM),
            ("Standort /\nRegion", "zweites RZ\nCold · Warm · Hot", "Cross-Region-\nFailover", ROSE)]
    for i, (lvl, op, cl, fc) in enumerate(rows):
        y0 = 6.3 - i * 2.75
        text(ax, 0.1, y0 + 1.05, lvl, 10.5, NAVY, bold=True, ha="left")
        box(ax, 2.65, y0, 3.95, 2.1, op, fc=fc, ec=NAVY, fs=11, bold=False)
        box(ax, 7.6, y0, 3.6, 2.1, cl, fc=fc, ec=NAVY, fs=11, bold=False)
        text(ax, 7.1, y0 + 1.05, "≈", 20, GREY)
    arrow(ax, (11.75, 8.4), (11.75, 0.4), color=RED, lw=3, ms=22)
    text(ax, 12.4, 4.4, "Kosten und Umschaltaufwand steigen", 10, RED, rotation=270)
    save(fig, "redundanz-ebenen.png")


# --------------------------------------------------------------------------------------
def ba_2017_kaskade():
    """British Airways 27.05.2017: Stromunterbrechung führt trotz Redundanz zum Stillstand."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    steps = [("Stromversorgung im RZ\nbei Heathrow getrennt", CREAM, ORANGE),
             ("Wiederzuschaltung\n→ Überspannung", PINK, RED),
             ("IT-Systeme beschädigt,\nAusweichsysteme greifen nicht", PINK, RED),
             ("Check-in, Gepäck, Flugplanung\nstehen in Heathrow und Gatwick", PINK, RED)]
    for i, (s, fc, ec) in enumerate(steps):
        y0 = 7.6 - i * 2.05
        box(ax, 0.3, y0, 7.6, 1.5, s, fc=fc, ec=ec, fs=11.5, color="#222222", bold=False)
        if i < len(steps) - 1:
            arrow(ax, (4.1, y0 - 0.02), (4.1, y0 - 0.5), color=GREY, lw=2.2)
    box(ax, 8.6, 3.6, 4.2, 5.5, "", fc=ICE, ec=NAVY)
    text(ax, 10.7, 8.4, "Folgen", 13.5, NAVY, bold=True)
    text(ax, 10.7, 7.1, "479 Flüge am\n27. Mai gestrichen", 11, "#222222")
    text(ax, 10.7, 5.75, "≥ 75.000 Passagiere\nbetroffen", 11, "#222222")
    text(ax, 10.7, 4.4, "Kosten bis\n≈ 100 Mio. €", 11, "#222222")
    text(ax, 10.7, 2.3, "Redundanz ohne\nIsolation und\ngetestete Umschaltung", 11.5, RED, bold=True)
    save(fig, "ba-2017-kaskade.png")


# --------------------------------------------------------------------------------------
def recovery_kette():
    """Backup ≠ Recovery: Wiederherstellung als Kette, die an jedem Glied reißen kann."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    links = [("Backup\nvorhanden", ICE), ("isoliert /\noffline", ICE), ("Restore\ngetestet", CREAM),
             ("Runbook,\nRollen", CREAM), ("Dienst\nim RTO", MINT)]
    w, gap = 2.3, 0.28
    for i, (lab, fc) in enumerate(links):
        x = 0.2 + i * (w + gap)
        ec = GREEN if i == 4 else NAVY
        box(ax, x, 5.6, w, 2.0, lab, fc=fc, ec=ec, fs=10)
        if i < len(links) - 1:
            arrow(ax, (x + w + 0.02, 6.6), (x + w + gap - 0.02, 6.6), color=GREY, lw=2, ms=14)
    text(ax, 1.3, 8.4, "Zustand", 12, NAVY, bold=True)
    text(ax, 7.8, 8.4, "Fähigkeit (Prozess mit Zeit- und Qualitätszielen)", 12, NAVY, bold=True)
    ax.plot([0.2, 4.95], [8.0, 8.0], color=NAVY, lw=2)
    ax.plot([5.4, 12.8], [8.0, 8.0], color=NAVY, lw=2)
    box(ax, 0.2, 0.6, 12.6, 3.9, "", fc=PINK, ec=RED, lw=1.8)
    text(ax, 6.5, 3.85, "Typische Brüche", 13, RED, bold=True)
    text(ax, 0.6, 2.85, "• Backup im selben Brand- oder Angriffsbereich (OVHcloud 2021)", 10, "#222222", ha="left")
    text(ax, 0.6, 2.05, "• Restore nie geübt, Dauer unbekannt (GitLab 2017)", 10, "#222222", ha="left")
    text(ax, 0.6, 1.25, "• Dienst wird aufgegeben statt wiederhergestellt (Rackspace 2022)", 10, "#222222", ha="left")
    save(fig, "recovery-kette.png")


# --------------------------------------------------------------------------------------
def rackspace_2022_zeitleiste():
    """Rackspace Hosted Exchange 2022: vom ungepatchten Server zur Einstellung des Dienstes."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    yt = 5.2
    ax.plot([0.4, 12.6], [yt, yt], color="#222222", lw=2)
    marks = [(1.4, "8. Nov 2022", "Microsoft-Patch gegen\nProxyNotShell verfügbar", ORANGE, True),
             (4.6, "Rackspace", "patcht nicht, setzt auf\nWorkarounds", ORANGE, False),
             (7.6, "2. Dez 2022", "Play-Gruppe umgeht\nWorkarounds: Ransomware", RED, True),
             (11.4, "Anfang Jan 2023", "Exchange-Dienst wird\neingestellt statt\nwiederhergestellt", NAVY, False)]
    for x, d, lab, c, up in marks:
        ax.plot([x, x], [yt - 0.25, yt + 0.25], color=c, lw=3.5)
        if up:
            text(ax, x, yt + 0.8, d, 11.5, c, bold=True)
            text(ax, x, yt + 2.0, lab, 10.5, "#222222")
        else:
            text(ax, x, yt - 0.8, d, 11.5, c, bold=True)
            text(ax, x, yt - 2.1, lab, 10.5, "#222222")
    ax.add_patch(FancyBboxPatch((7.6, yt - 0.18), 3.8, 0.36, boxstyle="round,pad=0,rounding_size=0.1",
                                fc=PINK, ec=RED, lw=1.5))
    box(ax, 0.4, 0.3, 12.2, 1.4, "Recovery ist eine Entscheidung über Kosten und Zeit –\nnicht nur eine technische Frage",
        fc=CREAM, ec=NAVY, fs=11.5)
    save(fig, "rackspace-2022-zeitleiste.png")


# --------------------------------------------------------------------------------------
def netflix_drei_zonen():
    """Netflix 2011: drei aktive Zonen, eine fällt aus, die anderen tragen die Last."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.2, 2.6, 12.6, 6.0, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 6.5, 8.15, "AWS-Region US-East · 21. April 2011", 12.5, NAVY, bold=True)
    zones = [("Zone A", False), ("Zone B", True), ("Zone C", True)]
    for i, (z, ok) in enumerate(zones):
        x = 0.6 + i * 4.1
        fc, ec = (MINT, GREEN) if ok else (PINK, RED)
        box(ax, x, 3.0, 3.7, 4.5, "", fc=fc, ec=ec)
        text(ax, x + 1.85, 7.0, z, 12.5, ec, bold=True)
        for j in range(3):
            box(ax, x + 0.35 + j * 1.05, 5.1, 0.85, 1.1, "", fc="white", ec=ec, lw=1.5)
        if ok:
            text(ax, x + 1.85, 4.0, "nimmt Zusatzlast\naus Reserve auf", 10.5, GREEN)
        else:
            cross(ax, x, 3.0, 3.7, 4.5)
            text(ax, x + 1.85, 4.0, "Speicherdienst\ngestört", 10.5, RED)
    text(ax, 6.5, 1.85, "✔ zustandslose Dienste, Last auf zwei Zonen verteilt", 11.5, GREEN, bold=True)
    text(ax, 6.5, 0.85, "✘ Umleitung aus der Zone teils manuell – Chaos Monkey\n   hatte nur Einzelausfälle geübt, keinen Zonenausfall", 10.5, RED)
    save(fig, "netflix-drei-zonen.png")


# --------------------------------------------------------------------------------------
def facebook_2021_kopplung():
    """Facebook 04.10.2021: Backbone weg, DNS zieht Routen zurück, auch interne Werkzeuge fallen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 7.6, 12.4, 1.4, "Wartungsbefehl trennt alle Backbone-Verbindungen\n(Prüfwerkzeug stoppt ihn wegen eines Fehlers nicht)",
        fc=CREAM, ec=ORANGE, fs=11, color="#222222", bold=False)
    arrow(ax, (6.5, 7.55), (6.5, 6.85), color=GREY)
    box(ax, 2.0, 5.3, 9.0, 1.5, "DNS-Server ziehen BGP-Routen zurück\n– wie vorgesehen", fc=PINK, ec=RED, fs=11, bold=False, color="#222222")
    effects = ["alle Dienste\nunerreichbar", "interne Tools und\nFernzugriff weg", "Techniker müssen\nphysisch ins RZ"]
    for i, e in enumerate(effects):
        x = 0.3 + i * 4.2
        arrow(ax, (6.5, 5.25), (x + 1.95, 4.15), color=RED, lw=1.8, ms=14)
        box(ax, x, 2.6, 3.9, 1.5, e, fc=PINK, ec=RED, fs=10.5, bold=False, color="#222222")
    box(ax, 0.3, 0.3, 12.4, 1.6, "Datenebene verteilt – Steuerungsebene gemeinsam:\nder SPOF liegt im Management-Pfad",
        fc=ICE, ec=NAVY, fs=11.5)
    save(fig, "facebook-2021-kopplung.png")


# --------------------------------------------------------------------------------------
def prinzipien_wirkung():
    """Wirkung der vier Prinzipien auf die Resilienzkurve aus Termin 2."""
    fig, ax = plt.subplots(figsize=(6.5, 4.6))
    import numpy as np
    t = np.linspace(0, 10, 500)

    def curve(t, drop, t_rec, floor_len):
        y = np.full_like(t, 100.0)
        t0 = 2.0
        y = np.where((t >= t0) & (t < t0 + 0.2), 100 - drop * (t - t0) / 0.2, y)
        y = np.where((t >= t0 + 0.2) & (t < t0 + 0.2 + floor_len), 100 - drop, y)
        s = t0 + 0.2 + floor_len
        y = np.where((t >= s) & (t < s + t_rec), 100 - drop + drop * (t - s) / t_rec, y)
        return y

    ax.plot(t, curve(t, 90, 2.5, 2.5), color=RED, lw=2.6)
    ax.plot(t, curve(t, 45, 1.2, 0.6), color=GREEN, lw=2.6)
    ax.axvline(2, color="#222222", ls=":", lw=1.4)
    ax.text(1.9, 104, "Störung", ha="right", fontsize=11)
    ax.text(5.0, 4, "ohne Architekturprinzipien", fontsize=10.5, color=RED, fontweight="bold")
    ax.text(4.3, 92, "mit Prinzipien", fontsize=10.5, color=GREEN, fontweight="bold")
    ax.annotate("flacher:\nRedundanz,\nDiversität,\nAdaptivität", xy=(2.45, 55), xytext=(0.15, 22),
                fontsize=10, color=NAVY, arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.annotate("schneller zurück:\nWiederherstellbarkeit", xy=(3.6, 80), xytext=(7.3, 55),
                fontsize=10, color=NAVY, arrowprops=dict(arrowstyle="->", color=NAVY))
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 110)
    ax.set_xticks([])
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Servicelevel (%)")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "prinzipien-wirkung.png")


if __name__ == "__main__":
    crowdstrike_common_mode()
    redundanz_ebenen()
    ba_2017_kaskade()
    recovery_kette()
    rackspace_2022_zeitleiste()
    netflix_drei_zonen()
    facebook_2021_kopplung()
    prinzipien_wirkung()
    print("Diagramme erzeugt in", OUT)
