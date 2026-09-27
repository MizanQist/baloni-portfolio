# Blueprint drawings for the vault placeholders: one line drawing per watch family, in champagne on black, drawn
# programmatically (case, bezel, dial furniture, hands at ten past ten, strap or bracelet, dimension ticks).
# Each returns an <svg> string; build_site.py wraps it. Replace with a photograph by setting image= in data.py.
import math

W, H = 300, 336
CX, CY = 150, 160
STROKE = "#cdb07a"; FAINT = "rgba(205,176,122,.35)"; DIM = "rgba(205,176,122,.55)"; INK = "rgba(233,231,225,.7)"

def _pt(cx, cy, r, deg):
    a = math.radians(deg); return cx + r * math.cos(a), cy + r * math.sin(a)

def _poly(n, cx, cy, r, rot=0):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in (_pt(cx, cy, r, rot + 360 * i / n) for i in range(n)))

def _hands(cx, cy, r, chrono=False):
    """hour and minute hands at 10:10, a seconds hand or a chronograph hand, plus the centre cap"""
    hx, hy = _pt(cx, cy, r * .52, -150); mx, my = _pt(cx, cy, r * .78, -60)
    out = f'<line x1="{cx}" y1="{cy}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>'
    out += f'<line x1="{cx}" y1="{cy}" x2="{mx:.1f}" y2="{my:.1f}" stroke="{INK}" stroke-width="2.6" stroke-linecap="round"/>'
    if not chrono:
        sx, sy = _pt(cx, cy, r * .84, 120); tx, ty = _pt(cx, cy, r * .16, 300)
        out += f'<line x1="{tx:.1f}" y1="{ty:.1f}" x2="{sx:.1f}" y2="{sy:.1f}" stroke="{STROKE}" stroke-width="1" stroke-linecap="round"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="3.2" fill="#0a0a0c" stroke="{INK}" stroke-width="1.2"/>'
    return out

