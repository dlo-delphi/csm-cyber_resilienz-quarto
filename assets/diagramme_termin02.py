"""Diagramme für den Foliensatz Termin 2 „Modelle und Messbarkeit der Resilienz“.

Aufruf im Projektordner:  python assets/diagramme_termin02.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-02/assets/.
Gestaltung wie die Diagramme in Termin 1 (Inter, Navy-Rahmen, helle Flächen).
Alle Kurven sind schematisch und enthalten keine Messwerte.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Präsentationen" / "Termin-02" / "assets"

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
def ovh_standort_backup():
    """Brand OVHcloud 2021: Backup im selben Gebäude vs. an anderem Standort."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    ax.plot([6.5, 6.5], [0.3, 9.0], color="#cccccc", ls="--", lw=2)
    for x0, title, ok in [(0.2, "Backup im selben\nGebäude", False), (6.8, "Backup an anderem\nStandort", True)]:
        text(ax, x0 + 3.0, 8.7, title, 15, NAVY, bold=True)
        # Gebäude 1 mit Produktion (brennt)
        box(ax, x0 + 0.1, 3.6, 2.7, 3.2, "", fc=PINK, ec=RED)
        text(ax, x0 + 1.45, 6.3, "Gebäude A", 11, RED, bold=True)
        box(ax, x0 + 0.3, 4.75, 2.3, 0.9, "Produktion", fc="white", ec=RED, fs=10)
        if not ok:
            box(ax, x0 + 0.3, 3.8, 2.3, 0.8, "Backup", fc="white", ec=RED, fs=10)
        cross(ax, x0 + 0.1, 3.6, 2.7, 3.2)
        # Gebäude 2 / anderer Standort
        if ok:
            box(ax, x0 + 3.3, 3.6, 2.7, 3.2, "", fc=MINT, ec=GREEN)
            text(ax, x0 + 4.65, 6.3, "Standort B", 11, GREEN, bold=True)
            box(ax, x0 + 3.55, 4.3, 2.2, 0.9, "Backup", fc="white", ec=GREEN, fs=11)
            arrow(ax, (x0 + 2.7, 5.2), (x0 + 3.5, 4.75), color=GREEN, lw=2)
        else:
            box(ax, x0 + 3.3, 3.6, 2.7, 3.2, "", fc="#f6f6f6", ec=LGREY)
            text(ax, x0 + 4.65, 5.2, "Gebäude B\n(leer)", 11, LGREY)
        # Flammen-Symbol
        text(ax, x0 + 1.45, 7.35, "Brand", 12, RED, bold=True)
        if ok:
            text(ax, x0 + 3.0, 2.6, "✔ Wiederherstellung möglich", 13, GREEN, bold=True)
            text(ax, x0 + 3.0, 1.4, "RPO = Alter des letzten\nexternen Backups", 11.5, GREEN)
        else:
            text(ax, x0 + 3.0, 2.6, "✘ beides verloren", 13, RED, bold=True)
            text(ax, x0 + 3.0, 1.4, "RPO faktisch unbegrenzt:\nDaten sind weg", 11.5, RED)
    save(fig, "ovh-standort-backup.png")


