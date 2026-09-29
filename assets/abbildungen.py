"""Erzeugt die gemeinsamen Abbildungen für Kapitel und Foliensätze.

Aufruf im Projektordner:  python assets/abbildungen.py
Benötigt: matplotlib. Die PNG-Dateien werden neben diesem Skript abgelegt.
Die Inhalte folgen den Vorlesungsunterlagen WS 2025/26; die Kurven sind
schematisch und enthalten keine Messwerte.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
NAVY = "#183449"
RED = "#9c343a"
BLUE = "#175b84"
GREY = "#6b7280"
LIGHT = "#dce6ef"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 12})


def save(fig, name):
    fig.savefig(HERE / name, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def resilienzkurve():
    """Degradations- und Wiederherstellungskurve mit RPO, RTO, Δ und tR (Sitzung 2)."""
    t = [0, 2, 2.4, 4.2, 6.5, 8, 10]
    level = [100, 100, 35, 35, 90, 100, 100]
    fig, ax = plt.subplots(figsize=(10, 4.6))
    ax.plot(t, level, color=NAVY, lw=3)
    ax.axhline(90, color=GREY, ls="--", lw=1)
    ax.text(10, 91.5, "akzeptabler Servicelevel", ha="right", color=GREY, fontsize=10)
    ax.axvline(2, color=RED, ls=":", lw=1.5)
    ax.text(2.1, 72, "Störung", color=RED, fontsize=11)
    # RPO: Datenverlustfenster vor der Störung
    ax.annotate("", xy=(0.8, 55), xytext=(2, 55), arrowprops=dict(arrowstyle="<->", color=BLUE, lw=2))
    ax.text(1.4, 58, "RPO\nDatenverlust", ha="center", color=BLUE, fontsize=10)
    ax.axvline(0.8, color=BLUE, ls=":", lw=1)
    ax.text(0.82, 8, "letzter\nSicherungspunkt", color=BLUE, fontsize=9)
    # RTO: Zeit bis zum akzeptablen Niveau
    ax.annotate("", xy=(2, 20), xytext=(6.5, 20), arrowprops=dict(arrowstyle="<->", color=RED, lw=2))
    ax.text(4.25, 22.5, "RTO (Ziel) bzw. tR (gemessen)", ha="center", color=RED, fontsize=10)
    # Ausfalltiefe Δ
    ax.annotate("", xy=(3.3, 100), xytext=(3.3, 35), arrowprops=dict(arrowstyle="<->", color=NAVY, lw=1.5))
    ax.text(3.4, 66, "Ausfalltiefe Δ", color=NAVY, fontsize=10)
    for x, label in [(1, "1 Normalbetrieb"), (2.3, "2"), (3.1, "3 degradiert"), (5.3, "4 Recovery"), (9, "5 Zielzustand")]:
        ax.text(x, 104, label, ha="center", fontsize=9, color=GREY)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 112)
    ax.set_xlabel("Zeit")
    ax.set_ylabel("Servicelevel L(t) in %")
    ax.set_xticks([])
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    save(fig, "resilienzkurve.png")


def box(ax, x, y, w, h, text, fc=LIGHT, ec=NAVY, fs=12, color=NAVY, bold=True):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", fc=fc, ec=ec, lw=2))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=color,
            fontweight="bold" if bold else "normal")


def arrow(ax, a, b, color=NAVY, style="-|>", rad=0.0):
    ax.add_patch(FancyArrowPatch(a, b, arrowstyle=style, mutation_scale=18, color=color, lw=2,
                                 connectionstyle=f"arc3,rad={rad}"))


def resilienzzyklus():
    """Detection → Response → Recovery → Adapt (Sitzung 5)."""
    fig, ax = plt.subplots(figsize=(7.5, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    pos = {"Detection": (3.5, 6.2), "Response": (7, 3.5), "Recovery": (3.5, 0.8), "Adapt": (0, 3.5)}
    sub = {"Detection": "Früherkennung", "Response": "Sofortmaßnahmen,\nSchadensbegrenzung",
           "Recovery": "Wiederanlauf auf\ndefiniertem Niveau", "Adapt": "Lernen und\nOptimieren"}
    for k, (x, y) in pos.items():
        box(ax, x, y, 3, 1.2, "", fc="white")
        ax.text(x + 1.5, y + 0.82, k, ha="center", va="center", fontsize=14, color=NAVY, fontweight="bold")
        ax.text(x + 1.5, y + 0.36, sub[k], ha="center", va="center", fontsize=9, color=GREY)
    arrow(ax, (6.6, 6.6), (8.3, 4.8), RED, rad=-0.25)
    arrow(ax, (8.3, 3.4), (6.6, 1.5), RED, rad=-0.25)
    arrow(ax, (3.4, 1.5), (1.6, 3.4), RED, rad=-0.25)
    arrow(ax, (1.6, 4.8), (3.4, 6.6), RED, rad=-0.25)
    ax.text(5, 4.3, "Resilienzzyklus", ha="center", fontsize=13, color=NAVY)
    ax.text(5, 3.5, "ISO 22316\nISO/IEC 27035\nBSI 200-4", ha="center", fontsize=9, color=GREY)
    save(fig, "resilienzzyklus.png")


def eskalationsmodell():
    """Beispielhafte Eskalationsstruktur (Skript Sitzung 6, Kap. 8.2)."""
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.4)
    ax.axis("off")
    box(ax, 3.5, 7, 5, 1, "Management Board")
    box(ax, 4.25, 5.2, 3.5, 1, "CISO")
    box(ax, 0.8, 3.2, 4, 1, "SOC (Detection)")
    box(ax, 7.2, 3.2, 4, 1, "CERT (Response)")
    box(ax, 0.8, 1.2, 4, 1, "IT Operations", fc="white")
    box(ax, 7.2, 1.2, 4, 1, "DPO / BCM / Risk", fc="white")
    arrow(ax, (6, 6.2), (6, 7.0))
    arrow(ax, (2.8, 4.2), (4.8, 5.2))
    arrow(ax, (9.2, 4.2), (7.2, 5.2))
    arrow(ax, (4.8, 3.7), (7.2, 3.7), RED)
    arrow(ax, (2.8, 3.2), (2.8, 2.2), style="<|-|>")
    arrow(ax, (9.2, 3.2), (9.2, 2.2), style="<|-|>")
    ax.text(6, 3.95, "Übergabe\n≤ 15 min", ha="center", fontsize=9, color=RED)
    ax.text(8.9, 4.75, "≤ 30 min", fontsize=9, color=RED)
    ax.text(6, 0.3, "Zeitvorgaben beispielhaft nach Skript Sitzung 6", ha="center", fontsize=9, color=GREY)
    save(fig, "eskalationsmodell.png")


def purdue():
    """Purdue-Modell (ISA-95) mit Ebenen 0–5 (Sitzung 9)."""
    levels = [
        ("Level 5", "Externe Partner / Cloud", "Fernwartung, IIoT-Plattformen, Cloud-SCADA"),
        ("Level 4", "Unternehmens-IT", "ERP, Supply-Chain-Management, Analytics"),
        ("Level 3", "Produktionsleitsysteme", "MES, Batch-Management, Qualitätskontrolle"),
        ("Level 2", "Überwachung & Kontrolle", "SCADA, HMI, Historian"),
        ("Level 1", "Steuerungsebene", "PLC, RTU, Embedded Controller"),
        ("Level 0", "Physische Prozesse", "Sensoren, Aktoren, Maschinen"),
    ]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(-0.6, 7.1)
    ax.axis("off")
    for i, (lvl, name, ex) in enumerate(levels):
        y = 6.1 - i * 1.1 - (0.5 if i >= 2 else 0)
        it = i <= 1
        box(ax, 0.3, y, 11.4, 0.9, "", fc=LIGHT if it else "white", ec=BLUE if it else NAVY)
        ax.text(0.6, y + 0.45, lvl, va="center", fontsize=12, color=RED, fontweight="bold")
        ax.text(2.2, y + 0.58, name, va="center", fontsize=12, color=NAVY, fontweight="bold")
        ax.text(2.2, y + 0.24, ex, va="center", fontsize=10, color=GREY)
    ax.plot([0.3, 11.7], [4.72, 4.72], color=RED, lw=3, ls="--")
    ax.text(6, 4.72, " IT/OT-Übergang: Segmentierung (Zonen & Conduits) ", ha="center", va="center",
            fontsize=10, color=RED, bbox=dict(fc="white", ec="none"))
    save(fig, "purdue-modell.png")


if __name__ == "__main__":
    resilienzkurve()
    resilienzzyklus()
    eskalationsmodell()
    purdue()
    print("Abbildungen erzeugt in", HERE)
