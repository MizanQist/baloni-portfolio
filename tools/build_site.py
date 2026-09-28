# Generates index.html for the Baloni Private Office from data.py and client.py. Run: python3 tools/build_site.py
# Design: site_css.py · behaviour: site_js.py · vault drawings: watch_art.py
import os, sys, json, html as H, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import SITES, WATCHES, HOUSES, AGENT, AGENT_FIRST, AGENT_INITIALS, AGENT_ROLE, DATE, CLIENT, CLIENT_SHORT, CLIENT_FIRST, CLIENT_SURNAME, CLIENT_CARD, CLIENT_SALUTATION, CLIENT_SIGNOFF, MEMBER_SINCE, SLUG
from site_css import CSS
from site_js import JS
from watch_art import watch_svg
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITLE = f"The {CLIENT_SURNAME} Private Office"
FONTS = "https://fonts.googleapis.com/css2?family=Bodoni+Moda:ital,opsz,wght@0,6..96,400;0,6..96,500;1,6..96,400&family=Manrope:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap"

# ---------------------------------------------------------------- markup helpers
MARK = '<svg viewBox="0 0 100 100" aria-hidden="true"><circle cx="48" cy="46" r="44" fill="currentColor"/><g fill="var(--void)"><rect x="18" y="22" width="11" height="48"/><rect x="67" y="22" width="11" height="48"/><path d="M29 22h11l8 18-6 12z"/><path d="M67 22H56l-8 18 6 12z"/></g><rect x="66" y="72" width="32" height="12" fill="currentColor" transform="rotate(45 82 78)"/></svg>'
MARK_LINE = '<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><circle cx="48" cy="46" r="43"/><path d="M24 24v44M72 24v44M24 24l24 30 24-30" stroke-linejoin="round"/><path d="M70 74l22 22" stroke-width="7"/></svg>'
STAR = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2.5c.9 5.6 3.9 8.6 9.5 9.5-5.6.9-8.6 3.9-9.5 9.5-.9-5.6-3.9-8.6-9.5-9.5 5.6-.9 8.6-3.9 9.5-9.5z"/></svg>'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M4 12h16M13 5l7 7-7 7"/></svg>'
CHEV_L = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>'
CHEV_R = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>'
CLOSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>'
ZOOM = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5M11 8v6M8 11h6"/></svg>'
LIST = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h10"/></svg>'
SEAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>'

LAZY = 'loading="lazy"'
def esc(s): return H.escape(str(s), quote=True)

_DIM = {}
def dim(name):
    if name not in _DIM:
        from PIL import Image
        try: _DIM[name] = Image.open(os.path.join(ROOT, "assets", name)).size
        except Exception: _DIM[name] = None
    return _DIM[name]

def img(name, alt, sizes, extra=""):
    """<img> for an asset; JPEGs wider than 1400 px get their phone edition (assets/m/) in srcset, PNG plans do not."""
    if name.endswith(".jpg") and dim(name) and dim(name)[0] > 1400:
        w = dim(name)[0]
        return f'<img src="assets/{name}" srcset="assets/m/{name} 1400w, assets/{name} {w}w" sizes="{sizes}" alt="{alt}" decoding="async" {extra}>'
    return f'<img src="assets/{name}" alt="{alt}" decoding="async" {extra}>'

def name_markup(text):
    words, i = [], 0
    for w in text.split(" "):
        chars = "".join(f'<span class="ch" style="--i:{i+k}">{esc(c)}</span>' for k, c in enumerate(w))
        i += len(w) + 1
        words.append(f'<span class="w" aria-hidden="true">{chars}</span>')
    return "".join(words)

def chip(status): return f'<span class="chip" data-s="{esc(status)}"><i></i>{esc(status)}</span>'
def star(item, label):
    return f'<button class="star" type="button" data-id="{item["id"]}" aria-pressed="false" aria-label="Add {esc(label)} to your requests" title="Add to your requests">{STAR}</button>'
def btn(label, href=None, cls="", attrs=""):
    inner = f'{esc(label)}<i>{ARROW}</i>'
    if href: return f'<a class="btn {cls}" href="{href}" {attrs}>{inner}</a>'
    return f'<button type="button" class="btn {cls}" {attrs}>{inner}</button>'

