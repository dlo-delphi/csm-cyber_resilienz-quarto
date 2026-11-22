"""Diagramme für den Foliensatz Termin 8 „Zero Trust, Microsegmentation, Cloud Resilience, Network Design“.

Aufruf im Projektordner:  python assets/diagramme_termin08.py
Benötigt: matplotlib und die Schrift Inter (Fallback: DejaVu Sans).
Die PNG-Dateien landen in Präsentationen/Termin-08/assets/.
Gestaltung wie die Diagramme in Termin 1–7 (Inter, Navy-Rahmen, helle Flächen).
Alle Darstellungen sind schematisch; Zahlen stammen aus den in quellen.qmd genannten Quellen.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Präsentationen" / "Termin-08" / "assets"

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
def colonial_2021():
    """Colonial Pipeline 2021: ein Passwort, ein altes VPN-Profil, kein zweiter Faktor."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "7. Mai 2021 · Ransomware bei Colonial Pipeline (USA)",
        fc=PINK, ec=RED, fs=10, color=RED)
    steps = [("Passwort", "ein gültiges\nPasswort –\nkomplex, aber\nbekannt geworden", CREAM, ORANGE),
             ("Altes VPN-Profil", "nicht mehr\nin Gebrauch,\nnur ein Faktor,\nkein MFA", PINK, RED),
             ("IT-Netz", "Ransomware,\nrund 100 GB\nDaten kopiert", PINK, RED)]
    for i, (t, s, fc, ec) in enumerate(steps):
        x = 0.3 + i * 4.25
        box(ax, x, 3.85, 3.9, 3.7, "", fc=fc, ec=ec)
        text(ax, x + 1.95, 6.95, t, 10.2, ec, bold=True)
        text(ax, x + 1.95, 5.2, s, 8.9, "#222222")
        if i < 2:
            arrow(ax, (x + 3.9, 5.7), (x + 4.25, 5.7), color=GREY, lw=2, ms=13)
    box(ax, 0.3, 2.0, 12.4, 1.5, "Pipeline (OT) vorsorglich abgeschaltet – Neustart erst am 12. Mai.\nDie Leitung liefert rund 45 % des Treibstoffs der US-Ostküste",
        fc=CREAM, ec=ORANGE, fs=8.8, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.45, "Das VPN prüfte nur: Kennt jemand das Passwort?\nNicht: Wer ist es, mit welchem Gerät, zu welchem Zweck?",
        fc=ICE, ec=NAVY, fs=9)
    save(fig, "colonial-2021.png")