# --------------------------------------------------------------------------------------
def verfuegbarkeit_mtbf_mttr():
    """Zeitstrahl Betrieb/Ausfall mit MTBF und MTTR, darunter die Verfügbarkeitsformel."""
    fig, ax = canvas(6.5, 4.6, 13, 9.2)
    segs = [(0.4, 3.4, "up"), (3.4, 4.4, "down"), (4.4, 8.2, "up"), (8.2, 9.2, "down"), (9.2, 12.6, "up")]
    y = 6.0
    for a, b, s in segs:
        fc, ec = (MINT, GREEN) if s == "up" else (PINK, RED)
        ax.add_patch(FancyBboxPatch((a, y), b - a, 1.0, boxstyle="round,pad=0,rounding_size=0.12",
                                    fc=fc, ec=ec, lw=2))
    text(ax, 1.9, y + 0.5, "Betrieb", 11.5, GREEN, bold=True)
    text(ax, 6.3, y + 0.5, "Betrieb", 11.5, GREEN, bold=True)
    text(ax, 10.9, y + 0.5, "Betrieb", 11.5, GREEN, bold=True)
    # MTBF-Klammer über Betriebsphase
    ax.annotate("", xy=(4.4, 7.55), xytext=(8.2, 7.55), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=2))
    text(ax, 6.3, 8.05, "MTBF – Zeit zwischen Ausfällen", 12, NAVY, bold=True)
    # MTTR-Pfeil unter Ausfall
    ax.annotate("", xy=(8.2, 5.5), xytext=(9.2, 5.5), arrowprops=dict(arrowstyle="|-|", color=RED, lw=2, mutation_scale=6))
    text(ax, 8.7, 4.8, "MTTR – Reparaturdauer", 12, RED, bold=True)
    text(ax, 3.9, 5.5, "Ausfall", 11, RED)
    text(ax, 12.6, 4.8, "Zeit →", 10.5, GREY, ha="right")
    # Formel
    box(ax, 0.6, 0.5, 11.8, 3.2, "", fc=CREAM, ec=NAVY)
    text(ax, 6.5, 2.85, "Verfügbarkeit  A = MTBF ÷ (MTBF + MTTR)", 15, NAVY, bold=True)
    text(ax, 6.5, 1.55, "Beispiel: MTBF 30 Tage, MTTR 45 min  →  A ≈ 99,9 %", 12.5, "#222222")
    save(fig, "verfuegbarkeit-mtbf-mttr.png")


# --------------------------------------------------------------------------------------
def gitlab_rpo():
    """GitLab.com 31.01.2017: geplante Sicherungen versagten, ein Zufalls-Snapshot rettete."""
    fig, ax = canvas(6.5, 4.9, 13, 9.8)
    # Sicherungsverfahren
    items = [("tägliches pg_dump", "leer – Versionskonflikt,\nFehlermails nie zugestellt", False),
             ("Cloud-Disk-Snapshots", "für die Datenbank\nnicht aktiviert", False),
             ("Replikat", "beim Neuaufbau\ngelöscht", False),
             ("LVM-Snapshot", "manuell, für Staging –\nzufällig 6 h alt", True)]
    for i, (name, why, ok) in enumerate(items):
        yy = 8.5 - i * 1.45
        ec, fc, col = (GREEN, MINT, GREEN) if ok else (RED, PINK, RED)
        box(ax, 0.2, yy - 0.55, 5.0, 1.1, name, fc=fc, ec=ec, fs=10.5)
        text(ax, 5.5, yy, why, 10.5, col, ha="left")
        text(ax, 12.6, yy, "✔" if ok else "✘", 18, col, bold=True, ha="right")
    # Zeitstrahl
    yt = 1.6
    ax.plot([0.3, 12.7], [yt, yt], color="#222222", lw=2)
    marks = [(1.4, "Snapshot\n≈ 17:20 UTC", GREEN), (5.0, "Löschung\n≈ 23:30 UTC", RED), (11.8, "wieder online\n1.2., ≈ 18:00", NAVY)]
    for x, lab, c in marks:
        ax.plot([x, x], [yt - 0.2, yt + 0.2], color=c, lw=3)
        text(ax, x, yt - 0.85, lab, 10, c)
    ax.annotate("", xy=(1.4, yt + 0.55), xytext=(5.0, yt + 0.55), arrowprops=dict(arrowstyle="<->", color=GREEN, lw=2))
    text(ax, 3.2, yt + 0.95, "Datenverlust ≈ 6 h", 11.5, GREEN, bold=True)
    ax.annotate("", xy=(5.0, yt + 0.55), xytext=(11.8, yt + 0.55), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=2))
    text(ax, 8.4, yt + 0.95, "Ausfall ≈ 18 h", 11.5, NAVY, bold=True)
    save(fig, "gitlab-2017-rpo.png")


