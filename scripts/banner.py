"""Generates assets/banner-dark.svg and assets/banner-light.svg: a terminal window, `flow.sh --live`.
Left: a head agent, two coordinators and their workers, with work moving between them and a human gate.
Right: a key/value profile that types itself in. Pure SVG + SMIL, no fonts or scripts, so GitHub renders it as an image.
Run: python scripts/banner.py
"""
from pathlib import Path

W, H = 1180, 560
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
THEMES = {
    "dark": dict(bg="#000000", win="#07070b", panel="#0b0b12", line="#26283a", ink="#ffffff", mist="#d4d4d4", smoke="#8f93ad", accent="#a3a8ee", warm="#f0a35e"),
    "light": dict(bg="#ffffff", win="#fbfbfd", panel="#f3f3f8", line="#d9dae6", ink="#0b0b12", mist="#2b2c3a", smoke="#5f6280", accent="#4b52c4", warm="#b8611d"),
}
ROWS = [
    ("Subject", "Uziel Di Paola"),
    ("Role", "AI & Full-stack Engineer"),
    ("Origin", "Buenos Aires · UTC−3"),
    ("Domain", "AML software for banks & fintechs"),
    ("Experience", "6 yrs in AML · coding since 2025"),
    ("Core.Lang", "TypeScript · Python · C#"),
    ("Core.Backend", "Node · Fastify · .NET 8 · NATS"),
    ("Core.Frontend", "Angular · React · Astro"),
    ("Core.Data", "SQL Server · PostgreSQL · RabbitMQ"),
    ("Agents", "Claude Code · Orca · human gates"),
    ("Status", "open to contract · freelance · part-time"),
    ("Grid.Web", "portfolio.wuzi.uk"),
    ("Grid.LinkedIn", "/in/uzidp"),
]
# the agent tree (left panel): id -> (x, y, label, kind)
NODES = {
    "head": (245, 160, "head", "head"),
    "tl1": (140, 270, "tl-1", "tl"),
    "tl2": (350, 270, "tl-2", "tl"),
    "w1": (85, 380, "coder", "w"),
    "w2": (195, 380, "reviewer", "w"),
    "w3": (295, 380, "tester", "w"),
    "w4": (405, 380, "coder", "w"),
    "sub": (85, 452, "explore", "sub"),
}
EDGES = [("head", "tl1"), ("head", "tl2"), ("tl1", "w1"), ("tl1", "w2"), ("tl2", "w3"), ("tl2", "w4"), ("w1", "sub")]
T = 8  # seconds per loop


