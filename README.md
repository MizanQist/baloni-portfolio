# The Baloni Private Office

A private, single-page office prepared by Mizan Qist Limited for Mr Ibrahim Baloni: Wing I, ten residential addresses (nine in Abuja, one in Victoria Island, Lagos); Wing II, a vault of ten watches from five houses (placeholders until each piece is secured). Static site: `index.html` + `assets/`, no build step needed to host it.

- `index.html` — the site (generated; see below)
- `assets/` — photographs, visualisations and plans (JPEG/PNG); `assets/m/` holds 1400 px phone editions; `assets/leaflet/` the map library
- `favicon.svg`, `robots.txt` (noindex), `.nojekyll` — for GitHub Pages
- `tools/client.py` — the client's name, card embossing and sign-off
- `tools/data.py` — every fact, price and caption: `SITES` (the residences) and `WATCHES` (the vault)
- `tools/build_site.py` — regenerates `index.html` from the data (`python3 tools/build_site.py`); design in `tools/site_css.py`, behaviour in `tools/site_js.py`, the vault's blueprint drawings in `tools/watch_art.py`
- `tools/build_artifact.py` — makes `tools/artifact.html`, a single-file preview with reduced images and packed map tiles inlined (`python3 tools/fetch_tiles.py` once, then `TILES_DIR=tools/tiles python3 tools/build_artifact.py`)
- `tools/build_mobile.py` — rebuilds `assets/m/`

## Filling in a watch

Each vault entry is a placeholder. When a piece is secured, edit its entry in `tools/data.py`: put the photograph in `assets/` and set `image="<file>.jpg"`, set `placeholder=False`, and fill in `ref`, `year`, `condition`, `price` and `status` (`Secured` shows as a filled chip). Rerun `build_site.py`.

This site is independent of the other clients' sites. Sources: Mizan Qist residential portfolio (August 2026), Maitama View and Cova Manor brochures, Heights 777 brochure, drone photography of 22 August 2026; makers' published specifications for the watch references named. Confidential; not for onward circulation.