# ---------------------------------------------------------------- chrome
def chrome():
    dz_rows = "".join(f'<a href="#{s["id"]}" data-go="{s["id"]}" style="--i:{i}"><span class="k">{s["n"]}</span><span>{esc(s["name"])}<small>{esc(s["district"])}{", Lagos" if s["city"]=="Lagos" else ""} · {esc(s["status"])}</small></span><span class="pr">{esc(s["price"])}</span></a>' for i, s in enumerate(SITES))
    w_rows = "".join(f'<a href="#vault" data-go="vault" style="--i:{i}"><span class="k">{w["n"]}</span><span>{esc(w["house"])} {esc(w["model"])}<small>{esc(w["ref"])}</small></span><span class="pr">{esc(w["status"])}</span></a>' for i, w in enumerate(WATCHES))
    secs = [("welcome", "Welcome"), ("brief", "Your brief"), ("residences", "Wing I · Residences"), ("glance", "Map &amp; ledger"), ("vault", "Wing II · The vault"), ("desk", "Your desk")]
    secs_html = "".join(f'<a href="#{i}" data-go="{i}" style="--i:{k}">{l}</a>' for k, (i, l) in enumerate(secs))
    return f'''
<div id="veil" aria-hidden="true"><div class="in"><div class="mark">{MARK_LINE}</div><div class="ro" id="vro">Mizan Qist · Private Office</div><div class="line"><i id="vline"></i></div><div class="ct" id="vct">000</div></div></div>
<div class="progress" aria-hidden="true"><i id="pbar"></i></div>
<div class="corner l"><b>The {esc(CLIENT_SURNAME)} Private Office</b>Prepared for {esc(CLIENT)}</div>
<div class="corner r"><b>{esc(DATE)}</b>Held by {esc(AGENT)}</div>
<nav class="isl" id="isl" aria-label="Your office">
  <a class="brand" href="#welcome" data-go="welcome" aria-label="Back to the top">{MARK}<span><b>{esc(CLIENT_SURNAME)}</b><small>Private Office</small></span></a>
  <span class="sep"></span>
  <span class="ind" id="ind" aria-hidden="true"></span>
  <button type="button" class="tab" data-go="brief">Brief</button>
  <button type="button" class="tab" data-go="residences">Residences</button>
  <button type="button" class="tab" data-go="vault">Vault</button>
  <button type="button" class="tab" data-go="desk">Desk<span class="n" id="reqcount"></span></button>
  <span class="sep"></span>
  <span class="clock" id="clock"></span>
  <button type="button" class="tab" id="idxbtn" aria-haspopup="dialog" aria-controls="index" aria-label="Open the index">Index</button>
</nav>
<div id="index" role="dialog" aria-modal="true" aria-label="Index"><div class="in">
  <div class="ih"><div><div class="eyebrow">Index</div><h2 class="t-2">Everything in your office.</h2></div><button type="button" class="close" id="idxclose" aria-label="Close the index">{CLOSE}</button></div>
  <div class="secs">{secs_html}</div>
  <div class="cols"><div><h3>Wing I · Ten residences</h3><div class="rows">{dz_rows}</div></div><div><h3>Wing II · Ten pieces</h3><div class="rows">{w_rows}</div></div></div>
</div></div>
<div id="case" role="dialog" aria-modal="true" aria-label="The piece"><div class="dim"></div><div class="pn">
  <div class="bar"><span class="k" id="csk"></span><div class="x"><button type="button" id="csprev" aria-label="Previous piece">{CHEV_L}</button><button type="button" id="csnext" aria-label="Next piece">{CHEV_R}</button><button type="button" id="csclose" aria-label="Close">{CLOSE}</button></div></div>
  <div class="cg"><div class="cart" id="csart"></div><div id="csbody"></div></div>
</div></div>
<div id="lb" role="dialog" aria-modal="true" aria-label="Plate viewer"><div class="bar"><span><b id="lbsite"></b> · <span id="lbgroup"></span></span><div class="x"><button type="button" id="lbzoom" aria-label="Zoom">{ZOOM}</button><button type="button" id="lbclose" aria-label="Close">{CLOSE}</button></div></div>
 <div class="st" id="lbst"><img id="lbA" alt=""><img id="lbB" alt=""><button type="button" class="nav p" id="lbprev" aria-label="Previous plate">{CHEV_L}</button><button type="button" class="nav n" id="lbnext" aria-label="Next plate">{CHEV_R}</button></div>
 <div class="cap"><span class="c" id="lbcap"></span><span><span class="k" id="lbct"></span> · swipe or use the arrows · esc closes</span></div></div>
<div class="cur" id="cur"></div><div class="cur2" id="cur2" data-l="View"></div>'''

# ---------------------------------------------------------------- welcome
def welcome():
    return f'''
<section id="welcome" aria-label="Welcome">
 <div class="glow"></div><div class="spot"></div>
 <div class="wrap w-g">
  <div class="w-copy">
   <div class="eyebrow">Mizan Qist Private Office · By invitation</div>
   <h1 class="w-name" id="wname"><span class="l1" id="wgreet">Welcome back,</span><span class="l2 t-1">{name_markup(CLIENT_SHORT + ".")}<span class="sr">{esc(CLIENT_SHORT)}.</span></span></h1>
   <p class="w-sub lede">Your office is open. Two wings tonight: ten residences in Abuja and Lagos, and ten pieces in the vault, every one of them sourced to your name.</p>
   <div class="w-cta">{btn("The residences", "#residences", "solid", 'data-go="residences"')}{btn("Open the vault", "#vault", "", 'data-go="vault"')}</div>
   <div class="w-meta">
    <div><b>10</b>Residences</div><div><b>10</b>Pieces in the vault</div><div><b>2</b>Cities</div><div><b>{esc(AGENT_INITIALS)}<small>at any hour</small></b>{esc(AGENT)}</div>
   </div>
  </div>
  <div class="card-stage" id="stage">
   <div class="mcard" id="mcard" aria-label="Your membership card">
    <div class="face"><div class="brush"></div><div class="sheen"></div><div class="glare"></div><div class="rim"></div></div>
    <div class="lay">
     <div class="row"><div class="house"><b>Mizan Qist</b>Private Office</div><div class="tier">By invitation</div></div>
     <div class="chip" aria-hidden="true"></div>
     <div class="emb"><div class="nm">{esc(CLIENT_CARD)}</div><div class="ln"><span>Member since<b>{esc(MEMBER_SINCE)}</b></span><span>Office<b>Abuja · London</b></span><span>Agent<b>{esc(AGENT_INITIALS)}</b></span></div></div>
    </div>
    <div class="sig">{MARK}</div>
   </div>
   <div class="card-note">The card answers to your hand · tilt it</div>
  </div>
 </div>
</section>'''