def svg(t):
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
    a('<title id="title">flow.sh --live: Uziel Di Paola</title>')
    a('<desc id="desc">A terminal window. On the left, a lead agent, two coordinating agents and their workers pass work along while a human gate waits for approval. On the right, a profile: AI and full-stack engineer in Buenos Aires, six years in anti-money-laundering software, TypeScript, Python and C#, open to contract work.</desc>')
    a(f'<defs><filter id="glow" x="-100%" y="-100%" width="300%" height="300%"><feGaussianBlur stdDeviation="3.5"/></filter></defs>')
    a(f'<rect width="{W}" height="{H}" rx="18" fill="{t["bg"]}"/>')
    a(f'<rect x="12" y="12" width="{W-24}" height="{H-24}" rx="13" fill="{t["win"]}" stroke="{t["line"]}"/>')
    a(f'<path d="M12 58H{W-12}" stroke="{t["line"]}"/>')
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        a(f'<circle cx="{38+i*21}" cy="35" r="6" fill="{c}"/>')
    a(f'<text x="{W//2}" y="40" text-anchor="middle" fill="{t["smoke"]}" font-family="{MONO}" font-size="13" letter-spacing=".4">flow.sh --live</text>')
    # panels
    a(f'<rect x="32" y="80" width="430" height="440" rx="6" fill="{t["panel"]}" stroke="{t["line"]}"/>')
    a(f'<path d="M32 112H462" stroke="{t["line"]}"/>')
    a(f'<text x="46" y="101" fill="{t["accent"]}" font-family="{MONO}" font-size="12" letter-spacing="1.5">AGENTS.MAP</text>')
    a(f'<text x="448" y="101" text-anchor="end" fill="{t["smoke"]}" font-family="{MONO}" font-size="11">1 head · 2 tl · 4 workers</text>')
    a(f'<rect x="482" y="80" width="666" height="440" rx="6" fill="{t["panel"]}" stroke="{t["line"]}"/>')
    a(f'<path d="M482 112H1148" stroke="{t["line"]}"/>')
    a(f'<text x="496" y="101" fill="{t["accent"]}" font-family="{MONO}" font-size="12" letter-spacing="1.5">SYSTEM.INFO</text>')
    a(f'<circle cx="986" cy="97" r="4" fill="{t["warm"]}"><animate attributeName="opacity" values="1;.2;1" dur="1.6s" repeatCount="indefinite"/></circle>')
    a(f'<text x="998" y="101" fill="{t["warm"]}" font-family="{MONO}" font-size="11" letter-spacing="1">LIVE</text>')
    a(f'<text x="1134" y="101" text-anchor="end" fill="{t["smoke"]}" font-family="{MONO}" font-size="11">@uzi-dev99</text>')
    # edges + packets
    for i, (p, c) in enumerate(EDGES):
        x1, y1 = NODES[p][:2]; x2, y2 = NODES[c][:2]
        dash = ' stroke-dasharray="4 5"' if c == "sub" else ""
        a(f'<path id="e{i}" d="M{x1} {y1}L{x2} {y2}" stroke="{t["line"]}" stroke-width="1.5"{dash}/>')
    for i, (p, c) in enumerate(EDGES):
        for k in range(2):
            # one trip of 1.6 s per half loop; the loop repeats forever (keyTimes place the trip inside the period)
            s0 = ((i * 0.9 + k * T / 2) % (T - 1.6)) / T; s1 = s0 + 1.6 / T
            kt = f"0;{s0:.4f};{s1:.4f};1"
            a(f'<circle r="3.2" fill="{t["accent"]}" opacity="0"><animateMotion dur="{T}s" repeatCount="indefinite" calcMode="linear" keyPoints="0;0;1;1" keyTimes="{kt}"><mpath href="#e{i}"/></animateMotion>'
              f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;{s0:.4f};{s0+0.02:.4f};{s1-0.02:.4f};{s1:.4f};1" dur="{T}s" repeatCount="indefinite"/></circle>')
    # nodes
    for nid, (x, y, label, kind) in NODES.items():
        r = {"head": 22, "tl": 17, "w": 13, "sub": 8}[kind]
        fill = t["accent"] if kind == "head" else t["win"]
        a(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" fill-opacity="{0.18 if kind == "head" else 1}" stroke="{t["accent"] if kind != "sub" else t["smoke"]}" stroke-width="1.6"/>')
        if kind != "sub":
            dur = {"head": 3.2, "tl": 2.6, "w": 2.0}[kind]
            a(f'<circle cx="{x}" cy="{y}" r="{r*0.38:.1f}" fill="{t["accent"]}"><animate attributeName="opacity" values=".35;1;.35" dur="{dur}s" begin="{(x % 7) / 10:.1f}s" repeatCount="indefinite"/></circle>')
        a(f'<text x="{x}" y="{y + r + 17}" text-anchor="middle" fill="{t["mist"]}" font-family="{MONO}" font-size="12">{label}</text>')
    # the human gate on the head: a ring that opens for a few seconds every loop
    hx, hy = NODES["head"][:2]
    a(f'<circle cx="{hx}" cy="{hy}" r="30" fill="none" stroke="{t["warm"]}" stroke-width="2" opacity="0">'
      f'<animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;.5;.55;.85;.9;1" dur="{T}s" repeatCount="indefinite"/>'
      f'<animate attributeName="r" values="30;30;30;34;30;30" keyTimes="0;.5;.55;.7;.85;1" dur="{T}s" repeatCount="indefinite"/></circle>')
    a(f'<g opacity="0"><animate attributeName="opacity" values="0;0;1;1;0;0" keyTimes="0;.5;.55;.85;.9;1" dur="{T}s" repeatCount="indefinite"/>'
      f'<rect x="{hx+40}" y="{hy-30}" width="168" height="44" rx="6" fill="{t["win"]}" stroke="{t["warm"]}"/>'
      f'<text x="{hx+52}" y="{hy-12}" fill="{t["warm"]}" font-family="{MONO}" font-size="11" letter-spacing="1">GATE · WAITING</text>'
      f'<text x="{hx+52}" y="{hy+5}" fill="{t["ink"]}" font-family="{MONO}" font-size="12">merge PR? → my OK</text></g>')
    a(f'<text x="46" y="506" fill="{t["smoke"]}" font-family="{MONO}" font-size="11">● anything irreversible waits for a human</text>')
    # rows, typed in one after another, then they stay
    y0, dy = 146, 27
    for i, (k, v) in enumerate(ROWS):
        y = y0 + i * dy
        begin = 0.25 + i * 0.18
        a(f'<g opacity="0"><animate attributeName="opacity" from="0" to="1" dur=".25s" begin="{begin:.2f}s" fill="freeze"/>'
          f'<text x="500" y="{y}" fill="{t["smoke"]}" font-family="{MONO}" font-size="14">{k}</text>'
          f'<text x="1130" y="{y}" text-anchor="end" fill="{t["ink"] if i < 2 else t["mist"]}" font-family="{MONO}" font-size="14"{" font-weight=\"700\"" if i < 2 else ""}>{v}</text></g>')
    cy = y0 + len(ROWS) * dy - 4
    a(f'<rect x="500" y="{cy}" width="9" height="16" fill="{t["accent"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    a(f'<text x="{W-34}" y="{H-24}" text-anchor="end" fill="{t["smoke"]}" font-family="{MONO}" font-size="11">● all agents nominal · UTC−3</text>')
    a('</svg>')
    return "".join(o).replace("&", "&amp;").replace("&amp;amp;", "&amp;")


out = Path(__file__).resolve().parent.parent / "assets"
out.mkdir(exist_ok=True)
for name, theme in THEMES.items():
    (out / f"banner-{name}.svg").write_text(svg(theme), encoding="utf-8")
    print(name, (out / f"banner-{name}.svg").stat().st_size, "bytes")
