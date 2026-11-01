# Rewrites routes.json: the drive from Lantees Cafe (IBB Boulevard, Maitama) to every Abuja address, by road on OpenStreetMap.
# Lagos addresses keep their existing route (Cova Manor is measured to the Eko Hotel). Run: python3 tools/route_lantees.py
# OSRM's demo server is fetched with curl because Python's TLS handshake with it fails.
import json, os, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data import SITES

LANTEES = (9.1017855, 7.4887182)  # Google pin for Lantees Cafe, 3259 Ibrahim Babangida Blvd
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "routes.json")
TOL = 0.00035  # simplification tolerance in degrees, about 35 m

def simplify(pts, tol):
    """Douglas-Peucker on [lat, lon] pairs."""
    if len(pts) < 3: return pts
    (y1, x1), (y2, x2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; n = (dx * dx + dy * dy) ** .5 or 1e-12
    far, i_far = 0, 0
    for i, (y, x) in enumerate(pts[1:-1], 1):
        d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / n
        if d > far: far, i_far = d, i
    if far <= tol: return [pts[0], pts[-1]]
    return simplify(pts[:i_far + 1], tol)[:-1] + simplify(pts[i_far:], tol)

def drive(a, b):
    url = f"https://router.project-osrm.org/route/v1/driving/{a[1]},{a[0]};{b[1]},{b[0]}?overview=full&geometries=geojson"
    r = json.loads(subprocess.run(["curl", "-s", "-m", "30", url], capture_output=True, text=True, check=True).stdout)
    if r.get("code") != "Ok": raise RuntimeError(f"OSRM: {r.get('code')} {r.get('message', '')}")
    rt = r["routes"][0]
    line = [[round(lat, 5), round(lon, 5)] for lon, lat in rt["geometry"]["coordinates"]]
    return dict(km=round(rt["distance"] / 1000, 1), min=max(1, round(rt["duration"] / 60)), line=simplify(line, TOL))

routes = json.load(open(OUT))
for s in SITES:
    if s["city"] != "Abuja" or not s["ll"]: continue
    routes[s["id"]] = drive(LANTEES, s["ll"]); time.sleep(1)
    print(s["id"], s["name"], routes[s["id"]]["km"], "km", routes[s["id"]]["min"], "min", len(routes[s["id"]]["line"]), "points")
live = {s["id"] for s in SITES}
json.dump({k: v for k, v in routes.items() if k in live}, open(OUT, "w"))