# ---------------------------------------------------------------- brief
def brief():
    return f'''
<section class="pg" id="brief" data-shade="paper" data-tab="brief" aria-label="Your brief">
 <div class="wrap">
  <div class="rv"><div class="eyebrow">Your brief</div><h2 class="t-2" style="margin-top:18px">A private office, not a brochure.</h2></div>
  <div class="brief-g" style="margin-top:clamp(40px,6vh,64px)">
   <div class="letter rv">
    <p class="sal">{esc(CLIENT_SALUTATION)}</p>
    <p>This office is yours alone. Nothing in it is on the open market in the form you see it here, and nothing in it was assembled for anyone else. Two wings are open: ten residential addresses across Abuja and Victoria Island, each with its price, its drawings and our honest view; and a vault of ten pieces from five houses, which we will source to your name once you tell us which of them you want on your wrist.</p>
    <p>Mark whatever interests you with the star. Your requests gather on your desk, and one message from there puts me to work: a viewing at the hour you choose, the full drawings, a valuation, or a piece secured with its box and papers. I am on retainer to you, not to any developer or dealer, so the view you read on every page is the one I would give you across a table.</p>
    <p>The office stays open. As new addresses and new pieces reach us, they are added here first.</p>
    <div class="sig"><b>{esc(AGENT_FIRST)}</b><span>{esc(AGENT)} · {esc(AGENT_ROLE)}</span></div>
   </div>
   <div class="rv">
    <div class="how">
     <div><b>I</b><div><h3>You mark</h3><p>Star an address or a piece anywhere in the office. The list is kept on this device and no one else sees it.</p></div></div>
     <div><b>II</b><div><h3>We source</h3><p>Viewings, drawings, valuations and title searches for the residences; provenance, papers and a price for each piece.</p></div></div>
     <div><b>III</b><div><h3>We complete</h3><p>Offers, contracts and handover; and where you choose a carcass or a new build, the design and finishing to follow.</p></div></div>
    </div>
    <div class="terms">
     <span><b>Selling</b> built or nearly so, available now</span><span><b>Off-plan</b> bought from the drawings, before completion</span><span><b>Carcass</b> structure and shell, finishing to your taste</span><span><b>BQ</b> boys' quarters, the staff annexe</span><span><b>On application</b> priced once the piece is secured</span><span><b>Box and papers</b> full set, no exceptions</span>
    </div>
   </div>
  </div>
 </div>
</section>'''

# ---------------------------------------------------------------- wing I
def wing(rn, eyebrow, title, desc, fill=False):
    return f'<div class="wing rv-stag"><div class="rn{" fill" if fill else ""}">{rn}</div><div><div class="eyebrow">{eyebrow}</div><h2 class="t-2">{title}</h2></div><p class="desc">{desc}</p></div>'

def residences():
    n_sell = sum(1 for x in SITES if x["status"] == "Selling"); n_off = sum(1 for x in SITES if x["status"] == "Off-plan")
    assert n_sell + n_off == len(SITES), "a status other than Selling / Off-plan needs its own tile"
    districts = len({(x["district"], x["city"]) for x in SITES})
    lo = min(x["pmin"] for x in SITES if x["pmin"]); hi = max(x["pmax"] for x in SITES if x["pmax"])
    fmt = lambda m: f"₦{m/1000:g}bn" if m >= 1000 else f"₦{m:g}m"
    cards = ""
    for i, s in enumerate(SITES):
        hero = s["hero"][0]
        pl = f'<div class="in">{img(hero + ".jpg", esc(s["name"]), "(max-width:900px) 70vw, 24vw", LAZY if i > 2 else "")}</div>' if hero else '<div class="dg">' + diagram_mini() + '</div>'
        cards += f'''<a class="card" href="#{s["id"]}" data-go="{s["id"]}"><div class="pl">{pl}<span class="k">{s["n"]}</span>{chip(s["status"])}</div>
<div class="nm">{esc(s["name"])}<small>{esc(s["district"])}{", Lagos" if s["city"]=="Lagos" else ""}</small></div><div class="pr"><span>{esc(s["short"])}</span><b>{esc(s["price"])}</b></div></a>'''
    return f'''
<section class="pg" id="residences" data-tab="residences" aria-label="Wing I, the residences">
 <div class="wrap">
  {wing("I", "Wing I", "The residences.", f"Ten addresses across {districts} districts and two cities, with the price, the drawings and our view on each. In the order we would show them.")}
  <div class="stats rv-stag">
    <div><div class="v num"><span data-count="10">10</span></div><div class="k">Addresses</div></div>
    <div><div class="v num"><span data-count="{districts}">{districts}</span></div><div class="k">Districts</div></div>
    <div><div class="v rng">{fmt(lo)}<small>to</small>{fmt(hi)}</div><div class="k">Price range</div></div>
    <div><div class="v num"><span data-count="{n_sell}">{n_sell}</span><small>·</small><span data-count="{n_off}">{n_off}</span></div><div class="k">Selling · off-plan</div></div>
  </div>
  <div class="shelf-h rv"><div><div class="eyebrow">The collection</div><h3 class="t-3">Ten dossiers, in order.</h3></div><div class="arrows"><button type="button" data-shelf="-1" aria-label="Scroll the collection left">{CHEV_L}</button><button type="button" data-shelf="1" aria-label="Scroll the collection right">{CHEV_R}</button></div></div>
  <div class="shelf rv" id="shelf">{cards}</div>
 </div>
</section>'''