# --------------------------------------------------------------------------------------
def framework_ebenen():
    """Frameworks als Ordnungsrahmen auf vier Ebenen, Messgrößen liefern Evidenz."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    layers = [("Sektor & Lieferketten", "ENISA", LILAC),
              ("Organisation", "BSI-Standard 200-4", ROSE),
              ("IKT-Bereitschaft", "ISO/IEC 27031", CREAM),
              ("System & Architektur", "NIST SP 800-160 Vol. 2", ICE)]
    for i, (lvl, fw, fc) in enumerate(layers):
        y0 = 7.2 - i * 2.2
        indent = 0.35 * (3 - i) * 0 + 0.0
        box(ax, 0.2 + indent, y0, 9.0, 1.8, "", fc=fc, ec=NAVY)
        text(ax, 0.6, y0 + 1.2, lvl, 13.5, NAVY, bold=True, ha="left")
        text(ax, 0.6, y0 + 0.55, fw, 12, "#222222", ha="left")
    # Evidenzpfeil
    arrow(ax, (9.9, 0.6), (9.9, 8.7), color=GREEN, lw=4, ms=26)
    text(ax, 11.55, 4.7, "Messgrößen\nliefern\nEvidenz", 11.5, GREEN, bold=True)
    text(ax, 11.55, 2.0, "RTO · RPO\nMTTR · MTBF", 10, GREEN)
    save(fig, "framework-ebenen.png")


# --------------------------------------------------------------------------------------
def kpi_drei_ebenen():
    """Technische, organisatorische und subjektive Messmethoden mit Beispielen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    cols = [("Technisch", ICE, ["MTTR", "Restore-Test\nbestanden?", "Alter des letzten\nBackups (RPO-Ist)"]),
            ("Organisatorisch", CREAM, ["BCM-KPIs:\nPläne getestet", "Übungen pro Jahr", "offene Audit-\nFeststellungen"]),
            ("Subjektiv", ROSE, ["Selbst-\nbewertung", "Reifegrad-\ninterview", "Experten-\neinschätzung"])]
    for i, (title, fc, ex) in enumerate(cols):
        x0 = 0.2 + i * 4.3
        box(ax, x0, 1.6, 4.0, 7.6, "", fc=fc, ec=NAVY)
        text(ax, x0 + 2.0, 8.55, title, 12, NAVY, bold=True)
        for j, e in enumerate(ex):
            box(ax, x0 + 0.3, 6.25 - j * 1.9, 3.4, 1.55, e, fc="white", ec=NAVY, fs=9.5, bold=False, lw=1.5)
    ax.annotate("", xy=(0.3, 0.75), xytext=(12.7, 0.75), arrowprops=dict(arrowstyle="<->", color=GREY, lw=2))
    text(ax, 0.3, 0.2, "objektiv gemessen", 10.5, GREY, ha="left")
    text(ax, 12.7, 0.2, "eingeschätzt", 10.5, GREY, ha="right")
    save(fig, "kpi-drei-ebenen.png")


# --------------------------------------------------------------------------------------
def reifegradtreppe():
    """Fünfstufiger Entwicklungspfad (Skript Abschnitt 5.2)."""
    fig, ax = canvas(7.6, 4.8, 16, 10.1)
    stufen = [("1 Ad hoc", "reaktiv,\nEinzelaktionen", PINK, RED),
              ("2 Definiert", "Prozesse da,\nnoch unzuverlässig", ROSE, ORANGE),
              ("3 Etabliert", "Rollen, Tests,\nKPIs verankert", CREAM, "#b08900"),
              ("4 Gesteuert", "Messgrößen\ngenutzt", ICE, NAVY),
              ("5 Optimiert", "Resilience\nby Design", MINT, GREEN)]
    w = 3.15
    for i, (name, desc, fc, ec) in enumerate(stufen):
        x0 = 0.2 + i * w
        h = 1.4 + i * 1.35
        ax.add_patch(FancyBboxPatch((x0, 1.6), w - 0.12, h, boxstyle="round,pad=0,rounding_size=0.15",
                                    fc=fc, ec=ec, lw=2.2))
        text(ax, x0 + (w - 0.12) / 2, 1.6 + h - 0.45, name, 11, ec, bold=True)
        text(ax, x0 + (w - 0.12) / 2, 0.8, desc, 9.5, "#333333")
    arrow(ax, (0.7, 5.4), (8.4, 9.6), color=GREY, lw=2.2, rad=-0.15)
    text(ax, 1.0, 9.0, "Fähigkeit vor\ndem Ereignis", 12, GREY, bold=True, ha="left")
    save(fig, "reifegradtreppe.png")