def _ticks(cx, cy, r, n=12, long=7, short=3.5, skip=(), width=1.2):
    out = ""
    for i in range(n):
        if i in skip: continue
        deg = -90 + 360 * i / n; ln = long if i % (n // 12 or 1) == 0 else short
        x1, y1 = _pt(cx, cy, r, deg); x2, y2 = _pt(cx, cy, r - ln, deg)
        out += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="{width}" stroke-linecap="round"/>'
    return out

def _screws(cx, cy, r, n=8, rot=22.5, size=3.6):
    out = ""
    for i in range(n):
        x, y = _pt(cx, cy, r, rot + 360 * i / n)
        out += f'<polygon points="{_poly(6, x, y, size, 30 + i * 13)}" fill="#0a0a0c" stroke="{STROKE}" stroke-width=".9"/><line x1="{x-size*.55:.1f}" y1="{y:.1f}" x2="{x+size*.55:.1f}" y2="{y:.1f}" stroke="{STROKE}" stroke-width=".8" transform="rotate({i*23} {x:.1f} {y:.1f})"/>'
    return out

def _subdial(cx, cy, r):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{FAINT}" stroke-width=".8"/>' + _ticks(cx, cy, r, 12, 3, 1.6, width=.8) + f'<line x1="{cx}" y1="{cy}" x2="{cx + r*.6:.1f}" y2="{cy - r*.5:.1f}" stroke="{INK}" stroke-width="1" stroke-linecap="round"/>'

def _dims(label, x1, x2, y, sub=""):
    """a dimension line with end ticks and a label, blueprint fashion"""
    out = f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{DIM}" stroke-width=".6"/><line x1="{x1}" y1="{y-4}" x2="{x1}" y2="{y+4}" stroke="{DIM}" stroke-width=".6"/><line x1="{x2}" y1="{y-4}" x2="{x2}" y2="{y+4}" stroke="{DIM}" stroke-width=".6"/>'
    out += f'<text x="{(x1+x2)/2:.1f}" y="{y+13}" text-anchor="middle" font-family="DM Mono,monospace" font-size="8.5" letter-spacing="1.5" fill="{DIM}">{label}</text>'
    return out

def _frame():
    """corner ticks and a faint grid, so every drawing sits on the same sheet"""
    g = '<defs><pattern id="wg" width="15" height="15" patternUnits="userSpaceOnUse"><path d="M15 0H0V15" fill="none" stroke="rgba(233,231,225,.045)" stroke-width=".5"/></pattern><linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".18" stop-color="#fff" stop-opacity="1"/><stop offset=".84" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><mask id="fm"><rect width="300" height="336" fill="url(#fade)"/></mask></defs>'
    g += f'<rect width="{W}" height="{H}" fill="url(#wg)"/>'
    for x, y in ((16, 16), (W - 16, 16), (16, H - 16), (W - 16, H - 16)):
        dx = 8 if x < W / 2 else -8; dy = 8 if y < H / 2 else -8
        g += f'<path d="M{x} {y+dy}V{y}H{x+dx}" fill="none" stroke="{DIM}" stroke-width=".8"/>'
    return g

def _bracelet(cx, top, bottom, w, links=5, taper=.85, kind="H"):
    """an integrated bracelet drawn above and below the case; kind H = three-row links, kind S = strap"""
    out = ""
    if kind == "S":
        for y0, y1 in ((0, top), (bottom, H)):
            ww = w * .82
            out += f'<path d="M{cx-ww/2:.1f} {y0}L{cx-ww/2:.1f} {y1}M{cx+ww/2:.1f} {y0}L{cx+ww/2:.1f} {y1}" stroke="{STROKE}" stroke-width="1"/>'
            for y in range(int(min(y0, y1)) + 10, int(max(y0, y1)), 9):
                out += f'<line x1="{cx-ww/2+6:.1f}" y1="{y}" x2="{cx+ww/2-6:.1f}" y2="{y}" stroke="{FAINT}" stroke-width=".6"/>'
        return out
    n = links; step = top / n
    for side in (-1, 1):
        for i in range(n):
            f = 1 - (1 - taper) * (i / n)
            ww = w * f; y = top - (i + 1) * step if side == -1 else bottom + i * step
            out += f'<rect x="{cx-ww/2:.1f}" y="{y:.1f}" width="{ww:.1f}" height="{step-2:.1f}" rx="2" fill="none" stroke="{STROKE}" stroke-width=".9"/>'
            out += f'<line x1="{cx-ww/6:.1f}" y1="{y:.1f}" x2="{cx-ww/6:.1f}" y2="{y+step-2:.1f}" stroke="{FAINT}" stroke-width=".7"/><line x1="{cx+ww/6:.1f}" y1="{y:.1f}" x2="{cx+ww/6:.1f}" y2="{y+step-2:.1f}" stroke="{FAINT}" stroke-width=".7"/>'
    return out

def _wrap(inner, title, dims):
    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Line drawing of a {title}" xmlns="http://www.w3.org/2000/svg">' + _frame()
            + f'<g mask="url(#fm)">{inner}</g>' + dims
            + f'<text x="{W-16}" y="{H-24}" text-anchor="end" font-family="DM Mono,monospace" font-size="7.5" letter-spacing="2" fill="{DIM}">BLUEPRINT · PLACEHOLDER</text></svg>')

# ---------------------------------------------------------------- families
def nautilus():
    r = 62
    inner = _bracelet(CX, CY - r - 4, CY + r + 4, 92, 4, .88)
    inner += f'<ellipse cx="{CX}" cy="{CY}" rx="{r+14}" ry="{r+9}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4"/>'      # the porthole case
    inner += f'<rect x="{CX-r-26}" y="{CY-16}" width="14" height="32" rx="4" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.2"/><rect x="{CX+r+12}" y="{CY-16}" width="14" height="32" rx="4" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.2"/>'  # the ears
    inner += f'<polygon points="{_poly(8, CX, CY, r+3, 22.5)}" fill="none" stroke="{STROKE}" stroke-width="1.1" stroke-linejoin="round"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r-6}" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    for y in range(CY - r + 10, CY + r - 8, 6):                                                                             # the embossed horizontal dial
        half = math.sqrt(max(0, (r - 9) ** 2 - (y - CY) ** 2))
        inner += f'<line x1="{CX-half:.1f}" y1="{y}" x2="{CX+half:.1f}" y2="{y}" stroke="rgba(205,176,122,.22)" stroke-width=".8"/>'
    inner += _ticks(CX, CY, r - 9, 12, 8, 8, skip=(3,), width=2)
    inner += f'<rect x="{CX+r-30}" y="{CY-6}" width="16" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'      # date
    inner += _hands(CX, CY, r - 9)
    return _wrap(inner, "Nautilus", _dims("41 MM", CX - r - 14, CX + r + 14, CY + r + 26))