LANDMARKS = [
 dict(id="cbd", n="Central Business District", s="Central Bank of Nigeria, Tafawa Balewa Way", ll=[9.0508926, 7.4929880], city="Abuja", dest=True),
 dict(id="hilton", n="Transcorp Hilton", s="Zambezi Crescent, Maitama", ll=[9.074966, 7.494881], city="Abuja"),
 dict(id="assembly", n="National Assembly", s="Three Arms Zone", ll=[9.068124, 7.511193], city="Abuja"),
 dict(id="wuse", n="Wuse Market", s="Wuse Market Road", ll=[9.068555, 7.465938], city="Abuja"),
 dict(id="jabi", n="Jabi Lake Mall", s="Jabi", ll=[9.076275, 7.42548], city="Abuja"),
 dict(id="aso", n="Aso Rock", s="The Presidential Villa below it", ll=[9.08039, 7.536039], city="Abuja"),
 dict(id="eko", n="Eko Hotel & Suites", s="Adetokunbo Ademola Street, Victoria Island", ll=[6.427074, 3.430286], city="Lagos", dest=True),
]
ROUTES = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "routes.json")))
def map_data():
    return [dict(id=x["id"], n=x["n"], name=x["name"], addr=x["addr"], price=x["price"], status=x["status"], ll=list(x["ll"]) if x["ll"] else None, gmaps=x["gmaps"], approx=x["approx"], city=x["city"], district=x["district"], route=ROUTES.get(x["id"])) for x in SITES]

def glance():
    ORDER = ["Maitama", "Wuse II", "Katampe Ext.", "Mabushi District", "Guzape", "Asokoro", "Victoria Island, Lagos"]
    groups = [(g, []) for g in ORDER]
    for x in SITES:
        dict(groups)[x["district"] + (", Lagos" if x["city"] == "Lagos" else "")].append(x)
    panel = ""
    for g, items in groups:
        rows = ""
        for x in items:
            r = ROUTES.get(x["id"], {})
            dist = f'<span class="dist"><b>{r["km"]}</b> km · <b>{r["min"]}</b> min</span>' if r else '<span class="dist">—</span>'
            rows += f'<button type="button" class="mrow" data-m="{x["id"]}" aria-pressed="false"><span class="k">{x["n"]}</span><span class="t">{esc(x["name"])}<small>{esc(x["addr"])}{" · approximate" if x["approx"]=="district" else " · nearest pin" if x["approx"]=="nearest" else ""}</small></span>{dist}</button>'
        panel += f'<div class="lm-grp"><div class="lm-gh"><span>{esc(g)}</span><span>{len(items)} {"address" if len(items)==1 else "addresses"}</span></div>{rows}</div>'
    fallback = "".join(f'<a href="{esc(x["gmaps"])}" target="_blank" rel="noopener"><span class="k">{x["n"]}</span><span>{esc(x["name"])}<small>{esc(x["addr"])}</small></span><span class="d">Google Maps</span></a>' for x in SITES)
    return f'''
<section class="pg" id="glance" data-shade="carbon" data-tab="residences" aria-label="Map and ledger">
 <div class="wrap">
  <div class="map-h rv" style="margin-top:0"><div><div class="eyebrow">The map</div><h3 class="t-3">Every address, and the drive to the centre, <em class="t-i">on one map.</em></h3></div>
   <div class="map-ctl"><div class="seg" role="group" aria-label="Map layer"><button type="button" data-layer="streets" aria-pressed="true">Streets</button><button type="button" data-layer="aerial" aria-pressed="false">Aerial</button></div><div class="seg" role="group" aria-label="View"><button type="button" data-city="Maitama" aria-pressed="false">Maitama</button><button type="button" data-city="Abuja" aria-pressed="true">Abuja</button><button type="button" data-city="Lagos" aria-pressed="false">Lagos</button></div></div></div>
  <div class="map-g">
   <div class="lmap-wrap night rv" id="lmapwrap"><div id="lmap" aria-label="Interactive map of the ten addresses"></div><div class="lm-hint" id="lmhint">Click the map, then scroll to zoom</div>
    <div class="map-fb" id="mapfb" hidden><div class="eyebrow plain">Map</div><p>The map could not load here. Each address opens in Google Maps:</p><div class="fbrows">{fallback}</div></div></div>
   <div class="lm-panel rv" id="mrows">{panel}<div class="lm-note">Distances are by road to the Central Business District (the Central Bank of Nigeria on Tafawa Balewa Way), routed on OpenStreetMap; Cova Manor is measured to the Eko Hotel. Drive times are approximate and off-peak. Choose a row to fly to the address and draw its route.</div></div>
  </div>
  {ledger()}
 </div>
</section>'''