# --------------------------------------------------------------------------------------
def reifegrad_metrik_matrix():
    """2×2: organisatorischer Reifegrad × gemessene Recovery."""
    fig, ax = canvas(6.5, 5.2, 13, 10.4)
    q = [(1.6, 5.4, "Papiersicherheit", "Pläne und Rollen,\naber nie getestet", CREAM, ORANGE),
         (7.2, 5.4, "Nachweislich\nresilient", "Rahmen + gemessene,\ngeübte Recovery", MINT, GREEN),
         (1.6, 0.9, "Fragil", "weder Rahmen\nnoch Evidenz", PINK, RED),
         (7.2, 0.9, "Zufallssicherheit", "gute Technik,\nkein Rahmen", ROSE, ORANGE)]
    for x0, y0, t, d, fc, ec in q:
        box(ax, x0, y0, 5.4, 4.3, "", fc=fc, ec=ec)
        text(ax, x0 + 2.7, y0 + 2.8, t, 15, ec, bold=True)
        text(ax, x0 + 2.7, y0 + 1.15, d, 11, "#333333")
    arrow(ax, (1.2, 0.6), (1.2, 10.1), color=NAVY, lw=2)
    text(ax, 0.55, 5.4, "Reifegrad (Rollen, Pläne, Übungen)", 11.5, NAVY, bold=True, rotation=90)
    arrow(ax, (1.2, 0.6), (12.9, 0.6), color=NAVY, lw=2)
    text(ax, 7.0, 0.05, "gemessene Recovery (MTTR, Restore-Tests)", 11.5, NAVY, bold=True)
    save(fig, "reifegrad-metrik-matrix.png")


# --------------------------------------------------------------------------------------
def gleiche_stoerung_drei_kurven():
    """Dasselbe Ereignis, drei Architekturen: Hard-Fail, Failover, Graceful Degradation."""
    import numpy as np

    t = np.linspace(0, 10, 600)

    def ramp(t, t0, t1, a, b):
        x = np.clip((t - t0) / (t1 - t0), 0, 1)
        s = x * x * (3 - 2 * x)
        return a + (b - a) * s

    hard = np.where(t < 2, 100, np.where(t < 2.15, ramp(t, 2, 2.15, 100, 0),
                    np.where(t < 7.2, 0, ramp(t, 7.2, 8.8, 0, 100))))
    fail = np.where(t < 2, 100, np.where(t < 2.15, ramp(t, 2, 2.15, 100, 25), ramp(t, 2.15, 2.9, 25, 100)))
    grace = np.where(t < 2, 100, np.where(t < 2.8, ramp(t, 2, 2.8, 100, 65),
                     np.where(t < 4.5, 65, ramp(t, 4.5, 5.8, 65, 100))))

    fig, ax = plt.subplots(figsize=(6.8, 4.6))
    ax.axvspan(0, 2, color=ICE, alpha=0.6, lw=0)
    ax.axhline(90, color=LGREY, ls="--", lw=1.4)
    ax.text(0.1, 80, "akzeptabler\nServicelevel", ha="left", fontsize=9.5, color=GREY)
    ax.plot(t, hard, color=RED, lw=3.2)
    ax.plot(t, grace, color=ORANGE, lw=3.2)
    ax.plot(t, fail, color=GREEN, lw=3.2)
    ax.axvline(2, color="#222222", ls=":", lw=1.4)
    ax.text(1.9, 40, "Störung", ha="right", fontsize=11, color="#222222")
    ax.text(3.05, 80, "Failover", fontsize=11, color=GREEN, fontweight="bold")
    ax.text(3.3, 57, "Graceful Degradation", fontsize=11, color=ORANGE, fontweight="bold")
    ax.text(2.4, 8, "Hard-Fail, Restore aus Offline-Backup", fontsize=10, color=RED, fontweight="bold")
    ax.set_xlim(0, 10)
    ax.set_ylim(-3, 110)
    ax.set_xticks([])
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Servicelevel (%)")
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    save(fig, "gleiche-stoerung-drei-kurven.png")


if __name__ == "__main__":
    ovh_standort_backup()
    verfuegbarkeit_mtbf_mttr()
    gitlab_rpo()
    framework_ebenen()
    kpi_drei_ebenen()
    reifegradtreppe()
    reifegrad_metrik_matrix()
    gleiche_stoerung_drei_kurven()
    print("Diagramme erzeugt in", OUT)