def aquanaut():
    r = 62
    inner = _bracelet(CX, CY - r - 2, CY + r + 2, 74, kind="S")
    inner += f'<path d="M{CX-r-8} {CY-r+16} Q{CX-r-8} {CY-r-2} {CX-r+10} {CY-r-2} L{CX+r-10} {CY-r-2} Q{CX+r+8} {CY-r-2} {CX+r+8} {CY-r+16} L{CX+r+8} {CY+r-16} Q{CX+r+8} {CY+r+2} {CX+r-10} {CY+r+2} L{CX-r+10} {CY+r+2} Q{CX-r-8} {CY+r+2} {CX-r-8} {CY+r-16} Z" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4"/>'
    inner += f'<polygon points="{_poly(8, CX, CY, r+1, 22.5)}" fill="none" stroke="{STROKE}" stroke-width="1"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r-8}" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    inner += f'<clipPath id="aqc"><circle cx="{CX}" cy="{CY}" r="{r-10}"/></clipPath><g clip-path="url(#aqc)">'
    for i in range(-9, 10):                                                                                                  # the embossed checker
        for j in range(-9, 10):
            x = CX + i * 11; y = CY + j * 11
            if (i + j) % 2 == 0: inner += f'<rect x="{x-4}" y="{y-4}" width="8" height="8" rx="2" fill="none" stroke="rgba(205,176,122,.2)" stroke-width=".7"/>'
    inner += '</g>'
    inner += _ticks(CX, CY, r - 10, 12, 7, 7, skip=(3,), width=2)
    inner += f'<rect x="{CX+r-30}" y="{CY-6}" width="16" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
    inner += _hands(CX, CY, r - 10)
    inner += f'<rect x="{CX+r+9}" y="{CY-7}" width="9" height="14" rx="2" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'   # crown
    return _wrap(inner, "Aquanaut", _dims("42.2 MM", CX - r - 8, CX + r + 8, CY + r + 26))

