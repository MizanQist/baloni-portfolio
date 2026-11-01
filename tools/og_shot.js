// Renders assets/og.jpg (1200 x 630), the link preview shown by WhatsApp, iMessage and the like.
// Serve the site root first (python3 -m http.server 8765), then: NODE_PATH=~/.local/node/lib/node_modules node tools/og_shot.js
// Needs the network for the Fontshare fonts. Re-run when the card or the client's name changes.
const path = require('path');
const { chromium } = require('playwright');
const OUT = path.join(__dirname, '..', 'assets', 'og.jpg');

(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  await p.goto('http://127.0.0.1:8765/', { waitUntil: 'networkidle' });
  await p.waitForTimeout(4500); // veil, name reveal and card entrance
  await p.evaluate(() => {
    for (const s of ['#isl', '.corner', '.progress', '.w-sub', '.w-cta', '.w-meta', '.card-note', '#cur', '#cur2']) document.querySelectorAll(s).forEach(e => e.style.display = 'none');
    document.querySelector('#wgreet').textContent = 'Prepared for';
    const w = document.querySelector('#welcome'); w.style.minHeight = '630px'; w.style.padding = '0';
    window.scrollTo(0, 0);
  });
  await p.waitForTimeout(600);
  await p.screenshot({ path: OUT, type: 'jpeg', quality: 84 });
  await b.close();
  console.log('wrote', OUT);
})();