# --------------------------------------------------------------------------------------
def zero_trust_entscheidung():
    """Logische Bausteine nach NIST SP 800-207: jede Anfrage einzeln entschieden."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Jeder Zugriff wird einzeln entschieden", 13.5, NAVY, bold=True)
    signals = [("Identität", "Wer? MFA,\nRolle"), ("Gerät", "Patchstand,\nZertifikat"),
               ("Kontext", "Ort, Zeit,\nRisikosignal")]
    for i, (t, s) in enumerate(signals):
        y = 6.2 - i * 2.05
        box(ax, 0.3, y, 3.1, 1.75, "", fc=ICE, ec=NAVY)
        text(ax, 1.85, y + 1.22, t, 10, NAVY, bold=True)
        text(ax, 1.85, y + 0.55, s, 8.2, "#222222")
        arrow(ax, (3.4, y + 0.88), (4.55, 5.0), color=GREY, lw=1.6, ms=11)
    box(ax, 4.55, 3.9, 3.6, 2.2, "Policy Decision\nPoint (PDP)\nentscheidet", fc=CREAM, ec=ORANGE, fs=9.4, color="#222222")
    box(ax, 4.55, 1.85, 3.6, 1.6, "Policy Enforcement\nPoint (PEP)", fc=LILAC, ec=NAVY, fs=9.2, color="#222222")
    arrow(ax, (6.35, 3.9), (6.35, 3.45), color=ORANGE, lw=2, ms=12)
    box(ax, 9.4, 1.85, 3.3, 1.6, "Ressource –\nnur diese Sitzung", fc=MINT, ec=GREEN, fs=8.8, color=GREEN)
    arrow(ax, (8.15, 2.65), (9.4, 2.65), color=GREEN, lw=2.2, ms=14)
    box(ax, 9.4, 4.2, 3.3, 3.6, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 11.05, 7.2, "Telemetrie", 9.6, GREY, bold=True)
    text(ax, 11.05, 5.6, "Logs, Verhalten,\nBedrohungs-\ninformationen\nfließen zurück", 8.2, "#222222")
    arrow(ax, (9.4, 5.0), (8.15, 5.0), color=LGREY, lw=1.6, ms=11)
    box(ax, 0.3, 0.2, 12.4, 1.3, "Vertrauen gilt für eine Anfrage – nicht für einen Netzstandort",
        fc=ICE, ec=NAVY, fs=9.6)
    save(fig, "zero-trust-entscheidung.png")


# --------------------------------------------------------------------------------------
def twilio_cloudflare_2022():
    """Twilio und Cloudflare 2022: dieselbe Kampagne, unterschiedlicher zweiter Faktor."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "Juli/August 2022 · dieselbe SMS-Phishing-Kampagne",
        fc=CREAM, ec=ORANGE, fs=10, color="#222222")
    for x, title, fc, ec, lines in [
        (0.3, "Twilio", PINK, RED,
         "Beschäftigte geben\nZugangsdaten auf einer\nfalschen Login-Seite ein\n\nAngreifer erreichen\ninterne Werkzeuge\n\n209 Kundenkonten,\n93 Authy-Nutzer betroffen"),
        (6.7, "Cloudflare", MINT, GREEN,
         "mindestens 76 Beschäftigte\nerhalten die SMS,\n3 geben ihr Passwort ein\n\nFIDO2-Schlüssel ist an\ndie echte Domain gebunden\n\nkein Zugriff,\nkein System kompromittiert")]:
        box(ax, x, 1.75, 6.0, 5.9, "", fc=fc, ec=ec)
        text(ax, x + 3.0, 7.1, title, 11.5, ec, bold=True)
        text(ax, x + 3.0, 4.2, lines, 8.6, "#222222")
    box(ax, 0.3, 0.2, 12.4, 1.4, "Passwort und Einmalcode lassen sich abphishen –\nein an die Domain gebundener FIDO2-Schlüssel nicht",
        fc=ICE, ec=NAVY, fs=9.4)
    save(fig, "twilio-cloudflare-2022.png")


# --------------------------------------------------------------------------------------
def suedwestfalen_2023():
    """Südwestfalen-IT 2023: eine Domäne für alle Kunden, andere Domänen nicht betroffen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "Südwestfalen-IT 2023 · elf Tage vom Einstieg bis zur Verschlüsselung",
        fc=PINK, ec=RED, fs=9.4, color=RED)
    box(ax, 0.3, 4.0, 2.6, 3.6, "VPN\nohne MFA;\nSchwachstelle\nder Cisco ASA\nvermutet", fc=CREAM, ec=ORANGE, fs=8.6, color="#222222", bold=False)
    arrow(ax, (2.9, 5.8), (3.5, 5.8), color=RED, lw=2.4, ms=15)
    box(ax, 3.5, 3.0, 5.2, 4.6, "", fc=PINK, ec=RED)
    text(ax, 6.1, 7.15, "Domäne intra.lan", 10.5, RED, bold=True)
    text(ax, 6.1, 4.95, "770 Server, 4.176 Clients,\nzentrale Systeme und\nFachverfahren aller Kunden\n\nDomänen-Admin übernommen,\n961 Systeme mit\nErpressernachricht", 7.9, "#222222")
    box(ax, 9.1, 3.0, 3.6, 4.6, "", fc=MINT, ec=GREEN)
    text(ax, 10.9, 6.85, "andere Domänen,\nDMZ", 9.4, GREEN, bold=True)
    text(ax, 10.9, 4.9, "nicht betroffen\n\nBackups intakt,\nkein Datenabfluss\nnachgewiesen", 8.4, "#222222")
    ax.plot([8.9, 8.9], [2.9, 7.7], color=GREEN, lw=3, linestyle=(0, (4, 3)))
    box(ax, 0.3, 1.75, 12.4, 1.0, "72 Verbandskommunen – Bürgerdienste wochen- bis monatelang eingeschränkt",
        fc=CREAM, ec=ORANGE, fs=8.6, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.25, "Die Grenze zwischen den Domänen hat gehalten –\ninnerhalb von intra.lan gab es keine",
        fc=ICE, ec=NAVY, fs=9.2)
    save(fig, "suedwestfalen-2023.png")


# --------------------------------------------------------------------------------------
def microseg_einfuehrung():
    """Microsegmentation schrittweise einführen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Erst verstehen, dann sperren", 13.5, NAVY, bold=True)
    steps = [("1", "Datenflüsse\nerheben", "Wer spricht\nmit wem?", ICE, NAVY),
             ("2", "Audit-Modus", "Regeln nur\nprotokollieren", CREAM, ORANGE),
             ("3", "Enforcement", "Allow-List,\ndeny all", MINT, GREEN),
             ("4", "Pflegen", "Ausnahmen\nmit Ablaufdatum", LILAC, NAVY)]
    for i, (n, t, s, fc, ec) in enumerate(steps):
        x = 0.3 + i * 3.17
        box(ax, x, 3.6, 2.85, 4.5, "", fc=fc, ec=ec)
        text(ax, x + 1.42, 7.45, n, 15, ec, bold=True)
        text(ax, x + 1.42, 6.05, t, 9.6, "#222222", bold=True)
        text(ax, x + 1.42, 4.45, s, 8.4, "#222222")
        if i < 3:
            arrow(ax, (x + 2.85, 5.85), (x + 3.17, 5.85), color=GREY, lw=2, ms=12)
    box(ax, 0.3, 1.75, 12.4, 1.4, "Anfangen bei den Kronjuwelen und Admin-Zugängen –\nnicht beim ganzen Netz",
        fc=CREAM, ec=ORANGE, fs=8.8, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.2, "Leitfrage: Wer muss wirklich miteinander kommunizieren?",
        fc=ICE, ec=NAVY, fs=9.4)
    save(fig, "microseg-einfuehrung.png")