def royaloak(offshore=False):
    r = 66 if offshore else 62
    inner = _bracelet(CX, CY - r - 8, CY + r + 8, 96, 4, .86) if not offshore else _bracelet(CX, CY - r - 4, CY + r + 4, 80, kind="S")
    inner += f'<polygon points="{_poly(8, CX, CY, r+12, 22.5)}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4" stroke-linejoin="round"/>'  # octagonal bezel
    inner += f'<polygon points="{_poly(8, CX, CY, r+1, 22.5)}" fill="none" stroke="{STROKE}" stroke-width="1" stroke-linejoin="round"/>'
    inner += _screws(CX, CY, r + 6.5, 8, 22.5, 3.4)
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r-6}" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    inner += f'<clipPath id="roc"><circle cx="{CX}" cy="{CY}" r="{r-8}"/></clipPath><g clip-path="url(#roc)">'
    s = 9 if offshore else 6.5
    k = int(r / s) + 1
    for i in range(-k, k + 1):                                                                                               # the tapisserie
        for j in range(-k, k + 1):
            x = CX + i * s; y = CY + j * s
            inner += f'<rect x="{x-s*.36:.1f}" y="{y-s*.36:.1f}" width="{s*.72:.1f}" height="{s*.72:.1f}" fill="none" stroke="rgba(205,176,122,.18)" stroke-width=".6"/>'
    inner += '</g>'
    if offshore:
        inner += _subdial(CX - 24, CY, 13) + _subdial(CX + 24, CY, 13) + _subdial(CX, CY + 26, 13)
        inner += f'<rect x="{CX+r+12}" y="{CY-32}" width="9" height="16" rx="2" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/><rect x="{CX+r+12}" y="{CY+16}" width="9" height="16" rx="2" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'  # pushers
        inner += f'<rect x="{CX+r+10}" y="{CY-8}" width="12" height="16" rx="3" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'
        inner += _ticks(CX, CY, r - 8, 12, 8, 8, skip=(3,), width=2.2)
        inner += _hands(CX, CY, r - 9, chrono=True)
        inner += f'<line x1="{CX}" y1="{CY+10}" x2="{CX+r*.55:.1f}" y2="{CY-r*.62:.1f}" stroke="{STROKE}" stroke-width="1" stroke-linecap="round"/>'
    else:
        inner += _ticks(CX, CY, r - 8, 12, 8, 8, skip=(3,), width=2.2)
        inner += f'<rect x="{CX+r-30}" y="{CY-6}" width="16" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
        inner += _hands(CX, CY, r - 9)
        inner += f'<rect x="{CX+r+10}" y="{CY-7}" width="9" height="14" rx="2" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'
    return _wrap(inner, "Royal Oak Offshore" if offshore else "Royal Oak", _dims("43 MM" if offshore else "41 MM", CX - r - 12, CX + r + 12, CY + r + 30))

def santos():
    s = 58
    inner = _bracelet(CX, CY - s - 14, CY + s + 14, 90, 4, .9)
    inner += f'<rect x="{CX-s-8}" y="{CY-s-8}" width="{2*s+16}" height="{2*s+16}" rx="16" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4"/>'   # the square case
    inner += f'<rect x="{CX-s+2}" y="{CY-s+2}" width="{2*s-4}" height="{2*s-4}" rx="10" fill="none" stroke="{STROKE}" stroke-width="1"/>'
    for i, (x, y) in enumerate(((CX - s - 1, CY - s - 1), (CX, CY - s - 1), (CX + s + 1, CY - s - 1), (CX - s - 1, CY), (CX + s + 1, CY), (CX - s - 1, CY + s + 1), (CX, CY + s + 1), (CX + s + 1, CY + s + 1))):
        inner += f'<circle cx="{x}" cy="{y}" r="3.4" fill="#0a0a0c" stroke="{STROKE}" stroke-width=".9"/><line x1="{x-2}" y1="{y}" x2="{x+2}" y2="{y}" stroke="{STROKE}" stroke-width=".8" transform="rotate({i*27} {x} {y})"/>'
    inner += f'<rect x="{CX-s+12}" y="{CY-s+12}" width="{2*s-24}" height="{2*s-24}" rx="6" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    inner += f'<rect x="{CX-30}" y="{CY-30}" width="60" height="60" fill="none" stroke="{FAINT}" stroke-width=".7"/>'       # the rail track
    for i in range(12):                                                                                                     # roman hours as bars
        deg = -90 + 30 * i; x, y = _pt(CX, CY, 40, deg)
        inner += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{_pt(CX, CY, 33, deg)[0]:.1f}" y2="{_pt(CX, CY, 33, deg)[1]:.1f}" stroke="{INK}" stroke-width="{2 if i%3==0 else 1.2}" stroke-linecap="round"/>'
    inner += f'<rect x="{CX+s-24}" y="{CY-6}" width="14" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
    inner += _hands(CX, CY, s - 22)
    inner += f'<polygon points="{_poly(7, CX+s+16, CY, 6, 0)}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'         # the crown with its cabochon
    inner += f'<circle cx="{CX+s+16}" cy="{CY}" r="2" fill="{STROKE}"/>'
    return _wrap(inner, "Santos de Cartier", _dims("39.8 MM", CX - s - 8, CX + s + 8, CY + s + 32))

def tank():
    w, h = 42, 66
    inner = _bracelet(CX, CY - h - 6, CY + h + 6, 64, kind="S")
    inner += f'<rect x="{CX-w-14}" y="{CY-h-2}" width="12" height="{2*h+4}" rx="3" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.3"/><rect x="{CX+w+2}" y="{CY-h-2}" width="12" height="{2*h+4}" rx="3" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.3"/>'   # brancards
    inner += f'<rect x="{CX-w}" y="{CY-h+6}" width="{2*w}" height="{2*h-12}" rx="4" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.2"/>'
    inner += f'<rect x="{CX-w+8}" y="{CY-h+14}" width="{2*w-16}" height="{2*h-28}" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    inner += f'<rect x="{CX-22}" y="{CY-36}" width="44" height="72" fill="none" stroke="{FAINT}" stroke-width=".7"/>'
    for x in range(CX - 20, CX + 22, 4): inner += f'<line x1="{x}" y1="{CY-36}" x2="{x}" y2="{CY-33}" stroke="{FAINT}" stroke-width=".5"/><line x1="{x}" y1="{CY+36}" x2="{x}" y2="{CY+33}" stroke="{FAINT}" stroke-width=".5"/>'
    for i in range(12):
        deg = -90 + 30 * i; x, y = _pt(CX, CY, 42, deg); x2, y2 = _pt(CX, CY, 35, deg)
        y = max(CY - 46, min(CY + 46, y)); y2 = max(CY - 42, min(CY + 42, y2))
        inner += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{INK}" stroke-width="{2 if i%3==0 else 1.1}" stroke-linecap="round"/>'
    inner += _hands(CX, CY, 40)
    inner += f'<polygon points="{_poly(7, CX+w+22, CY, 6, 0)}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/><circle cx="{CX+w+22}" cy="{CY}" r="2" fill="{STROKE}"/>'
    return _wrap(inner, "Tank Louis Cartier", _dims("33.7 × 25.5 MM", CX - w - 14, CX + w + 14, CY + h + 24))

def overseas():
    r = 62
    inner = _bracelet(CX, CY - r - 10, CY + r + 10, 92, 4, .86)
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r+13}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4"/>'
    for i in range(6):                                                                                                      # the Maltese-cross bezel: six notches
        deg = 30 + 60 * i; x1, y1 = _pt(CX, CY, r + 13, deg - 7); x2, y2 = _pt(CX, CY, r + 13, deg + 7); mx, my = _pt(CX, CY, r + 4, deg)
        inner += f'<path d="M{x1:.1f} {y1:.1f}L{mx:.1f} {my:.1f}L{x2:.1f} {y2:.1f}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.1" stroke-linejoin="round"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r+1}" fill="none" stroke="{STROKE}" stroke-width="1"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r-6}" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r-11}" fill="none" stroke="{FAINT}" stroke-width=".6" stroke-dasharray="1 2.4"/>'
    inner += _ticks(CX, CY, r - 8, 12, 9, 9, skip=(3,), width=2.4)
    inner += f'<rect x="{CX+r-30}" y="{CY-6}" width="16" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
    inner += _hands(CX, CY, r - 9)
    inner += f'<rect x="{CX+r+12}" y="{CY-8}" width="11" height="16" rx="3" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'
    return _wrap(inner, "Overseas", _dims("41 MM", CX - r - 13, CX + r + 13, CY + r + 32))

