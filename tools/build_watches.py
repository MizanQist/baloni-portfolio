# Makes assets/w01-…w10-*.jpg for the vault from the makers' own catalogue photographs (URLs in watch_sources.json).
# Each source is cut out (transparent PNGs as they are; white-ground JPEGs by flood fill from the corners), centred at a
# uniform scale and laid on the vault's flat black (#050506) at 1200 x 1344, the aspect of the piece cards.
# Run: python3 tools/build_watches.py [source_dir]   (source_dir defaults to tools/watch-src; missing files are downloaded)
import io, json, os, sys, urllib.request
from PIL import Image, ImageDraw, ImageFilter, ImageChops

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "tools", "watch-src")
OUT = os.path.join(ROOT, "assets")
W, H = 1200, 1344
BG = (5, 5, 6)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
SOURCES = json.load(open(os.path.join(ROOT, "tools", "watch_sources.json")))

def fetch(entry):
    path = os.path.join(SRC, entry["file"])
    if not os.path.exists(path):
        os.makedirs(SRC, exist_ok=True)
        data = urllib.request.urlopen(urllib.request.Request(entry["url"], headers={"User-Agent": UA}), timeout=120).read()
        open(path, "wb").write(data)
    return Image.open(path)

def cutout_light(im, thresh=48, erode=2, shadow=False, texture=0):
    """flood-fill the pale studio ground from the four corners, then erode and feather the edge so no white fringe survives.
    shadow=True also removes the soft drop shadow: bright, neutral pixels that touch the ground (safe for gold cases and
    leather straps; not for steel, which is bright and neutral itself). texture=N (odd) keeps only textured regions instead"""
    rgb = im.convert("RGB"); w, h = rgb.size
    fill = rgb.copy(); key = (255, 0, 255)
    corners = ((0, 0), (w - 1, 0), (0, h - 1), (w - 1, h - 1), (w // 2, 0), (w // 2, h - 1), (0, h // 2), (w - 1, h // 2))
    for pt in corners:
        if fill.getpixel(pt) != key: ImageDraw.floodfill(fill, pt, key, thresh=thresh)
    mask = Image.eval(ImageChops.difference(fill, Image.new("RGB", (w, h), key)).convert("L"), lambda v: 255 if v > 0 else 0)  # 255 = watch
    if shadow:
        lum = rgb.convert("L"); r, g, b = rgb.split()
        hi = Image.eval(ImageChops.lighter(ImageChops.lighter(r, g), b), lambda v: v); lo = ImageChops.darker(ImageChops.darker(r, g), b)
        sat = ImageChops.subtract(hi, lo)
        cand = ImageChops.multiply(lum.point(lambda v: 255 if v > 150 else 0), sat.point(lambda v: 255 if v < 22 else 0))  # bright and neutral
        walk = ImageChops.lighter(ImageChops.invert(mask), cand)  # 255 where the fill may travel: the ground, and shadow-like pixels
        walk = walk.point(lambda v: 255 if v > 127 else 0)
        for pt in corners:
            if walk.getpixel(pt) == 255: ImageDraw.floodfill(walk, pt, 128)
        reached = walk.point(lambda v: 255 if v == 128 else 0)
        mask = ImageChops.subtract(mask, reached)
    if texture:
        # steel is as bright and neutral as a shadow, so keep only what has texture: edges dilated, with enclosed holes filled
        edges = rgb.convert("L").filter(ImageFilter.FIND_EDGES).point(lambda v: 255 if v > 22 else 0)
        core = edges.filter(ImageFilter.MaxFilter(texture))
        walk = ImageChops.invert(core)
        for x, y in corners:  # seed inside the frame: FIND_EDGES marks the image border itself
            pt = (min(max(x, 24), w - 25), min(max(y, 24), h - 25))
            if walk.getpixel(pt) == 255: ImageDraw.floodfill(walk, pt, 128)
        filled = ImageChops.lighter(core, walk.point(lambda v: 255 if v == 255 else 0))  # the core plus every hole inside it
        mask = ImageChops.multiply(mask, filled)
    for _ in range(erode): mask = mask.filter(ImageFilter.MinFilter(3))
    mask = mask.filter(ImageFilter.GaussianBlur(1.2))
    out = rgb.convert("RGBA"); out.putalpha(mask); return out

def lift_black(im, floor=BG):
    """a photograph on true black: raise its black point to the vault's ground so the plate has no visible edge"""
    rgb = im.convert("RGB")
    r, g, b = rgb.split()
    r = r.point(lambda v: max(v, floor[0])); g = g.point(lambda v: max(v, floor[1])); b = b.point(lambda v: max(v, floor[2]))
    out = Image.merge("RGB", (r, g, b)).convert("RGBA"); return out

def place(cut, scale, dy=0.0, ground=True):
    """centre the cut-out on the plate; scale = fraction of the plate width the watch's bounding box takes"""
    bbox = cut.getbbox() if ground else None
    if bbox: cut = cut.crop(bbox)
    cw, ch = cut.size
    s = min(W * scale / cw, H * 0.86 / ch)
    cut = cut.resize((max(1, round(cw * s)), max(1, round(ch * s))), Image.LANCZOS)
    plate = Image.new("RGBA", (W, H), BG + (255,))
    plate.alpha_composite(cut, ((W - cut.width) // 2, round((H - cut.height) / 2 + dy * H)))
    return plate.convert("RGB")

def build():
    made = []
    for wid, e in SOURCES.items():
        im = fetch(e); kind = e.get("kind", "alpha")
        if kind == "alpha": cut = im.convert("RGBA")
        elif kind == "light": cut = cutout_light(im, e.get("thresh", 48), e.get("erode", 2), e.get("shadow", False), e.get("texture", 0))
        elif kind == "black":
            cut = lift_black(im)
        else: raise SystemExit("unknown kind " + kind)
        plate = place(cut, e.get("scale", 0.62), e.get("dy", 0.0), ground=(kind != "black"))
        if kind == "black":  # the photograph fills its own frame: fit by height instead, letterboxed on the same ground
            cw, ch = cut.size; s = min(W / cw, H / ch); fit = cut.resize((round(cw * s), round(ch * s)), Image.LANCZOS)
            plate = Image.new("RGB", (W, H), BG); plate.paste(fit.convert("RGB"), ((W - fit.width) // 2, (H - fit.height) // 2))
        name = f'{wid}-{e["slug"]}.jpg'; plate.save(os.path.join(OUT, name), "JPEG", quality=88, optimize=True, progressive=True)
        made.append(name); print(name, "from", e["file"], kind)
    return made

if __name__ == "__main__":
    build()