STATUS_ORDER = {"Ready": 0, "Selling": 1, "Off-plan": 2}
def ledger():
    rows = ""
    for s in SITES:
        types = " · ".join(t[0] for t in s["types"])
        availcell = "" if s["avail"] == "—" else '<span class="small"> · ' + esc(s["avail"]) + ' avail.</span>'
        rows += f'''<tr data-go="{s["id"]}" data-n="{s["n"]}" data-price="{s["pmin"] or 99999}" data-status="{STATUS_ORDER[s["status"]]}">
<td class="k">{s["n"]}</td><td class="nm">{esc(s["name"])}<small>{esc(s["addr"])}</small></td>
<td>{esc(types)}</td><td class="num">{esc(s["beds"])}</td><td class="num">{s.get("homes_cell") or (esc(s["units"]) + availcell)}</td><td class="pr">{esc(s["price"])}</td><td>{chip(s["status"])}</td><td class="vw">{esc(s["short"])}</td><td class="st">{star(s, s["name"])}</td></tr>'''
    return f'''
  <div class="ledger-h rv"><div><div class="eyebrow">The ledger</div><h2 class="t-2">Every address on one page.</h2></div>
   <div class="sorts" role="group" aria-label="Sort the ledger"><button type="button" class="on" data-sort="n">In order</button><button type="button" data-sort="price">By price</button><button type="button" data-sort="status">By status</button></div></div>
  <div class="ledger-w rv"><table class="ledger" id="ledger"><thead><tr><th>No.</th><th>Address</th><th>House types</th><th>Beds</th><th>Homes</th><th>Price</th><th>Status</th><th>In a line</th><th class="st">Request</th></tr></thead><tbody>{rows}</tbody></table></div>'''

# ---------------------------------------------------------------- dossiers
def diagram_svg(cls="diagram"):
    return f'''<div class="{cls}" aria-label="Illustrative plot diagram for Mississippi Street">
<svg viewBox="0 0 100 68" role="img">
 <defs><pattern id="hx" width="1.6" height="1.6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="1.6" stroke="rgba(205,176,122,.55)" stroke-width=".25"/></pattern></defs>
 <line class="road" x1="4" y1="60" x2="96" y2="60"/><line class="road" x1="4" y1="63" x2="96" y2="63"/>
 <text class="s" x="50" y="66.6" text-anchor="middle">Mississippi Street</text>
 <path class="b" d="M16 8 L84 8 L86 54 L14 54 Z"/>
 <text class="s" x="16" y="6">Plot boundary · indicative</text>
 <rect class="hx" x="30" y="20" width="34" height="22"/>
 <text x="47" y="29.5" text-anchor="middle">Existing house</text>
 <text class="s" x="47" y="33.2" text-anchor="middle">5 bedrooms · to be cleared</text>
 <rect class="hx" x="68" y="14" width="12" height="9"/>
 <text class="s" x="74" y="27" text-anchor="middle">Guest chalet</text>
 <path class="nw" d="M20 13 L80 13 L80 50 L20 50 Z"/>
 <text class="r" x="22" y="47.6">Proposed new residence</text>
 <text class="s" x="22" y="51" style="fill:var(--champ-hi);opacity:.8">to your brief · footprint indicative</text>
 <g transform="translate(90 44)"><circle r="3.2" fill="none" stroke="rgba(233,231,225,.35)" stroke-width=".25"/><path d="M0-2.6 L1 1 L0 .2 L-1 1 Z" fill="var(--champ)"/><text class="s" y="6.2" text-anchor="middle">N</text></g>
</svg>
<div class="cap">Illustrative diagram · not a survey · not to scale</div></div>'''

def diagram_mini():
    return '<svg viewBox="0 0 100 68" aria-hidden="true"><defs><pattern id="hx2" width="1.6" height="1.6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="1.6" stroke="rgba(205,176,122,.6)" stroke-width=".25"/></pattern></defs><path d="M16 8 L84 8 L86 54 L14 54 Z" fill="none" stroke="#cdb07a" stroke-width=".4" stroke-dasharray="1.4 1"/><rect x="30" y="20" width="34" height="22" fill="url(#hx2)" stroke="rgba(233,231,225,.4)" stroke-width=".25"/><path d="M20 13 L80 13 L80 50 L20 50 Z" fill="none" stroke="#efdfb8" stroke-width=".45" stroke-dasharray=".4 1.2" stroke-linecap="round"/></svg>'

def facts_html(s):
    out = ""
    for k, v, u in s["facts"]:
        unit = f'<small>{esc(u)}</small>' if u and len(u) <= 6 else (f'<small class="b">{esc(u)}</small>' if u else "")
        out += f'<div><dt>{esc(k)}</dt><dd>{esc(v)}{unit}</dd></div>'
    return f'<dl class="facts">{out}</dl>'