def two22():
    r = 56
    inner = _bracelet(CX, CY - r - 10, CY + r + 10, 88, 4, .84)
    inner += f'<rect x="{CX-r-12}" y="{CY-r-8}" width="{2*r+24}" height="{2*r+16}" rx="{r-6}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4"/>'   # the tonneau-round case
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r+2}" fill="none" stroke="{STROKE}" stroke-width="1"/>'
    for i in range(24):                                                                                                     # the notched bezel
        deg = 360 * i / 24; x1, y1 = _pt(CX, CY, r + 2, deg); x2, y2 = _pt(CX, CY, r + 7, deg)
        inner += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{FAINT}" stroke-width="1"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{r-5}" fill="#0a0a0c" stroke="{FAINT}" stroke-width=".8"/>'
    inner += _ticks(CX, CY, r - 7, 12, 8, 8, skip=(3,), width=2)
    inner += f'<rect x="{CX+r-28}" y="{CY-6}" width="15" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
    inner += _hands(CX, CY, r - 8)
    mx, my = _pt(CX, CY, r + 9, 60)                                                                                          # the Maltese cross at five o'clock
    inner += f'<path d="M{mx:.1f} {my-6:.1f}l2.2 3.2 3.8-.6-2 3.4 2 3.4-3.8-.6-2.2 3.2-2.2-3.2-3.8.6 2-3.4-2-3.4 3.8.6z" fill="#0b0b0d" stroke="{STROKE}" stroke-width=".9"/>'
    inner += f'<rect x="{CX+r+12}" y="{CY-7}" width="9" height="14" rx="2" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'
    return _wrap(inner, "Historiques 222", _dims("37 MM", CX - r - 12, CX + r + 12, CY + r + 30))