# --------------------------------------------------------------------------------------
def capital_one_2019():
    """Capital One 2019: Kette aus Fehlkonfiguration und zu weiter Rolle."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "März 2019 · Capital One in AWS – bemerkt erst im Juli",
        fc=PINK, ec=RED, fs=10, color=RED)
    steps = [("WAF", "falsch\nkonfiguriert,\nleitet Anfragen\nweiter (SSRF)"),
             ("Metadaten-\ndienst", "liefert\ntemporäre\nZugangsdaten\nder IAM-Rolle"),
             ("IAM-Rolle", "zu weit gefasst:\nüber 700\nS3-Buckets\nsichtbar"),
             ("Daten", "Daten zu\nrund 106 Mio.\nPersonen\nkopiert")]
    for i, (t, s) in enumerate(steps):
        x = 0.3 + i * 3.17
        fc, ec = (PINK, RED) if i in (0, 2) else (CREAM, ORANGE)
        if i == 3:
            fc, ec = "#f8f8f8", GREY
        box(ax, x, 3.7, 2.85, 3.9, "", fc=fc, ec=ec)
        text(ax, x + 1.42, 6.85, t, 9.4, ec, bold=True)
        text(ax, x + 1.42, 4.95, s, 8.2, "#222222")
        if i < 3:
            arrow(ax, (x + 2.85, 5.65), (x + 3.17, 5.65), color=GREY, lw=2, ms=12)
    text(ax, 1.72, 3.25, "Kunde", 8.6, RED, bold=True)
    text(ax, 7.66, 3.25, "Kunde", 8.6, RED, bold=True)
    box(ax, 0.3, 1.55, 12.4, 1.3, "Aufsicht (OCC, 2020): unzureichende Risikobewertung vor dem\nUmzug in die Cloud – 80 Mio. US-Dollar Strafe",
        fc=CREAM, ec=ORANGE, fs=8.6, bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.0, "Der Anbieter war nicht das Problem – Konfiguration und Rechte schon",
        fc=ICE, ec=NAVY, fs=9.2)
    save(fig, "capital-one-2019.png")


# --------------------------------------------------------------------------------------
def google_paris_2023():
    """Google Cloud europe-west9 2023: ein Gebäude, eine ganze Region."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "25./26. April 2023 · Wasser und Brand in Paris (europe-west9)",
        fc=PINK, ec=RED, fs=10, color=RED)
    box(ax, 0.3, 4.4, 12.4, 3.3, "", fc="#f8f8f8", ec=LGREY, lw=1.6)
    text(ax, 6.5, 7.25, "Region europe-west9: drei Zonen", 9.6, GREY, bold=True)
    for i, (t, s, fc, ec) in enumerate([("Zone a", "Gebäude geflutet,\nabgeschaltet", PINK, RED),
                                         ("Zone b", "physisch intakt –\ntrotzdem gestört", CREAM, ORANGE),
                                         ("Zone c", "ebenfalls\ngestört", CREAM, ORANGE)]):
        x = 0.7 + i * 4.0
        box(ax, x, 4.75, 3.6, 2.0, "", fc=fc, ec=ec)
        text(ax, x + 1.8, 6.2, t, 10, ec, bold=True)
        text(ax, x + 1.8, 5.3, s, 8.2, "#222222")
    box(ax, 0.3, 2.05, 12.4, 1.95, "", fc=PINK, ec=RED)
    text(ax, 6.5, 3.35, "gemeinsame Abhängigkeit: regionale Datenbank der Steuerungsebene", 9, RED, bold=True)
    text(ax, 6.5, 2.55, "Replikate nicht über die Gebäude verteilt → Quorum verloren → IAM und Dienste\nder ganzen Region gestört, die Cloud-Konsole weltweit beeinträchtigt", 8.1, "#222222")
    box(ax, 0.3, 0.2, 12.4, 1.45, "Mehrere Zonen helfen nur, wenn auch die Steuerungsebene\nunabhängig verteilt ist",
        fc=ICE, ec=NAVY, fs=9.2)
    save(fig, "google-paris-2023.png")