def types_html(s):
    rows = ""
    for name, spec, size, avail, price in s["types"]:
        off = price in ("Sold out", "Not listed", "On application", "By request")
        rows += f'<tr><td class="t">{esc(name)}<small>{esc(spec)}</small></td><td>{esc(size) or "—"}</td><td class="n">{esc(avail) or "—"}</td><td class="p{" off" if off else ""}">{esc(price)}</td></tr>'
    return f'<div class="types-w"><table class="types"><thead><tr><th>Type</th><th>Size</th><th class="n">Available</th><th class="p">Price</th></tr></thead><tbody>{rows}</tbody></table></div>'

def credits_html(s):
    lines = []
    if s["dev"]: lines.append(f'<span><b>Developer</b> · {esc(s["dev"])}</span>')
    if s["arch"]: lines.append(f'<span><b>Architect</b> · {esc(s["arch"])}</span>')
    src = "Mizan Qist residential portfolio, August 2026"
    if s["name"] == "Maitama View": src += "; Maitama View brochure and working drawings; gate design drawings, September 2026"
    if s["name"] == "Cova Manor": src += "; Cova Manor brochure and construction documentation"
    if s["name"] == "Heights 777": src += "; Heights 777 brochure and drawings"
    lines.append(f'<span><b>Source</b> · {esc(src)}</span>')
    return f'<div class="credits">{"".join(lines)}</div>'

def plate_html(s, cls):
    src, kind, cap = s["hero"]
    sizes = "100vw" if cls == "wide" else "(max-width:900px) 100vw, 45vw"
    return f'<div class="plate {cls} wipe" data-lb="{s["id"]}" data-src="assets/{src}.jpg" role="button" tabindex="0" aria-label="Open the visualisation of {esc(s["name"])}"><div class="pi">{img(src + ".jpg", esc(cap), sizes, LAZY)}</div><div class="cap"><span>{esc(cap)}</span></div></div>'

def gallery_html(s):
    if not s["gallery"]: return ""
    groups = []
    for g, _, _ in s["gallery"]:
        if g not in groups: groups.append(g)
    figs = ""
    for g, src, cap in s["gallery"]:
        plan = " plan" if src.startswith("cova-plan") or src in ("kat-plan2",) else ""
        ext = "png" if src.startswith("cova-plan") else "jpg"
        figs += f'<figure class="gi{plan}" data-g="{esc(g)}" data-lb="{s["id"]}" data-src="assets/{src}.{ext}" data-cap="{esc(cap)}" tabindex="0" role="button" aria-label="Open {esc(cap)}">{img(src + "." + ext, esc(cap), "(max-width:900px) 46vw, 14vw", LAZY)}<span class="g">{esc(g)}</span><figcaption>{esc(cap)}</figcaption></figure>'
    btns = '<button type="button" class="on" data-g="*">All</button>' + "".join(f'<button type="button" data-g="{esc(g)}">{esc(g)}</button>' for g in groups)
    n = len(s["gallery"])
    return f'<div class="gal-h rv"><div class="eyebrow">Plates · {n} {"view" if n==1 else "views"}</div><div class="groups" role="group" aria-label="Filter the plates">{btns}</div></div><div class="gal rv-stag">{figs}</div>'

def dossier(s, shade, flip):
    n = s["n"]; kind = s["hero"][1]
    availtxt = "Availability on request" if s["avail"] == "—" else "<b>" + esc(s["avail"]) + "</b> available"
    units = s.get("units_line") and f'<span>{s["units_line"]}</span>' or f'<span><b>{esc(s["units"])}</b> {"home" if s["units"]=="1" else "homes"} in the scheme</span><span>{availtxt}</span>'
    pin = " · nearest pin" if s["approx"] == "nearest" else " · street" if s["approx"] == "street" else " · district, approximate" if s["approx"] == "district" else ""
    head = f'''<div class="head rv-stag">
    <div><div class="eyebrow">{esc(s["street"])}{(" · " + esc(s["plot"])) if s["plot"] else ""}</div><h2 class="nm">{esc(s["name"])}</h2>{f'<p class="sc">{esc(s["scheme"])}</p>' if s["scheme"] else ""}
      <div class="addr"><span><b>{esc(s["addr"])}</b></span>{units}<a class="gm" href="{esc(s["gmaps"])}" target="_blank" rel="noopener">Open in Google Maps{pin} {ARROW}</a></div></div>
    <div class="pr"><div class="v">{esc(s["price"])}</div><div class="k">{"Price band" if "–" in s["price"] else "Price"} · {esc(s["beds"])} bedrooms</div></div></div>'''
    left = facts_html(s) + types_html(s)
    view = f'<div class="view"><div class="eyebrow">Our view</div><p>{esc(s["view"])}</p></div>'
    if s["name"] == "Mississippi":
        view += '''<div class="reco rv"><div class="eyebrow">Recommendation</div><div class="t">Best use: demolition and new construction.</div><p>Buy the plot for its street and its ground. Clear the existing house and chalet, and build a new residence to your brief, rather than renovate a building that has reached the end of its life. Mizan Qist is in construction and can take on the project, from design to handover.</p></div>
<div class="steps"><div><b>I</b><span>A private viewing, arranged with the owner's consent and at a time of his choosing.</span></div><div><b>II</b><span>A survey of the plot and a search of the title before any offer.</span></div><div><b>III</b><span>A concept design for the new residence, so that the purchase and the build are priced together.</span></div></div>'''
    right = view + credits_html(s)
    if kind == "wide":
        body = f'{plate_html(s, "wide")}<div class="body"><div class="rv">{left}</div><div class="rv">{right}</div></div>'
    elif kind == "diagram":
        body = f'<div class="body split{" flip" if flip else ""}"><div class="sticky rv">{diagram_svg()}</div><div class="rv">{left}{right}</div></div>'
    else:
        pcls = {"split": "sp", "tall": "tall"}.get(kind, "sp")
        if s["name"] == "Cova Manor": pcls = "sq"
        body = f'<div class="body split{" flip" if flip else ""}"><div class="sticky">{plate_html(s, pcls)}</div><div class="rv">{left}{right}</div></div>'
    return f'''
<section class="pg dz" id="{s["id"]}" data-shade="{shade}" data-tab="residences" data-n="{n}" data-name="{esc(s["name"])}" aria-label="Dossier {n}, {esc(s["name"])}">
 <div class="wrap">
  <div class="run rv"><div>Dossier {n} / 10</div><div class="c">{esc(s["district"])} · {esc(s["city"])}</div><div class="r">{chip(s["status"])}{star(s, s["name"])}</div></div>
  {head}
  {body}
  {gallery_html(s)}
  <div class="foot"><span>Prepared for {esc(CLIENT)} · Mizan Qist Private Office</span><span><b>{n}</b> / 10</span></div>
 </div>
</section>'''