def rm(chrono=True):
    w, h = 46, 66
    inner = _bracelet(CX, CY - h - 12, CY + h + 12, 72, kind="S")
    inner += f'<path d="M{CX-w-14} {CY-h+10} Q{CX-w-18} {CY} {CX-w-14} {CY+h-10} Q{CX-w-6} {CY+h+8} {CX-w+16} {CY+h+8} L{CX+w-16} {CY+h+8} Q{CX+w+6} {CY+h+8} {CX+w+14} {CY+h-10} Q{CX+w+18} {CY} {CX+w+14} {CY-h+10} Q{CX+w+6} {CY-h-8} {CX+w-16} {CY-h-8} L{CX-w+16} {CY-h-8} Q{CX-w-6} {CY-h-8} {CX-w-14} {CY-h+10} Z" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1.4"/>'  # the tonneau
    inner += f'<path d="M{CX-w-4} {CY-h+18} Q{CX-w-7} {CY} {CX-w-4} {CY+h-18} Q{CX-w} {CY+h-2} {CX-w+16} {CY+h-2} L{CX+w-16} {CY+h-2} Q{CX+w} {CY+h-2} {CX+w+4} {CY+h-18} Q{CX+w+7} {CY} {CX+w+4} {CY-h+18} Q{CX+w} {CY-h+2} {CX+w-16} {CY-h+2} L{CX-w+16} {CY-h+2} Q{CX-w} {CY-h+2} {CX-w-4} {CY-h+18} Z" fill="#0a0a0c" stroke="{STROKE}" stroke-width="1"/>'
    for x, y in ((CX - w - 8, CY - h + 12), (CX + w + 8, CY - h + 12), (CX - w - 8, CY + h - 12), (CX + w + 8, CY + h - 12), (CX - w - 11, CY), (CX + w + 11, CY), (CX - w + 6, CY - h - 2), (CX + w - 6, CY - h - 2), (CX - w + 6, CY + h + 2), (CX + w - 6, CY + h + 2), (CX, CY - h - 4), (CX, CY + h + 4)):
        inner += f'<circle cx="{x}" cy="{y}" r="3" fill="#0a0a0c" stroke="{STROKE}" stroke-width=".9"/><path d="M{x-1.6} {y-1.6}l3.2 3.2M{x+1.6} {y-1.6}l-3.2 3.2M{x} {y-2.2}v4.4" stroke="{STROKE}" stroke-width=".6"/>'  # spline screws
    inner += f'<clipPath id="rmc"><rect x="{CX-w}" y="{CY-h+4}" width="{2*w}" height="{2*h-8}" rx="26"/></clipPath><g clip-path="url(#rmc)">'
    for i in range(-3, 4):                                                                                                  # the skeleton bridges
        inner += f'<path d="M{CX-w-4} {CY+i*20} L{CX+w+4} {CY+i*20-14}" stroke="rgba(205,176,122,.2)" stroke-width="{1.4 if i%2 else .7}"/>'
    inner += f'<circle cx="{CX}" cy="{CY}" r="{w-4}" fill="none" stroke="{FAINT}" stroke-width=".7"/>'
    inner += f'<circle cx="{CX-20}" cy="{CY+40}" r="10" fill="none" stroke="{FAINT}" stroke-width=".7"/><circle cx="{CX+18}" cy="{CY-44}" r="8" fill="none" stroke="{FAINT}" stroke-width=".7"/>'
    for cx_, cy_, r_ in ((CX - 20, CY + 40, 10), (CX + 18, CY - 44, 8)):
        for k in range(12):
            x1, y1 = _pt(cx_, cy_, r_, 30 * k); x2, y2 = _pt(cx_, cy_, r_ - 2.5, 30 * k)
            inner += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{FAINT}" stroke-width=".5"/>'   # gear teeth
    inner += '</g>'
    inner += _ticks(CX, CY, w - 6, 12, 7, 5, skip=(), width=1.6)
    if chrono:
        inner += _subdial(CX - 22, CY - 4, 11) + _subdial(CX + 22, CY - 4, 11) + _subdial(CX, CY + 22, 10)
        inner += f'<rect x="{CX+w+12}" y="{CY-38}" width="9" height="18" rx="3" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/><rect x="{CX+w+12}" y="{CY+20}" width="9" height="18" rx="3" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/>'
        inner += f'<rect x="{CX+w-30}" y="{CY-42}" width="14" height="11" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
        inner += _hands(CX, CY, w - 8, chrono=True)
    else:
        inner += f'<rect x="{CX+w-26}" y="{CY-6}" width="14" height="12" rx="1.5" fill="#0a0a0c" stroke="{INK}" stroke-width=".9"/>'
        inner += _hands(CX, CY, w - 8)
    inner += f'<polygon points="{_poly(8, CX+w+20, CY, 7, 22.5)}" fill="#0b0b0d" stroke="{STROKE}" stroke-width="1"/><circle cx="{CX+w+20}" cy="{CY}" r="2.6" fill="none" stroke="{STROKE}" stroke-width=".8"/>'   # the crown
    return _wrap(inner, "Richard Mille tonneau", _dims("50 × 40 MM" if chrono else "47.5 × 38.7 MM", CX - w - 18, CX + w + 18, CY + h + 32))

ART = {"nautilus": nautilus, "aquanaut": aquanaut, "royaloak": lambda: royaloak(False), "offshore": lambda: royaloak(True), "santos": santos, "tank": tank, "overseas": overseas, "two22": two22, "rm011": lambda: rm(True), "rm67": lambda: rm(False)}

def watch_svg(kind):
    return ART[kind]()

if __name__ == "__main__":
    import os, sys
    out = sys.argv[1] if len(sys.argv) > 1 else "."
    for k in ART: open(os.path.join(out, k + ".svg"), "w").write(watch_svg(k))
    print("wrote", len(ART), "drawings to", out)