# --------------------------------------------------------------------------------------
def rogers_2022():
    """Rogers 2022: ein IP-Kern für Mobilfunk, Festnetz und Management."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    box(ax, 0.3, 8.05, 12.4, 1.25, "8. Juli 2022 · Rogers (Kanada): rund 26 Stunden Ausfall",
        fc=PINK, ec=RED, fs=10, color=RED)
    box(ax, 0.3, 5.55, 3.4, 2.0, "Konfigurations-\nänderung löscht\nRoutingfilter", fc=CREAM, ec=ORANGE, fs=8.8, color="#222222", bold=False)
    arrow(ax, (3.7, 6.55), (4.5, 6.55), color=RED, lw=2.4, ms=15)
    box(ax, 4.5, 5.25, 4.0, 2.6, "", fc=PINK, ec=RED)
    text(ax, 6.5, 7.15, "ein IP-Kernnetz", 10.5, RED, bold=True)
    text(ax, 6.5, 6.05, "Routinginformationen\nüberfluten die Router,\nkein Überlastschutz", 8.2, "#222222")
    box(ax, 9.3, 5.25, 3.4, 2.6, "> 12 Mio.\nKunden ohne\nMobilfunk, Festnetz,\nInternet, Notruf", fc=PINK, ec=RED, fs=8.4, color="#222222", bold=False)
    arrow(ax, (8.5, 6.55), (9.3, 6.55), color=RED, lw=2.4, ms=15)
    for x, t in [(0.3, "Mobilfunk"), (3.45, "Festnetz,\nInternet"), (6.6, "Management-\nnetz"), (9.75, "Kommunikation\nder Teams")]:
        box(ax, x, 2.6, 2.95, 1.85, t, fc="#f8f8f8", ec=GREY, fs=8.6, color="#222222")
        arrow(ax, (x + 1.47, 4.45), (6.5, 5.25), color=LGREY, lw=1.4, ms=10)
    text(ax, 6.5, 2.15, "alles hängt am selben Kern – Techniker müssen zu den Routern fahren", 8.4, RED, bold=True)
    box(ax, 0.3, 0.2, 12.4, 1.5, "Folge: Kerne trennen, Management-Netz unabhängig (Out-of-Band),\nÜberlastschutz, strengeres Change-Management",
        fc=ICE, ec=NAVY, fs=8.8)
    save(fig, "rogers-2022.png")


# --------------------------------------------------------------------------------------
def schadensdomaenen():
    """Redundanz zählt nur über Schadensdomänen hinweg."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "Redundanz braucht Unabhängigkeit", 13.5, NAVY, bold=True)
    text(ax, 2.3, 8.1, "Fall", 9.6, GREY, bold=True)
    text(ax, 6.0, 8.1, "scheinbar redundant", 9.6, GREY, bold=True)
    text(ax, 10.45, 8.1, "gemeinsamer Punkt", 9.6, RED, bold=True)
    rows = [("Google Paris 2023", "drei Zonen", "Datenbank der\nSteuerungsebene"),
            ("Rogers 2022", "Mobilfunk und\nFestnetz", "ein IP-Kern, auch\nfür das Management"),
            ("UniSuper 2024", "zwei Standorte", "Vertrag und\nSteuerungsebene"),
            ("Südwestfalen-IT 2023", "viele Kommunen,\nviele Fachverfahren", "eine Domäne,\nein Admin-Konto")]
    for i, (f, r, g) in enumerate(rows):
        y = 6.35 - i * 1.5
        box(ax, 0.3, y, 4.0, 1.25, f, fc=ICE, ec=NAVY, fs=8.8, color="#222222")
        box(ax, 4.5, y, 3.0, 1.25, r, fc=MINT, ec=GREEN, fs=8.4, color="#222222", bold=False)
        arrow(ax, (7.5, y + 0.62), (8.3, y + 0.62), color=RED, lw=1.8, ms=11)
        box(ax, 8.3, y, 4.4, 1.25, g, fc=PINK, ec=RED, fs=8.4, color="#222222", bold=False)
    box(ax, 0.3, 0.2, 12.4, 1.45, "Prüffrage: Was teilen die beiden Hälften noch –\nNetz, Identität, Steuerung, Management, Gebäude, Strom?",
        fc=CREAM, ec=ORANGE, fs=9)
    save(fig, "schadensdomaenen.png")