# ---------------------------------------------------------------- wing II · the vault
def vault():
    houses = '<button type="button" class="on" data-h="*">All ten</button>' + "".join(f'<button type="button" data-h="{esc(h)}">{esc(h)}</button>' for h in HOUSES)
    cards = ""
    for w in WATCHES:
        spec = {k: w[k] for k in ("n", "house", "model", "ref", "case", "dial", "movement", "reserve", "water", "strap", "year", "condition", "price", "status", "view", "placeholder", "image")}
        art = img(w["image"], f'{esc(w["house"])} {esc(w["model"])}', "(max-width:900px) 90vw, 30vw", LAZY) if w["image"] else watch_svg(w["art"])
        ph = ('<span class="ph">To be sourced</span>' if w["image"] else '<span class="ph">Blueprint · to be sourced</span>') if w["placeholder"] else ""
        cards += f'''<div class="piece rv" id="{w["id"]}" data-id="{w["id"]}" data-house="{esc(w["house"])}" data-spec="{esc(json.dumps(spec, ensure_ascii=False))}" role="button" tabindex="0" aria-label="Open piece {w["n"]}, {esc(w["house"])} {esc(w["model"])}">
 <div class="art">{art}{ph}<span class="rn">{w["n"]}</span></div>
 <div class="meta"><div class="hs">{esc(w["house"])}</div><div class="md">{esc(w["model"])}</div><div class="rf">{esc(w["ref"])}</div>
  <div class="ft"><span class="pr">{esc(w["price"])}</span>{star(w, w["house"] + " " + w["model"])}</div></div>
</div>'''
    return f'''
<section class="pg" id="vault" data-tab="vault" aria-label="Wing II, the vault">
 <div class="wrap">
  {wing("II", "Wing II", "The vault.", "Ten pieces from five houses, chosen for a wrist that moves between the site, the boardroom and the evening. Each is sourced to your name, with box and papers, once you ask for it.", fill=True)}
  <div class="rv"><div class="eyebrow">By house</div><div class="houses" role="group" aria-label="Filter the vault by house">{houses}</div></div>
  <div class="vgrid">{cards}</div>
  <div class="v-note rv">{SEAL}<p><b>Shown as the makers show them.</b> The photographs are the houses' own catalogue images of each reference. Every entry stays a placeholder until the piece is secured: the year, the condition, the price and our own photograph of the watch in hand replace the catalogue entry then. Open any piece for its full sheet, and reserve it to add it to your requests.</p></div>
 </div>
</section>'''