# --------------------------------------------------------------------------------------
def gamenova():
    """Übung GameNova GmbH: hybride Plattform mit vier Vorfällen."""
    fig, ax = canvas(6.5, 4.8, 13, 9.6)
    text(ax, 6.5, 9.15, "GameNova GmbH – Ausgangslage", 13.5, NAVY, bold=True)
    box(ax, 0.3, 4.3, 6.0, 4.1, "", fc=ICE, ec=NAVY)
    text(ax, 3.3, 7.95, "Public Cloud (AWS)", 9.6, NAVY, bold=True)
    box(ax, 0.6, 6.2, 2.6, 1.3, "Login,\nProfile", fc="white", ec=NAVY, fs=8.2, color="#222222", bold=False)
    box(ax, 3.4, 6.2, 2.6, 1.3, "Managed\nSQL", fc="white", ec=NAVY, fs=8.2, color="#222222", bold=False)
    box(ax, 0.6, 4.6, 5.4, 1.25, "Storage-Bucket\n(Telemetrie) – offen", fc=PINK, ec=RED, fs=8.2, color=RED)
    box(ax, 6.7, 4.3, 6.0, 4.1, "", fc=LILAC, ec=NAVY)
    text(ax, 9.7, 7.95, "eigenes Rechenzentrum", 9.6, NAVY, bold=True)
    box(ax, 7.0, 6.2, 2.6, 1.3, "Match-\nmaking", fc="white", ec=NAVY, fs=8.2, color="#222222", bold=False)
    box(ax, 9.8, 6.2, 2.6, 1.3, "Entwickler-\nnetz mit\nRansomware", fc=PINK, ec=RED, fs=7.6, color=RED)
    box(ax, 7.0, 4.6, 5.4, 1.25, "Router: 2 h Ausfall", fc=PINK, ec=RED, fs=8.4, color=RED)
    box(ax, 0.3, 2.3, 3.8, 1.5, "CDN:\nWeb-Frontend", fc="#f8f8f8", ec=GREY, fs=8.4, color="#222222", bold=False)
    box(ax, 4.6, 2.3, 8.1, 1.5, "Admin-VPN: gestohlene Zugangsdaten,\nunbemerkter Login", fc=PINK, ec=RED, fs=8.4, color=RED)
    box(ax, 0.3, 0.2, 12.4, 1.55, "Ihr Auftrag: Resilienzprogramm – Zero Trust, Segmentierung,\nCloud und Netz, priorisiert",
        fc=CREAM, ec=ORANGE, fs=9)
    save(fig, "gamenova.png")


if __name__ == "__main__":
    colonial_2021()
    zero_trust_entscheidung()
    twilio_cloudflare_2022()
    suedwestfalen_2023()
    microseg_einfuehrung()
    capital_one_2019()
    google_paris_2023()
    rogers_2022()
    schadensdomaenen()
    gamenova()
    print("Diagramme erzeugt in", OUT)