# ---------------------------------------------------------------- desk
def desk():
    intents = [("a private viewing", "A viewing"), ("the full drawings", "The drawings"), ("a valuation", "A valuation"), ("the pieces to be sourced", "Source the pieces"), ("a call at your convenience", "A call")]
    ib = "".join(f'<button type="button" data-i="{esc(v)}" aria-pressed="{"true" if i==0 else "false"}">{esc(l)}</button>' for i, (v, l) in enumerate(intents))
    return f'''
<section class="pg" id="desk" data-shade="carbon" data-tab="desk" aria-label="Your desk">
 <div class="wrap">
  <div class="rv"><div class="eyebrow">Your desk</div><h2 class="t-2" style="margin-top:18px">Open at any hour.</h2><p class="lede" style="margin-top:22px">Everything in this office can be set in motion with one message. {esc(AGENT)} holds your file and answers it personally.</p></div>
  <div class="desk-g">
   <div class="rv">
    <div class="req"><div class="in">
     <div class="eyebrow">Your requests</div><h3 class="t-3">What you have marked.</h3>
     <ul id="reqlist"></ul><p class="empty" id="reqempty">Nothing marked yet. Star an address or reserve a piece and it appears here.</p>
     <div class="intent" role="group" aria-label="What would you like arranged">{ib}</div>
     <div class="prev" id="reqprev" aria-live="polite"></div>
     <div class="send">{btn("Send to " + AGENT_FIRST, "https://wa.me/447931814601", "solid", 'id="reqsend" target="_blank" rel="noopener"')}<span class="hint">Opens WhatsApp with the message above, ready to send.</span></div>
    </div></div>
   </div>
   <div class="rv">
    <div class="contacts">
     <a href="https://wa.me/message/CL4UJVGMQEHBK1?src=qr" target="_blank" rel="noopener"><span class="v">+44 7931 814601<small>Mizan Qist · United Kingdom</small></span><span class="chip">WhatsApp</span></a>
     <a href="tel:+2348086666206"><span class="v">+234 808 6666 206<small>Mizan Qist · Abuja</small></span><span class="chip">Call now</span></a>
     <a href="mailto:mizanqistltd@gmail.com?subject={urllib.parse.quote("Private office · " + CLIENT)}"><span class="v">mizanqistltd@gmail.com<small>Email</small></span><span class="chip">Write</span></a>
     <a href="https://www.instagram.com/mizanqistltd?stkn=MTNvcmwzc2F5MjVvMQ%3D%3D&amp;utm_source=qr" target="_blank" rel="noopener"><span class="v">@mizanqistltd<small>Instagram</small></span><span class="chip">Follow</span></a>
    </div>
    <div class="agent"><div class="av">{esc(AGENT_INITIALS)}</div><div><b>{esc(AGENT)}</b><span>{esc(AGENT_ROLE)}</span></div><div class="st"><i></i>On retainer · any hour</div></div>
    <div class="next">
     <div><b>I</b><div><h3>You mark</h3><p>The star on any dossier, ledger row or piece. Kept on this device; listed on the left.</p></div></div>
     <div><b>II</b><div><h3>We arrange</h3><p>Viewings, drawings and valuations for the residences; provenance, papers and pricing for the pieces, in the order you prefer.</p></div></div>
     <div><b>III</b><div><h3>We complete</h3><p>Offers, title checks and contracts; a piece delivered to your hand; and where you build, the design and finishing to follow.</p></div></div>
    </div>
   </div>
  </div>
  <div class="credit-g rv-stag">
   <div><div class="lg">{MARK}<span>Mizan Qist Limited<small>Where ideas become reality</small></span></div><p>Prepared by the Private Office of Mizan Qist Limited, Abuja, {esc(DATE)}. Personal agent: {esc(AGENT)}.</p></div>
   <div><b>Sources</b><p>Residences: prices, unit counts and statuses as quoted to Mizan Qist by the developers and owners, August and September 2026; site and drone photography by Mizan Qist; visualisations and plans supplied by the developers and their architects. Vault: makers' published specifications and catalogue photographs for the references named (Patek Philippe, Audemars Piguet, Cartier, Vacheron Constantin, Richard Mille), reproduced for this private presentation only and to be confirmed on each piece.</p></div>
   <div><b>Confidential</b><p>Prepared for {esc(CLIENT)} and not for onward circulation. Visualisations are artists' impressions; vault photographs are the makers' catalogue images and remain their property. Areas are indicative. Prices are subject to confirmation and to contract; nothing here forms part of an offer or contract.</p></div>
  </div>
  <div class="fin"><span>Prepared for {esc(CLIENT)} · Confidential · {esc(DATE)}</span><span class="seal">Mizan Qist · Private Office</span></div>
 </div>
</section>'''

# ---------------------------------------------------------------- build
def build():
    parts = [chrome(), welcome(), brief(), residences(), glance()]
    shade = "dark"; flip = False
    for s in SITES:
        parts.append(dossier(s, shade, flip))
        shade = "carbon" if shade == "dark" else "dark"
        if s["hero"][1] != "wide": flip = not flip
    parts += [vault(), desk()]
    content = "\n".join(parts)
    js = (JS.replace('__SLUG__', json.dumps(SLUG)).replace('__SIGNOFF__', json.dumps(CLIENT_SIGNOFF))
            .replace('__AGENT_FIRST__', json.dumps(AGENT_FIRST)).replace('__CLIENT_CARD__', json.dumps(CLIENT_CARD)))
    data = f'<script>window.MQ_MAP={json.dumps(map_data(), ensure_ascii=False)};window.MQ_LM={json.dumps(LANDMARKS, ensure_ascii=False)};</script>'
    head = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{esc(TITLE)}</title>
<meta name="description" content="The private office of {esc(CLIENT)}: ten residences in Abuja and Lagos and a vault of ten watches, prepared by Mizan Qist Limited.">
<meta name="robots" content="noindex,nofollow">
<meta name="theme-color" content="#08080a">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}">
<style>{CSS}</style>
</head>
<body>
'''
    page = head + content + f'\n{data}\n<script>{js}</script>\n</body>\n</html>\n'
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f: f.write(page)
    art = f'<title>{esc(TITLE)}</title>\n<style>{CSS}</style>\n<link rel="stylesheet" href="{FONTS}">\n' + content + f'\n{data}\n<script>{js}</script>\n'
    with open(os.path.join(ROOT, "tools", "artifact-src.html"), "w", encoding="utf-8") as f: f.write(art)
    print("index.html", len(page) // 1024, "KB")

if __name__ == "__main__":
    build()
