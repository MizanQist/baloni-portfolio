# Stylesheet for the Baloni Private Office. One visual world: titanium black, platinum, champagne. Imported by build_site.py.
CSS = r"""
:root{
  --void:#08080a; --carbon:#111114; --graphite:#1a1a1f; --slate:#232329;
  --platinum:#e9e7e1; --silver:#b4b3ad; --steel:#77787e; --steel-2:#4f5056;
  --champ:#cdb07a; --champ-hi:#efdfb8; --champ-lo:#8f7745;
  --paper:#ecebe6; --paper-2:#dfddd6; --ink:#141416; --ink-2:#55565c;
  --rule:rgba(233,231,225,.12); --rule-2:rgba(233,231,225,.07); --rule-champ:rgba(205,176,122,.35);
  --fd:"Bodoni Moda",Didot,"Bodoni 72",Georgia,serif;
  --fs:"Manrope",system-ui,-apple-system,"Segoe UI",sans-serif;
  --fm:"DM Mono","SF Mono",Menlo,Consolas,monospace;
  --ease:cubic-bezier(.32,.72,0,1); --ease-o:cubic-bezier(.16,1,.3,1); --ease-io:cubic-bezier(.77,0,.18,1);
  --gut:clamp(20px,5vw,80px); --wrap:1440px;
  --nav-z:120; --overlay-z:170; --veil-z:300; --cursor-z:400;
  color-scheme:dark;
}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
html,body{overflow-x:clip}
body{margin:0;background:var(--void);color:var(--platinum);font:400 16px/1.6 var(--fs);-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;min-height:100vh}
body.locked{position:fixed;left:0;right:0;width:100%;overflow:hidden}
body::before{content:"";position:fixed;inset:0;z-index:2;pointer-events:none;opacity:.055;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .6 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>");background-size:160px 160px}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
button:focus-visible,a:focus-visible,[tabindex]:focus-visible{outline:1.5px solid var(--champ-hi);outline-offset:4px}
::selection{background:var(--champ);color:var(--void)}
h1,h2,h3{margin:0;font-weight:400;text-wrap:balance}
p{margin:0}
dl,dd,dt,figure{margin:0}
table{border-collapse:collapse}
.wrap{max-width:var(--wrap);margin:0 auto;padding-inline:var(--gut)}
.num,.tnum{font-variant-numeric:tabular-nums}
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}

/* ------- type scale ------- */
.eyebrow{font:500 10.5px/1 var(--fs);letter-spacing:.26em;text-transform:uppercase;color:var(--champ);display:inline-flex;align-items:center;gap:12px}
.eyebrow::before{content:"";width:22px;height:1px;background:var(--champ);opacity:.7}
.eyebrow.plain::before{display:none}
.mono{font-family:var(--fm);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--silver)}
.t-1{font:400 clamp(2.6rem,6.2vw,6.4rem)/1 var(--fd);letter-spacing:-.015em;font-variation-settings:"opsz" 96}
.t-2{font:400 clamp(2rem,3.9vw,3.7rem)/1.06 var(--fd);letter-spacing:-.01em;font-variation-settings:"opsz" 72}
.t-3{font:400 clamp(1.5rem,2.4vw,2.2rem)/1.18 var(--fd);font-variation-settings:"opsz" 48}
.t-i{font-style:italic;font-weight:400}
.lede{font:300 clamp(1.05rem,1.45vw,1.3rem)/1.6 var(--fs);color:var(--silver);max-width:60ch}
.small{font-size:.8em;color:var(--steel)}
.pg{position:relative;padding-block:clamp(88px,12vh,160px)}
.pg[data-shade="carbon"]{background:var(--carbon)}
.pg[data-shade="paper"]{background:var(--paper);color:var(--ink);--rule:rgba(20,20,22,.14);--rule-2:rgba(20,20,22,.08);--silver:#4a4b50;--steel:#6d6e74;--platinum:#141416;--champ:#8f7745;--champ-hi:#7a6238;color-scheme:light}
.pg[data-shade="paper"] ::selection{background:var(--ink);color:var(--paper)}
.pg[data-shade="paper"] .t-1,.pg[data-shade="paper"] .t-2,.pg[data-shade="paper"] .t-3{color:var(--ink)}

/* ------- reveals ------- */
.rv{opacity:0;transform:translateY(28px);transition:opacity 1s var(--ease-o),transform 1.1s var(--ease-o)}
.rv.in{opacity:1;transform:none}
.rv-stag>*{opacity:0;transform:translateY(22px);transition:opacity .9s var(--ease-o),transform 1s var(--ease-o)}
.rv-stag.in>*{opacity:1;transform:none}
.rv-stag.in>*:nth-child(2){transition-delay:.08s}.rv-stag.in>*:nth-child(3){transition-delay:.16s}.rv-stag.in>*:nth-child(4){transition-delay:.24s}.rv-stag.in>*:nth-child(5){transition-delay:.32s}.rv-stag.in>*:nth-child(6){transition-delay:.4s}.rv-stag.in>*:nth-child(7){transition-delay:.48s}.rv-stag.in>*:nth-child(8){transition-delay:.56s}.rv-stag.in>*:nth-child(n+9){transition-delay:.64s}
.wipe{clip-path:inset(0 0 100% 0);transition:clip-path 1.3s var(--ease-io)}
.wipe.in{clip-path:inset(0 0 0 0)}

/* ------- buttons ------- */
.btn{display:inline-flex;align-items:center;gap:14px;padding:6px 6px 6px 24px;border-radius:999px;border:1px solid var(--rule-champ);font:600 11px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--platinum);transition:border-color .5s var(--ease),background .5s var(--ease),color .5s var(--ease),transform .5s var(--ease);position:relative;white-space:nowrap}
.btn i{width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:rgba(233,231,225,.08);transition:transform .6s var(--ease),background .5s var(--ease)}
.btn i svg{width:15px;height:15px}
.btn:hover{border-color:var(--champ);background:rgba(205,176,122,.08)}
.btn:hover i{transform:translate(2px,-1px) scale(1.06);background:var(--champ);color:var(--void)}
.btn:active{transform:scale(.98)}
.btn.solid{background:var(--platinum);color:var(--void);border-color:var(--platinum)}
.btn.solid i{background:rgba(8,8,10,.1)}
.btn.solid:hover{background:var(--champ-hi);border-color:var(--champ-hi);color:var(--void)}
.btn.solid:hover i{background:var(--void);color:var(--champ-hi)}
.btn.sm{padding:4px 4px 4px 16px;font-size:10px;gap:10px}
.btn.sm i{width:28px;height:28px}
.pg[data-shade="paper"] .btn{color:var(--ink);border-color:rgba(20,20,22,.25)}
.pg[data-shade="paper"] .btn i{background:rgba(20,20,22,.08)}
.pg[data-shade="paper"] .btn:hover{background:rgba(143,119,69,.1)}
.pg[data-shade="paper"] .btn:hover i{background:var(--ink);color:var(--paper)}
.link{font:600 10.5px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--champ);display:inline-flex;align-items:center;gap:10px;transition:gap .4s var(--ease),color .3s}
.link svg{width:14px;height:14px}
.link:hover{gap:16px;color:var(--champ-hi)}

/* ------- chips ------- */
.chip{display:inline-flex;align-items:center;gap:8px;font:600 9.5px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;padding:8px 12px;border-radius:999px;border:1px solid var(--rule);color:var(--silver);white-space:nowrap}
.chip i{width:6px;height:6px;border-radius:50%;background:currentColor}
.chip[data-s="Selling"]{color:var(--champ-hi);border-color:var(--rule-champ)}
.chip[data-s="Off-plan"]{color:var(--silver)}
.chip[data-s="To be sourced"]{color:var(--champ);border-color:var(--rule-champ)}
.chip[data-s="Secured"]{color:var(--void);background:var(--champ-hi);border-color:var(--champ-hi)}
.pg[data-shade="paper"] .chip{color:var(--ink-2);border-color:rgba(20,20,22,.2)}
.pg[data-shade="paper"] .chip[data-s="Selling"]{color:var(--champ-lo);border-color:rgba(143,119,69,.5)}

/* ------- veil ------- */
#veil{position:fixed;inset:0;z-index:var(--veil-z);background:var(--void);color:var(--platinum);display:grid;place-items:center;transition:opacity 1s var(--ease),visibility 0s 1s}
#veil.off{opacity:0;visibility:hidden;pointer-events:none}
#veil .in{display:grid;justify-items:center;gap:26px;text-align:center}
#veil .mark{width:52px;height:52px;color:var(--champ)}
#veil .mark svg{width:100%;height:100%}
#veil .ro{font-family:var(--fm);font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--silver);min-height:1.4em}
#veil .ro b{font-weight:500;color:var(--champ-hi)}
#veil .line{width:180px;height:1px;background:var(--rule);position:relative;overflow:hidden}
#veil .line i{position:absolute;inset:0;background:var(--champ);transform-origin:left;transform:scaleX(0)}
#veil .ct{font-family:var(--fm);font-size:10px;letter-spacing:.3em;color:var(--steel)}

/* ------- island nav ------- */
.isl{position:fixed;top:18px;left:50%;transform:translateX(-50%);z-index:var(--nav-z);display:flex;align-items:center;gap:4px;padding:5px;border-radius:999px;background:rgba(17,17,20,.78);border:1px solid var(--rule);backdrop-filter:blur(18px) saturate(1.2);-webkit-backdrop-filter:blur(18px) saturate(1.2);box-shadow:0 18px 50px rgba(0,0,0,.45),inset 0 1px 0 rgba(233,231,225,.06);opacity:0;translate:0 -12px;transition:opacity .9s var(--ease) .3s,translate .9s var(--ease) .3s}
body.ready .isl{opacity:1;translate:0 0}
.isl .brand{display:flex;align-items:center;gap:10px;padding:6px 14px 6px 8px;border-radius:999px;color:var(--platinum)}
.isl .brand svg{width:26px;height:26px;color:var(--champ)}
.isl .brand b{font:500 12px/1 var(--fd);letter-spacing:.14em;text-transform:uppercase}
.isl .brand small{display:block;font:500 8.5px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel);margin-top:4px}
.isl .sep{width:1px;height:22px;background:var(--rule);margin:0 4px}
.isl .tab{position:relative;padding:11px 16px;border-radius:999px;font:600 10.5px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--silver);transition:color .4s var(--ease)}
.isl .tab:hover{color:var(--platinum)}
.isl .tab.on{color:var(--void)}
.isl .ind{position:absolute;top:5px;left:0;height:calc(100% - 10px);border-radius:999px;background:var(--platinum);opacity:0;transition:left .6s var(--ease),width .6s var(--ease),opacity .4s;z-index:0}
.isl .tab{z-index:1}
.isl .tab .n{display:inline-block;min-width:16px;height:16px;line-height:16px;border-radius:999px;background:var(--champ);color:var(--void);font-size:9px;text-align:center;letter-spacing:0;margin-left:8px;padding:0 4px;vertical-align:middle;transition:transform .4s var(--ease-o)}
.isl .tab .n:empty{display:none}
.isl .tab .n.pop{animation:pop .5s var(--ease-o)}
.isl .clock{padding:0 16px 0 10px;font-family:var(--fm);font-size:10.5px;letter-spacing:.14em;color:var(--steel);white-space:nowrap}
.isl .clock b{font-weight:500;color:var(--silver)}
.progress{position:fixed;top:0;left:0;right:0;height:1px;z-index:var(--nav-z);pointer-events:none}
.progress i{display:block;height:100%;background:var(--champ);transform-origin:left;transform:scaleX(0)}
.corner{position:fixed;z-index:var(--nav-z);top:26px;font:500 9.5px/1.5 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel);mix-blend-mode:difference;opacity:0;transition:opacity 1s .6s}
body.ready .corner{opacity:1}
.corner.l{left:var(--gut)}.corner.r{right:var(--gut);text-align:right}
.corner b{display:block;color:var(--silver);font-weight:500}
@media (max-width:1180px){.corner{display:none}.isl .clock{display:none}}
@media (max-width:760px){
  .isl{top:auto;bottom:max(14px,env(safe-area-inset-bottom));left:12px;right:12px;transform:none;translate:0 12px;justify-content:space-between;padding:4px}
  body.ready .isl{translate:0 0}
  .isl .brand small{display:none}.isl .brand{padding:6px 4px 6px 6px}.isl .brand b{display:none}
  .isl .sep{display:none}
  .isl .tab{padding:12px 5px;font-size:9px;letter-spacing:.08em;flex:1;text-align:center}
  .isl .tab .n{margin-left:5px}
  body{padding-bottom:88px}
}

/* ------- welcome / the card ------- */
#welcome{position:relative;min-height:100svh;display:grid;align-items:center;padding-block:clamp(120px,16vh,180px) clamp(70px,9vh,110px);overflow:hidden;isolation:isolate}
#welcome .glow{position:absolute;inset:-20%;z-index:-1;background:radial-gradient(38% 40% at 68% 42%,rgba(205,176,122,.14),transparent 70%),radial-gradient(30% 30% at 22% 80%,rgba(233,231,225,.05),transparent 70%);pointer-events:none}
#welcome .spot{position:absolute;inset:0;z-index:-1;background:radial-gradient(520px circle at var(--mx,50%) var(--my,50%),rgba(205,176,122,.09),transparent 60%);pointer-events:none;opacity:0;transition:opacity 1.2s}
body.ready #welcome .spot{opacity:1}
.w-g{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(320px,.95fr);gap:clamp(32px,5vw,90px);align-items:center}
.w-copy .eyebrow{opacity:0;transform:translateY(10px);transition:opacity .9s var(--ease-o) .35s,transform .9s var(--ease-o) .35s}
body.ready .w-copy .eyebrow{opacity:1;transform:none}
.w-name{margin-top:26px;overflow:hidden}
.w-name .w{display:inline-block;white-space:nowrap;margin-right:.24em}
.w-name .ch{display:inline-block;opacity:0;transform:translateY(105%) rotate(4deg);transition:opacity .01s,transform 1s var(--ease-o);transition-delay:calc(.55s + var(--i) * 32ms)}
body.ready .w-name .ch{opacity:1;transform:none;transition:opacity .01s calc(.55s + var(--i) * 32ms),transform 1s var(--ease-o) calc(.55s + var(--i) * 32ms)}
.w-name.shine .ch{transition:none}
.w-name.shine .l2{background:linear-gradient(100deg,var(--platinum) 30%,var(--champ-hi) 50%,var(--platinum) 70%);background-size:220% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:shine 2.6s var(--ease) .1s 1}
@keyframes shine{from{background-position:120% 0}to{background-position:-120% 0}}
.w-name .l1{display:block;font:italic 400 clamp(1.4rem,2.4vw,2.2rem)/1.2 var(--fd);color:var(--silver);margin-bottom:8px}
.w-name .l2{display:block}
.w-sub{margin-top:28px;max-width:52ch;opacity:0;transform:translateY(14px);transition:opacity 1s var(--ease-o) 1.5s,transform 1s var(--ease-o) 1.5s}
.w-cta{display:flex;gap:14px;flex-wrap:wrap;margin-top:40px;opacity:0;transform:translateY(14px);transition:opacity 1s var(--ease-o) 1.75s,transform 1s var(--ease-o) 1.75s}
body.ready .w-sub,body.ready .w-cta{opacity:1;transform:none}
.w-meta{display:flex;gap:clamp(20px,3vw,44px);flex-wrap:wrap;margin-top:clamp(48px,7vh,80px);padding-top:26px;border-top:1px solid var(--rule);opacity:0;transition:opacity 1.2s 2.1s}
body.ready .w-meta{opacity:1}
.w-meta div{font:500 10px/1.5 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel)}
.w-meta b{display:block;font:400 clamp(1.3rem,1.8vw,1.7rem)/1.1 var(--fd);color:var(--platinum);letter-spacing:0;text-transform:none;margin-bottom:6px}
.w-meta b small{font:500 10px/1 var(--fs);letter-spacing:.2em;color:var(--champ);margin-left:8px;vertical-align:middle;text-transform:uppercase}

/* the card */
.card-stage{perspective:1600px;display:grid;place-items:center;padding:clamp(10px,3vw,40px) 0;opacity:0;transform:translateY(40px) scale(.96);transition:opacity 1.4s var(--ease-o) .9s,transform 1.6s var(--ease-o) .9s}
body.ready .card-stage{opacity:1;transform:none}
.mcard{position:relative;width:min(100%,520px);aspect-ratio:1.586;border-radius:22px;transform-style:preserve-3d;transform:rotateX(var(--rx,0deg)) rotateY(var(--ry,0deg));transition:transform .9s var(--ease-o);cursor:grab;touch-action:pan-y;will-change:transform;-webkit-tap-highlight-color:transparent}
.mcard.live{transition:transform .12s linear}
.mcard:active{cursor:grabbing}
.mcard .face{position:absolute;inset:0;border-radius:22px;overflow:hidden;background:linear-gradient(135deg,#1b1b1f 0%,#0c0c0e 45%,#141417 70%,#09090b 100%);box-shadow:0 40px 80px -20px rgba(0,0,0,.8),0 0 0 1px rgba(233,231,225,.08),inset 0 1px 0 rgba(233,231,225,.14),inset 0 -1px 0 rgba(0,0,0,.6)}
.mcard .brush{position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(255,255,255,.028) 0 1px,transparent 1px 3px),repeating-linear-gradient(0deg,rgba(255,255,255,.012) 0 1px,transparent 1px 2px);mix-blend-mode:screen;opacity:.9}
.mcard .sheen{position:absolute;inset:-40%;background:linear-gradient(115deg,transparent 35%,rgba(239,223,184,.22) 48%,rgba(255,255,255,.34) 50%,rgba(239,223,184,.2) 52%,transparent 65%);transform:translate(var(--sx,-30%),var(--sy,0)) rotate(0.001deg);mix-blend-mode:screen;opacity:.85;pointer-events:none;transition:transform .9s var(--ease-o)}
.mcard.live .sheen{transition:transform .12s linear}
.mcard .glare{position:absolute;inset:0;background:radial-gradient(60% 55% at var(--gx,30%) var(--gy,20%),rgba(255,255,255,.12),transparent 70%);pointer-events:none;mix-blend-mode:screen}
.mcard .rim{position:absolute;inset:0;border-radius:22px;box-shadow:inset 0 0 0 1.5px rgba(205,176,122,.18),inset 0 0 40px rgba(0,0,0,.6);pointer-events:none}
.mcard .lay{position:absolute;inset:0;padding:7.2% 7.5%;display:grid;grid-template-rows:auto 1fr auto;color:var(--platinum);transform:translateZ(1px)}
.mcard .row{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
.mcard .house{font:500 clamp(9px,1.65cqw,12px)/1.4 var(--fs);letter-spacing:.3em;text-transform:uppercase;color:var(--silver)}
.mcard .house b{display:block;font:400 clamp(12px,2.6cqw,17px)/1.1 var(--fd);letter-spacing:.2em;color:var(--platinum);margin-bottom:4px}
.mcard .tier{font:500 clamp(8px,1.5cqw,10.5px)/1 var(--fs);letter-spacing:.32em;text-transform:uppercase;color:var(--champ);padding:8px 12px;border:1px solid rgba(205,176,122,.45);border-radius:999px;white-space:nowrap}
.mcard .chip{position:absolute;left:7.5%;top:38%;width:13.5%;aspect-ratio:1.25;border-radius:12%;padding:0;border:0;background:linear-gradient(135deg,#efdfb8,#b8955c 45%,#e7cf98 60%,#8f7745);box-shadow:inset 0 1px 1px rgba(255,255,255,.5),0 3px 8px rgba(0,0,0,.5);overflow:hidden}
.mcard .chip::before,.mcard .chip::after{content:"";position:absolute;background:rgba(80,60,25,.55)}
.mcard .chip::before{left:0;right:0;top:34%;height:1px;box-shadow:0 12px 0 rgba(80,60,25,.55)}
.mcard .chip::after{top:0;bottom:0;left:38%;width:1px;box-shadow:12px 0 0 rgba(80,60,25,.55)}
.mcard .emb{align-self:end;font-family:var(--fm);font-weight:500;letter-spacing:.22em;text-transform:uppercase;color:#d7d5cf;text-shadow:0 1px 0 rgba(255,255,255,.22),0 -1px 0 rgba(0,0,0,.9),0 2px 3px rgba(0,0,0,.55)}
.mcard .emb .nm{font-size:clamp(14px,3.6cqw,23px);letter-spacing:.24em;line-height:1.1}
.mcard .emb .ln{display:flex;gap:clamp(14px,4cqw,32px);flex-wrap:wrap;margin-top:clamp(8px,1.6cqw,12px);font-size:clamp(8.5px,1.7cqw,11px);letter-spacing:.24em;color:#a9a8a2}
.mcard .emb .ln span b{display:block;font-weight:500;color:#cfcdc7;margin-top:3px;font-size:1.05em}
.mcard .sig{position:absolute;right:7.5%;bottom:7.5%;width:clamp(28px,8cqw,50px);height:clamp(28px,8cqw,50px);color:rgba(205,176,122,.9);transform:translateZ(1px)}
.mcard .sig svg{width:100%;height:100%}
.card-stage{container-type:inline-size}
.card-note{margin-top:22px;text-align:center;font-family:var(--fm);font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--steel)}
@media (max-width:980px){.w-g{grid-template-columns:1fr}.card-stage{order:-1;padding-top:0}.mcard{width:min(100%,440px)}#welcome{min-height:0}}
@media (max-width:760px){#welcome{padding-top:84px}.w-cta .btn{flex:1;justify-content:space-between}}

/* ------- brief (paper) ------- */
.brief-g{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(280px,.85fr);gap:clamp(36px,6vw,100px);align-items:start}
.letter{font:400 clamp(1.15rem,1.6vw,1.45rem)/1.62 var(--fd);color:var(--ink);max-width:62ch}
.letter p+p{margin-top:1.1em}
.letter .sal{font-style:italic;color:var(--ink-2)}
.letter .sig{margin-top:2.2em;display:grid;gap:4px}
.letter .sig b{font:italic 400 1.9rem/1 var(--fd);color:var(--ink)}
.letter .sig span{font:500 10px/1.6 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--ink-2)}
.how{display:grid;gap:14px}
.how>div{display:grid;grid-template-columns:44px 1fr;gap:18px;padding:22px 0;border-top:1px solid var(--rule)}
.how>div:last-child{border-bottom:1px solid var(--rule)}
.how b{font:400 1.7rem/1 var(--fd);color:var(--champ-lo);font-style:italic}
.how h3{font:600 12px/1.4 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--ink)}
.how p{margin-top:8px;font-size:14.5px;line-height:1.6;color:var(--ink-2)}
.terms{margin-top:clamp(40px,6vh,64px);display:flex;flex-wrap:wrap;gap:10px}
.terms span{font:500 11px/1.4 var(--fs);letter-spacing:.06em;color:var(--ink-2);padding:9px 14px;border:1px solid var(--rule);border-radius:999px;background:rgba(255,255,255,.35)}
.terms span b{color:var(--ink);font-weight:600;letter-spacing:.14em;text-transform:uppercase;font-size:10px;margin-right:8px}
@media (max-width:900px){.brief-g{grid-template-columns:1fr}}

/* ------- wing heads ------- */
.wing{display:grid;grid-template-columns:auto 1fr auto;gap:clamp(20px,3vw,44px);align-items:end;padding-bottom:30px;border-bottom:1px solid var(--rule);margin-bottom:clamp(40px,6vh,72px)}
.wing .rn{font:italic 400 clamp(4rem,9vw,8.5rem)/.85 var(--fd);color:transparent;-webkit-text-stroke:1px rgba(205,176,122,.55);letter-spacing:-.02em}
.wing .rn.fill{color:var(--champ);-webkit-text-stroke:0}
.wing .t-2{margin-top:16px}
.wing .desc{max-width:34ch;font-size:14.5px;line-height:1.6;color:var(--silver);padding-bottom:6px}
@media (max-width:900px){.wing{grid-template-columns:1fr;gap:18px}.wing .desc{max-width:none}}

/* ------- stats ------- */
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stats>div{padding:28px clamp(16px,2vw,32px) 26px 0;border-right:1px solid var(--rule-2)}
.stats>div+div{padding-left:clamp(16px,2vw,32px)}
.stats>div:last-child{border-right:0}
.stats .v{font:400 clamp(2.2rem,4vw,3.8rem)/1 var(--fd);letter-spacing:-.01em;font-variation-settings:"opsz" 72;color:var(--platinum)}
.stats .v.rng{font-size:clamp(1.5rem,2.3vw,2.3rem);line-height:1.15}
.stats .v small{font-size:.5em;letter-spacing:0;color:var(--steel);margin-inline:.15em}
.stats .k{font:500 10.5px/1 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel);margin-top:14px}
@media (max-width:760px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))}.stats>div:nth-child(2n){border-right:0}.stats>div:nth-child(odd){padding-left:0}.stats>div:nth-child(even){padding-left:18px}.stats>div{border-bottom:1px solid var(--rule-2)}}

/* ------- shelf ------- */
.shelf-h{display:flex;justify-content:space-between;align-items:end;gap:20px;margin-top:clamp(56px,8vh,96px);margin-bottom:26px}
.shelf-h .t-3{margin-top:14px}
.arrows{display:flex;gap:8px}
.arrows button{width:46px;height:46px;border-radius:50%;border:1px solid var(--rule);display:grid;place-items:center;color:var(--silver);transition:.4s var(--ease)}
.arrows button:hover{border-color:var(--champ);color:var(--champ-hi)}
.arrows svg{width:16px;height:16px}
.shelf{display:flex;gap:18px;overflow-x:auto;scroll-snap-type:x proximity;padding:4px 0 26px;margin-inline:calc(-1 * var(--gut));padding-inline:var(--gut);scrollbar-width:none;cursor:grab}
.shelf::-webkit-scrollbar{display:none}
.shelf.drag{cursor:grabbing;scroll-snap-type:none}
.card{flex:0 0 clamp(250px,24vw,330px);scroll-snap-align:start;display:grid;gap:14px;color:inherit}
.card .pl{position:relative;aspect-ratio:4/5;overflow:hidden;border-radius:18px;background:var(--graphite);padding:6px;border:1px solid var(--rule);transition:border-color .5s}
.card .pl .in{position:absolute;inset:6px;border-radius:13px;overflow:hidden;background:var(--carbon)}
.card .pl img{width:100%;height:100%;object-fit:cover;transition:transform 1.4s var(--ease-o),filter .8s;filter:saturate(.85) contrast(1.02)}
.card:hover .pl img{transform:scale(1.05);filter:saturate(1)}
.card:hover .pl{border-color:var(--rule-champ)}
.card .pl .k{position:absolute;left:18px;top:18px;font:400 12px/1 var(--fd);letter-spacing:.2em;color:var(--champ-hi);padding:8px 10px;border-radius:999px;background:rgba(8,8,10,.62)}
.card .pl .chip{position:absolute;right:16px;bottom:16px;background:rgba(8,8,10,.62)}
.card .pl .dg{position:absolute;inset:6px;display:grid;place-items:center;padding:14%;background:var(--carbon);border-radius:13px}
.card .pl .dg svg{width:100%;height:auto}
.card .nm{font:400 1.35rem/1.15 var(--fd);padding-inline:6px}
.card .nm small{display:block;font:500 10px/1.5 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);margin-top:6px}
.card .pr{display:flex;justify-content:space-between;gap:14px;align-items:baseline;padding:12px 6px 0;border-top:1px solid var(--rule-2);font-size:13px;color:var(--silver)}
.card .pr b{font:400 1.05rem/1 var(--fd);color:var(--platinum);white-space:nowrap}

/* ------- map ------- */
.map-h{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-top:clamp(56px,8vh,96px)}
.map-h .t-3{margin-top:14px}
.map-ctl{display:flex;gap:10px;flex-wrap:wrap}
.seg{display:inline-flex;border:1px solid var(--rule);border-radius:999px;padding:3px;background:rgba(17,17,20,.5)}
.seg button{font:600 10px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;padding:9px 14px;border-radius:999px;color:var(--steel);transition:.4s var(--ease);white-space:nowrap}
.seg button:hover{color:var(--platinum)}
.seg button[aria-pressed="true"]{background:var(--platinum);color:var(--void)}
.map-g{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(280px,1fr);gap:clamp(20px,3vw,44px);align-items:stretch;margin-top:26px}
.lmap-wrap{position:relative;height:clamp(460px,64vh,720px);border:1px solid var(--rule);border-radius:22px;padding:6px;background:var(--graphite);isolation:isolate}
#lmap{width:100%;height:100%;background:var(--carbon);border-radius:16px;overflow:hidden;opacity:0;transition:opacity 1.2s ease}
.lmap-wrap.ready #lmap{opacity:1}
.lmap-wrap.night:not(.aerial) .leaflet-tile-pane .leaflet-tile{filter:invert(1) hue-rotate(180deg) grayscale(.96) brightness(.82) contrast(1.06);-webkit-filter:invert(1) hue-rotate(180deg) grayscale(.96) brightness(.82) contrast(1.06)}
.lmap-wrap .leaflet-container{font-family:var(--fs);font-size:12px}
.lmap-wrap .leaflet-container a{color:inherit}
.lmap-wrap .leaflet-control-zoom{border:1px solid var(--rule);border-radius:999px;overflow:hidden;margin:16px;box-shadow:none}
.lmap-wrap .leaflet-bar a{background:rgba(17,17,20,.9);color:var(--platinum);border-bottom:1px solid var(--rule);width:36px;height:36px;line-height:34px;font-family:var(--fd);font-size:20px}
.lmap-wrap .leaflet-bar a:last-child{border-bottom:0}
.lmap-wrap .leaflet-bar a:hover{background:var(--slate);color:var(--champ-hi)}
.lmap-wrap .leaflet-bar a.leaflet-disabled{color:var(--steel-2)}
.lmap-wrap .leaflet-control-attribution{background:rgba(8,8,10,.7);color:var(--steel);font:400 9.5px/1.4 var(--fs);letter-spacing:.02em;padding:3px 8px;border-radius:8px 0 12px 0}
.lmap-wrap .leaflet-control-scale{margin:0 0 14px 16px}
.lmap-wrap .leaflet-control-scale-line{border:1px solid rgba(233,231,225,.5);border-top:0;background:rgba(8,8,10,.6);color:var(--platinum);font:500 9.5px/1.7 var(--fs);letter-spacing:.1em;padding:1px 6px}
.lmap-wrap .lm-pin{width:0!important;height:0!important;margin:0!important;border:0;background:none}
.lmap-wrap .lm-pin i{position:absolute;left:-13px;top:-13px;width:26px;height:26px;border-radius:50%;background:var(--champ);color:var(--void);border:1.5px solid var(--void);box-shadow:0 0 0 4px rgba(205,176,122,.22),0 2px 10px rgba(0,0,0,.5);font:400 11px/23px var(--fd);letter-spacing:.06em;text-align:center;font-style:normal;transition:.3s}
.lmap-wrap .lm-pin b{position:absolute;left:18px;top:-9px;white-space:nowrap;font:600 9.5px/18px var(--fs);letter-spacing:.16em;text-transform:uppercase;color:var(--platinum);text-shadow:0 0 4px #08080a,0 0 8px #08080a,0 1px 2px #08080a;transition:opacity .3s}
.lmap-wrap.aerial .lm-pin b{text-shadow:0 0 4px #000,0 0 8px #000}
.lmap-wrap.far .lm-pin:not(.on):not(:hover) b{opacity:0}
.lmap-wrap .lm-pin.on i,.lmap-wrap .lm-pin:hover i{background:var(--champ-hi);transform:scale(1.15)}
.lmap-wrap .lm-pin.ap i{background:var(--graphite);color:var(--champ-hi);border-color:var(--champ)}
.lmap-wrap .leaflet-popup-content-wrapper{background:var(--graphite);color:var(--platinum);border-radius:14px;border:1px solid var(--rule);box-shadow:0 14px 40px rgba(0,0,0,.5);padding:0}
.lmap-wrap .leaflet-popup-content{margin:16px 18px 15px;font:400 13px/1.5 var(--fs);min-width:220px}
.lmap-wrap .leaflet-popup-tip{background:var(--graphite);box-shadow:none}
.lmap-wrap .leaflet-container a.leaflet-popup-close-button{color:var(--steel);font:300 20px/22px var(--fs);padding:6px 8px 0 0;width:auto;height:auto}
.lm-pop .k{font-family:var(--fd);color:var(--champ);letter-spacing:.2em;font-size:11px}
.lm-pop .n{font-family:var(--fd);font-size:18px;margin:4px 0 2px}
.lm-pop .a{color:var(--steel);font-size:12px}
.lm-pop .p{font-family:var(--fd);font-size:15px;margin-top:8px}
.lm-pop .x{display:flex;gap:14px;margin-top:12px;font-size:10px;letter-spacing:.18em;text-transform:uppercase;font-weight:600;color:var(--champ-hi)}
.lmap-wrap .lm-ref{width:0!important;height:0!important;margin:0!important;border:0;background:none}
.lmap-wrap .lm-ref i{position:absolute;left:-5px;top:-5px;width:10px;height:10px;border-radius:50%;background:var(--void);border:1.5px solid var(--platinum);opacity:.85}
.lmap-wrap .lm-ref.dest i{background:var(--platinum);border-color:var(--void);width:12px;height:12px;left:-6px;top:-6px}
.lmap-wrap .lm-ref b{position:absolute;left:11px;top:-8px;white-space:nowrap;font:600 9px/16px var(--fs);letter-spacing:.14em;text-transform:uppercase;color:rgba(233,231,225,.8);text-shadow:0 0 4px #08080a,0 0 8px #08080a}
.lmap-wrap.far .lm-ref:not(.dest) b{opacity:0}
.lmap-wrap .leaflet-tooltip{background:var(--graphite);color:var(--platinum);border:1px solid var(--rule);border-radius:8px;font:400 11px/1.4 var(--fs);letter-spacing:.06em;box-shadow:none}
.lmap-wrap .leaflet-tooltip::before{display:none}
.lm-panel{border:1px solid var(--rule);border-radius:22px;background:var(--graphite);display:flex;flex-direction:column;max-height:clamp(460px,64vh,720px);overflow:auto;scrollbar-width:thin}
.lm-grp{border-bottom:1px solid var(--rule-2)}
.lm-gh{display:flex;justify-content:space-between;gap:12px;padding:14px 20px 8px;font:500 10px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel)}
.lm-panel .mrow{display:grid;grid-template-columns:26px 1fr auto;gap:14px;align-items:center;text-align:left;padding:12px 20px;border-top:1px solid var(--rule-2);width:100%;transition:background .3s,color .3s}
.lm-panel .mrow:hover{background:rgba(233,231,225,.04)}
.lm-panel .mrow[aria-pressed="true"]{background:rgba(205,176,122,.12)}
.lm-panel .mrow .k{width:26px;height:26px;border-radius:50%;background:var(--champ);color:var(--void);font:400 11px/25px var(--fd);text-align:center;letter-spacing:.06em;border:1px solid var(--void);box-shadow:0 0 0 3px rgba(205,176,122,.18)}
.lm-panel .mrow .t{font-size:14.5px;line-height:1.25}
.lm-panel .mrow .t small{display:block;font-size:11.5px;color:var(--steel);margin-top:3px}
.lm-panel .mrow .dist{font-size:11px;letter-spacing:.06em;color:var(--steel);white-space:nowrap;text-align:right}
.lm-panel .mrow .dist b{font-family:var(--fd);font-weight:400;font-size:15px;color:var(--platinum);letter-spacing:0}
.lm-note{padding:14px 20px 18px;font-size:12px;line-height:1.55;color:var(--steel);margin-top:auto}
.lm-hint{position:absolute;left:50%;top:16px;transform:translateX(-50%);z-index:500;font:600 10px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--platinum);background:rgba(8,8,10,.72);border:1px solid var(--rule);border-radius:999px;padding:10px 16px;pointer-events:none;transition:opacity .5s;white-space:nowrap}
.lmap-wrap.wheel .lm-hint,.lmap-wrap.failed .lm-hint{opacity:0}
.map-fb{position:absolute;inset:6px;border-radius:16px;background:var(--carbon);padding:clamp(20px,3vw,36px);overflow:auto}
.map-fb p{margin:14px 0 18px;color:var(--silver);font-size:14px}
.fbrows{display:grid;gap:0}
.fbrows a{display:grid;grid-template-columns:28px 1fr auto;gap:14px;align-items:center;padding:12px 0;border-top:1px solid var(--rule-2);font-size:14px}
.fbrows a .k{font-family:var(--fd);color:var(--champ)}
.fbrows a small{display:block;color:var(--steel);font-size:12px}
.fbrows a .d{font:600 10px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--champ-hi)}
@media (max-width:900px){.map-g{grid-template-columns:1fr}.lm-panel{max-height:380px}.lmap-wrap{height:min(64vh,520px)}}

/* ------- ledger ------- */
.ledger-h{display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap;margin-top:clamp(56px,8vh,96px)}
.ledger-h .t-2{margin-top:14px}
.sorts{display:inline-flex;border:1px solid var(--rule);border-radius:999px;padding:3px}
.sorts button{font:600 10px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;padding:9px 14px;border-radius:999px;color:var(--steel);transition:.4s var(--ease)}
.sorts button.on{background:var(--platinum);color:var(--void)}
.ledger-w{margin-top:26px;overflow-x:auto;border:1px solid var(--rule);border-radius:22px;background:var(--graphite);padding:6px;min-width:0}
.ledger{width:100%;min-width:900px;border-radius:16px;overflow:hidden;background:var(--carbon)}
.ledger th{font:500 10px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel);text-align:left;padding:18px 16px;border-bottom:1px solid var(--rule)}
.ledger td{padding:16px;border-bottom:1px solid var(--rule-2);vertical-align:middle;font-size:14px;color:var(--silver)}
.ledger tr:last-child td{border-bottom:0}
.ledger tbody tr{transition:background .3s;cursor:pointer}
.ledger tbody tr:hover{background:rgba(233,231,225,.035)}
.ledger td.k{font-family:var(--fd);color:var(--champ);letter-spacing:.14em}
.ledger td.nm{font:400 1.1rem/1.2 var(--fd);color:var(--platinum)}
.ledger td.nm small{display:block;font:400 11.5px/1.4 var(--fs);color:var(--steel);margin-top:4px;max-width:28ch}
.ledger td.pr{font-family:var(--fd);color:var(--platinum);white-space:nowrap;font-size:15px}
.ledger td.vw{max-width:26ch;font-size:13px}
.ledger th.st,.ledger td.st{text-align:center}

/* ------- stars ------- */
.star{width:40px;height:40px;border-radius:50%;border:1px solid var(--rule);display:inline-grid;place-items:center;color:var(--silver);transition:.4s var(--ease);flex:0 0 auto}
.star svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:1.2;transition:.4s var(--ease)}
.star:hover{border-color:var(--champ);color:var(--champ-hi)}
.star.on{background:var(--champ);border-color:var(--champ);color:var(--void)}
.star.on svg{fill:currentColor}
.star.pop{animation:pop .5s var(--ease-o)}
@keyframes pop{0%{transform:scale(1)}40%{transform:scale(1.25)}100%{transform:scale(1)}}
.pg[data-shade="paper"] .star{color:var(--ink-2);border-color:rgba(20,20,22,.25)}
.pg[data-shade="paper"] .star.on{background:var(--ink);border-color:var(--ink);color:var(--paper)}

/* ------- dossiers ------- */
.dz .run{display:flex;justify-content:space-between;align-items:center;gap:16px;font:500 10px/1 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel);padding-bottom:22px;border-bottom:1px solid var(--rule)}
.dz .run .r{display:flex;align-items:center;gap:10px}
.dz .head{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:clamp(24px,4vw,64px);align-items:end;margin-top:clamp(36px,5vh,56px)}
.dz .head .nm{font:400 clamp(2.6rem,6vw,5.6rem)/.98 var(--fd);letter-spacing:-.015em;margin-top:18px;font-variation-settings:"opsz" 96}
.dz .head .sc{font:italic 400 1.25rem/1.3 var(--fd);color:var(--silver);margin-top:10px}
.dz .addr{display:flex;flex-wrap:wrap;gap:8px 24px;margin-top:22px;font-size:14px;color:var(--silver)}
.dz .addr b{font-weight:500;color:var(--platinum)}
.dz .addr .gm{color:var(--champ);display:inline-flex;align-items:center;gap:8px;font:600 10.5px/1 var(--fs);letter-spacing:.18em;text-transform:uppercase}
.dz .addr .gm svg{width:13px;height:13px;transition:transform .4s var(--ease)}
.dz .addr .gm:hover svg{transform:translateX(4px)}
.dz .head .pr{text-align:right}
.dz .head .pr .v{font:400 clamp(1.8rem,3vw,2.8rem)/1 var(--fd);color:var(--champ-hi);white-space:nowrap}
.dz .head .pr .k{font:500 10px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel);margin-top:10px}
.plate{position:relative;overflow:hidden;border-radius:22px;background:var(--graphite);padding:6px;border:1px solid var(--rule);cursor:zoom-in}
.plate .pi{position:absolute;inset:6px;border-radius:16px;overflow:hidden;background:var(--carbon)}
.plate .pi img{width:100%;height:100%;object-fit:cover;transform:translateY(var(--py,0)) scale(1.08);will-change:transform;transition:filter .8s;filter:saturate(.9)}
.plate:hover .pi img{filter:saturate(1)}
.plate .cap{position:absolute;left:22px;bottom:20px;right:22px;display:flex;justify-content:space-between;align-items:center;gap:12px;font:500 10.5px/1.4 var(--fs);letter-spacing:.14em;text-transform:uppercase;color:var(--platinum);text-shadow:0 1px 3px rgba(0,0,0,.7)}
.plate .cap::after{content:"Open";font:600 9.5px/1 var(--fs);letter-spacing:.22em;padding:9px 12px;border-radius:999px;background:rgba(8,8,10,.6);border:1px solid var(--rule);color:var(--champ-hi);white-space:nowrap}
.plate.wide{aspect-ratio:21/9;margin-top:clamp(36px,5vh,56px)}
.plate.sp{aspect-ratio:4/5}
.plate.tall{aspect-ratio:3/4}
.plate.sq{aspect-ratio:1}
.dz .body{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(28px,4vw,72px);margin-top:clamp(40px,6vh,72px)}
.dz .body.split{grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);align-items:start}
.dz .body.split.flip .sticky{order:2}
.dz .sticky{position:sticky;top:96px}
.facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0;border-top:1px solid var(--rule)}
.facts>div{padding:20px 0 18px;border-bottom:1px solid var(--rule-2);padding-right:18px}
.facts dt{font:500 10px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel)}
.facts dd{font:400 clamp(1.6rem,2.4vw,2.2rem)/1.05 var(--fd);color:var(--platinum);margin-top:10px}
.facts dd small{font:500 10.5px/1 var(--fs);letter-spacing:.14em;text-transform:uppercase;color:var(--champ);margin-left:8px;vertical-align:middle}
.facts dd small.b{display:block;margin:8px 0 0;color:var(--steel);text-transform:none;letter-spacing:.02em;font-size:12px}
.types-w{margin-top:30px;overflow-x:auto}
.types{width:100%;min-width:420px}
.types th{font:500 10px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--steel);text-align:left;padding:12px 10px 12px 0;border-bottom:1px solid var(--rule)}
.types td{padding:14px 10px 14px 0;border-bottom:1px solid var(--rule-2);vertical-align:top;font-size:14px;color:var(--silver)}
.types td.t{color:var(--platinum);font-size:15px}
.types td.t small{display:block;font-size:12px;color:var(--steel);margin-top:3px}
.types th.n,.types td.n{text-align:center}
.types th.p,.types td.p{text-align:right;font-family:var(--fd);color:var(--champ-hi);font-size:15px;white-space:nowrap}
.types td.p.off{color:var(--steel);font-family:var(--fs);font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.view{margin-top:6px;padding:28px clamp(20px,2.6vw,36px);border-radius:22px;background:var(--graphite);border:1px solid var(--rule);position:relative}
.view::before{content:"";position:absolute;inset:6px;border-radius:16px;border:1px solid var(--rule-2);pointer-events:none}
.view p{margin-top:16px;font:italic 400 clamp(1.1rem,1.5vw,1.35rem)/1.6 var(--fd);color:var(--platinum)}
.reco{margin-top:22px;padding:26px clamp(20px,2.6vw,36px);border-radius:22px;border:1px solid var(--rule-champ);background:rgba(205,176,122,.06)}
.reco .t{font:400 1.5rem/1.2 var(--fd);margin-top:14px;color:var(--champ-hi)}
.reco p{margin-top:12px;font-size:14.5px;line-height:1.65;color:var(--silver)}
.steps{display:grid;gap:0;margin-top:20px}
.steps>div{display:grid;grid-template-columns:34px 1fr;gap:14px;padding:14px 0;border-top:1px solid var(--rule-2);font-size:14px;color:var(--silver);line-height:1.55}
.steps b{font:italic 400 1.3rem/1.2 var(--fd);color:var(--champ)}
.credits{margin-top:28px;display:grid;gap:8px;font-size:12px;color:var(--steel);line-height:1.5}
.credits b{font-weight:600;color:var(--silver);letter-spacing:.14em;text-transform:uppercase;font-size:10px}
.gal-h{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-top:clamp(48px,7vh,80px)}
.groups{display:inline-flex;border:1px solid var(--rule);border-radius:999px;padding:3px;flex-wrap:wrap}
.groups button{font:600 10px/1 var(--fs);letter-spacing:.18em;text-transform:uppercase;padding:9px 13px;border-radius:999px;color:var(--steel);transition:.4s var(--ease)}
.groups button.on{background:var(--platinum);color:var(--void)}
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:12px;margin-top:22px}
.gal figure{position:relative;aspect-ratio:4/3;overflow:hidden;border-radius:14px;background:var(--graphite);cursor:zoom-in;border:1px solid var(--rule-2)}
.gal figure.plan{background:var(--paper)}
.gal figure.plan img{object-fit:contain;padding:6%}
.gal figure img{width:100%;height:100%;object-fit:cover;transition:transform 1.2s var(--ease-o);filter:saturate(.9)}
.gal figure:hover img{transform:scale(1.06)}
.gal figure .g{position:absolute;left:12px;top:12px;font:600 9px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--champ-hi);padding:7px 10px;border-radius:999px;background:rgba(8,8,10,.6)}
.gal figcaption{position:absolute;left:0;right:0;bottom:0;padding:26px 14px 12px;font-size:12px;color:var(--platinum);background:linear-gradient(180deg,transparent,rgba(8,8,10,.8));opacity:0;transform:translateY(6px);transition:.5s var(--ease)}
.gal figure:hover figcaption{opacity:1;transform:none}
.gal figure.hide{display:none}
.dz .foot{display:flex;justify-content:space-between;align-items:center;margin-top:clamp(48px,7vh,80px);padding-top:20px;border-top:1px solid var(--rule);font:500 10px/1 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel)}
.dz .foot b{font:400 15px/1 var(--fd);color:var(--champ)}
.diagram{padding:6px;border-radius:22px;border:1px solid var(--rule);background:var(--graphite)}
.diagram svg{width:100%;height:auto;border-radius:16px;background:var(--carbon);padding:6%;font:400 3px/1 var(--fs);fill:var(--platinum)}
.diagram svg .s{font-size:2.4px;fill:var(--steel)}
.diagram svg .r{font-size:2.9px;fill:var(--champ-hi)}
.diagram svg .road{stroke:rgba(233,231,225,.28);stroke-width:.35;stroke-dasharray:2 1.2}
.diagram svg .b{fill:none;stroke:var(--champ);stroke-width:.4;stroke-dasharray:1.4 1}
.diagram svg .hx{fill:url(#hx);stroke:rgba(233,231,225,.4);stroke-width:.25}
.diagram svg .nw{fill:none;stroke:var(--champ-hi);stroke-width:.45;stroke-dasharray:.4 1.2;stroke-linecap:round}
.diagram .cap{margin-top:12px;text-align:center;font:500 10px/1.5 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);padding-bottom:8px}
@media (max-width:900px){.dz .body,.dz .body.split{grid-template-columns:1fr}.dz .sticky{position:static}.dz .body.split.flip .sticky{order:0}.dz .head{grid-template-columns:1fr}.dz .head .pr{text-align:left}.plate.wide{aspect-ratio:4/3}.gal{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:560px){.facts{grid-template-columns:1fr}.plate.sp,.plate.tall,.plate.sq{aspect-ratio:4/5}}

/* ------- the vault ------- */
#vault{background:#050506;position:relative;isolation:isolate}
#vault::before{content:"";position:absolute;inset:0;z-index:-1;background:radial-gradient(60% 40% at 50% 0%,rgba(205,176,122,.08),transparent 70%);pointer-events:none}
.houses{display:flex;flex-wrap:wrap;gap:8px;margin-top:8px}
.houses button{font:600 10px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;padding:11px 16px;border-radius:999px;border:1px solid var(--rule);color:var(--steel);transition:.4s var(--ease)}
.houses button:hover{color:var(--platinum);border-color:var(--rule-champ)}
.houses button.on{background:var(--platinum);color:var(--void);border-color:var(--platinum)}
.vgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:18px;margin-top:clamp(28px,4vh,44px)}
.piece{position:relative;border-radius:24px;padding:6px;background:var(--graphite);border:1px solid var(--rule);display:grid;grid-template-rows:auto 1fr;transition:border-color .6s var(--ease),transform .8s var(--ease-o),opacity .6s var(--ease),filter .6s;text-align:left;color:inherit;cursor:pointer}
.piece:hover{border-color:var(--rule-champ);transform:translateY(-4px)}
.piece.dim{opacity:.22;filter:grayscale(1);pointer-events:none}
.piece .art{position:relative;aspect-ratio:1/1.12;border-radius:18px;overflow:hidden;background:radial-gradient(70% 60% at 50% 42%,#15151a,#0a0a0c 80%);box-shadow:inset 0 1px 0 rgba(233,231,225,.06);perspective:900px}
.piece .art svg{position:absolute;inset:0;width:100%;height:100%;transform:rotateX(var(--px,0deg)) rotateY(var(--pyaw,0deg));transition:transform .9s var(--ease-o);will-change:transform}
.piece.live .art svg{transition:transform .1s linear}
.piece .art img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.piece .art .ph{position:absolute;left:14px;top:14px;font:600 9px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);padding:7px 10px;border-radius:999px;border:1px solid var(--rule-2);background:rgba(8,8,10,.5)}
.piece .art .rn{position:absolute;right:16px;top:12px;font:italic 400 1.5rem/1 var(--fd);color:var(--champ)}
.piece .meta{padding:18px 16px 16px;display:grid;gap:6px}
.piece .hs{font:500 10px/1 var(--fs);letter-spacing:.26em;text-transform:uppercase;color:var(--champ)}
.piece .md{font:400 1.35rem/1.15 var(--fd);color:var(--platinum)}
.piece .rf{font-family:var(--fm);font-size:10.5px;letter-spacing:.12em;color:var(--steel);text-transform:uppercase}
.piece .ft{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-top:12px;padding-top:12px;border-top:1px solid var(--rule-2)}
.piece .ft .pr{font:400 .95rem/1 var(--fd);color:var(--silver)}
.piece .star{width:34px;height:34px}
.piece .star svg{width:12px;height:12px}
.v-note{margin-top:clamp(32px,5vh,52px);display:grid;grid-template-columns:auto 1fr;gap:18px;align-items:start;padding:22px 26px;border-radius:22px;border:1px solid var(--rule-champ);background:rgba(205,176,122,.05);font-size:13.5px;line-height:1.6;color:var(--silver);max-width:820px}
.v-note svg{width:22px;height:22px;color:var(--champ);margin-top:2px}
.v-note b{color:var(--platinum);font-weight:500}
/* case (piece detail) */
#case{position:fixed;inset:0;top:0;right:0;bottom:0;left:0;z-index:var(--overlay-z);overscroll-behavior:contain;display:grid;grid-template-columns:1fr minmax(0,min(100%,1080px));opacity:0;visibility:hidden;transition:opacity .5s var(--ease),visibility 0s .5s}
#case.open{opacity:1;visibility:visible;transition:opacity .5s var(--ease)}
#case .dim{background:rgba(5,5,6,.72);cursor:pointer}
#case .pn{background:var(--carbon);border-left:1px solid var(--rule);overflow:auto;transform:translateX(40px);transition:transform .7s var(--ease-o);display:grid;grid-template-rows:auto 1fr;-webkit-overflow-scrolling:touch}
#case.open .pn{transform:none}
#case .bar{display:flex;justify-content:space-between;align-items:center;padding:22px var(--gut) 18px;border-bottom:1px solid var(--rule);position:sticky;top:0;background:var(--carbon);z-index:2}
#case .bar .k{font:500 10px/1.5 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel)}
#case .bar .k b{color:var(--champ);font-weight:500}
#case .bar .x{display:flex;gap:8px}
#case .bar button{width:44px;height:44px;border:1px solid var(--rule);border-radius:50%;display:grid;place-items:center;transition:.3s}
#case .bar button:hover{border-color:var(--champ);color:var(--champ-hi)}
#case .bar button svg{width:16px;height:16px}
#case .cg{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(24px,3vw,48px);padding:clamp(24px,3vw,44px) var(--gut) clamp(40px,5vh,64px);align-items:start}
#case .cart{position:sticky;top:96px;aspect-ratio:1/1.12;border-radius:22px;overflow:hidden;background:radial-gradient(70% 60% at 50% 42%,#15151a,#0a0a0c 80%);border:1px solid var(--rule)}
#case .cart svg,#case .cart img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
#case .cart .ph{position:absolute;left:16px;top:16px;font:600 9.5px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);padding:8px 12px;border-radius:999px;border:1px solid var(--rule-2);background:rgba(8,8,10,.6)}
#case .hs{font:500 11px/1 var(--fs);letter-spacing:.28em;text-transform:uppercase;color:var(--champ)}
#case .md{font:400 clamp(2rem,3.4vw,3rem)/1.05 var(--fd);margin-top:14px;font-variation-settings:"opsz" 72}
#case .rf{font-family:var(--fm);font-size:11px;letter-spacing:.14em;color:var(--steel);text-transform:uppercase;margin-top:12px}
#case .vw{margin-top:22px;font:italic 400 clamp(1.05rem,1.4vw,1.25rem)/1.6 var(--fd);color:var(--platinum)}
#case .spec{margin-top:26px;border-top:1px solid var(--rule)}
#case .spec div{display:grid;grid-template-columns:130px 1fr;gap:16px;padding:13px 0;border-bottom:1px solid var(--rule-2);font-size:14px;color:var(--silver)}
#case .spec dt{font:500 10px/1.6 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel)}
#case .spec dd.hi{color:var(--champ-hi);font-family:var(--fd);font-size:16px}
#case .acts{display:flex;gap:12px;flex-wrap:wrap;margin-top:28px}
#case .fine{margin-top:22px;font-size:12px;line-height:1.55;color:var(--steel)}
@media (max-width:900px){#case{grid-template-columns:1fr}#case .dim{display:none}#case .cg{grid-template-columns:1fr}#case .cart{position:static}#case .spec div{grid-template-columns:110px 1fr}}

/* ------- desk ------- */
.desk-g{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(28px,4vw,72px);margin-top:clamp(40px,6vh,72px)}
.contacts{display:grid;gap:0;border-top:1px solid var(--rule)}
.contacts a{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:18px 0;border-bottom:1px solid var(--rule-2);transition:padding .4s var(--ease)}
.contacts a:hover{padding-left:8px}
.contacts .v{font:400 1.25rem/1.1 var(--fd);color:var(--platinum)}
.contacts .v small{display:block;font:500 10px/1.5 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);margin-top:6px}
.agent{display:flex;align-items:center;gap:18px;margin-top:30px;padding:20px;border-radius:22px;border:1px solid var(--rule-champ);background:rgba(205,176,122,.05)}
.agent .av{width:58px;height:58px;border-radius:50%;display:grid;place-items:center;font:400 1.15rem/1 var(--fd);letter-spacing:.1em;color:var(--void);background:linear-gradient(135deg,var(--champ-hi),var(--champ) 60%,var(--champ-lo));box-shadow:inset 0 1px 0 rgba(255,255,255,.5)}
.agent b{display:block;font:400 1.25rem/1.15 var(--fd);color:var(--platinum)}
.agent span{display:block;font:500 10px/1.6 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);margin-top:6px}
.agent .st{margin-left:auto;font-family:var(--fm);font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--champ);white-space:nowrap;display:flex;align-items:center;gap:8px}
.agent .st i{width:7px;height:7px;border-radius:50%;background:var(--champ);box-shadow:0 0 0 0 rgba(205,176,122,.6);animation:pulse 2.4s infinite}
@keyframes pulse{0%{box-shadow:0 0 0 0 rgba(205,176,122,.55)}70%{box-shadow:0 0 0 9px rgba(205,176,122,0)}100%{box-shadow:0 0 0 0 rgba(205,176,122,0)}}
.req{padding:6px;border-radius:24px;border:1px solid var(--rule);background:var(--graphite)}
.req .in{border-radius:18px;background:var(--carbon);padding:clamp(20px,2.6vw,32px)}
.req .t-3{margin-top:12px}
.req ul{list-style:none;margin:20px 0 0;padding:0;display:grid;gap:0;border-top:1px solid var(--rule)}
.req li{display:grid;grid-template-columns:34px 1fr auto;gap:14px;align-items:center;padding:12px 0;border-bottom:1px solid var(--rule-2);font-size:14px}
.req li .k{font-family:var(--fd);color:var(--champ);letter-spacing:.1em;font-size:13px}
.req li small{display:block;color:var(--steel);font-size:11.5px;margin-top:2px}
.req li .rm{font:600 9.5px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel);padding:8px 10px;border-radius:999px;border:1px solid var(--rule-2);transition:.3s}
.req li .rm:hover{color:var(--platinum);border-color:var(--rule)}
.req .empty{margin-top:18px;font-size:14px;color:var(--steel)}
.req .intent{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
.req .intent button{font:600 10px/1 var(--fs);letter-spacing:.18em;text-transform:uppercase;padding:10px 14px;border-radius:999px;border:1px solid var(--rule);color:var(--steel);transition:.4s var(--ease)}
.req .intent button[aria-pressed="true"]{background:var(--champ);color:var(--void);border-color:var(--champ)}
.req .prev{margin-top:20px;padding:18px 20px;border-radius:14px;background:var(--void);border:1px solid var(--rule-2);font-family:var(--fm);font-size:12px;line-height:1.7;color:var(--silver);white-space:pre-wrap;word-break:break-word;min-height:80px}
.req .send{margin-top:20px;display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.req .hint{font-size:11.5px;color:var(--steel)}
.next{display:grid;gap:0;margin-top:34px;border-top:1px solid var(--rule)}
.next>div{display:grid;grid-template-columns:40px 1fr;gap:16px;padding:20px 0;border-bottom:1px solid var(--rule-2)}
.next b{font:italic 400 1.6rem/1 var(--fd);color:var(--champ)}
.next h3{font:600 11.5px/1.4 var(--fs);letter-spacing:.2em;text-transform:uppercase}
.next p{margin-top:8px;font-size:14px;line-height:1.6;color:var(--silver)}
.credit-g{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(24px,3vw,48px);margin-top:clamp(64px,9vh,110px);padding-top:36px;border-top:1px solid var(--rule);font-size:12.5px;line-height:1.6;color:var(--steel)}
.credit-g b{display:block;font:500 10px/1 var(--fs);letter-spacing:.22em;text-transform:uppercase;color:var(--silver);margin-bottom:12px}
.credit-g .lg{display:flex;align-items:center;gap:12px;margin-bottom:14px;color:var(--platinum)}
.credit-g .lg svg{width:30px;height:30px;color:var(--champ)}
.credit-g .lg span{font:400 14px/1.2 var(--fd);letter-spacing:.1em;text-transform:uppercase}
.credit-g .lg small{display:block;font:italic 400 12px/1.4 var(--fd);text-transform:none;letter-spacing:0;color:var(--steel)}
.fin{display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap;margin-top:44px;padding-top:22px;border-top:1px solid var(--rule);font:500 9.5px/1.5 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel)}
.fin .seal{font-family:var(--fd);color:var(--champ);letter-spacing:.2em}
@media (max-width:900px){.desk-g{grid-template-columns:1fr}.credit-g{grid-template-columns:1fr}}

/* ------- index overlay ------- */
#index{position:fixed;inset:0;top:0;right:0;bottom:0;left:0;z-index:var(--overlay-z);background:rgba(5,5,6,.9);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);overscroll-behavior:contain;opacity:0;visibility:hidden;transition:opacity .5s var(--ease),visibility 0s .5s;overflow:auto}
#index.open{opacity:1;visibility:visible;transition:opacity .5s var(--ease)}
#index .in{max-width:1100px;margin:0 auto;padding:clamp(80px,10vh,120px) var(--gut) 120px}
#index .ih{display:flex;justify-content:space-between;align-items:end;gap:20px;border-bottom:1px solid var(--rule);padding-bottom:26px}
#index .ih .t-2{margin-top:14px}
#index .close{width:52px;height:52px;border-radius:50%;border:1px solid var(--rule);display:grid;place-items:center;transition:.3s}
#index .close:hover{border-color:var(--champ);color:var(--champ-hi)}
#index .close svg{width:18px;height:18px}
#index .secs{display:flex;flex-wrap:wrap;gap:8px;margin-top:26px}
#index .secs a{font:600 10.5px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;padding:12px 16px;border-radius:999px;border:1px solid var(--rule);color:var(--silver);transition:.3s;opacity:0;transform:translateY(12px)}
#index.open .secs a{opacity:1;transform:none;transition:opacity .6s var(--ease-o) calc(.1s + var(--i,0) * 40ms),transform .6s var(--ease-o) calc(.1s + var(--i,0) * 40ms),border-color .3s,color .3s}
#index .secs a:hover{border-color:var(--champ);color:var(--champ-hi)}
#index .cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(20px,3vw,48px);margin-top:36px}
#index .cols h3{font:500 10px/1 var(--fs);letter-spacing:.24em;text-transform:uppercase;color:var(--steel);padding-bottom:14px;border-bottom:1px solid var(--rule)}
#index .rows a{display:grid;grid-template-columns:28px 1fr auto;gap:14px;align-items:center;padding:13px 0;border-bottom:1px solid var(--rule-2);font-size:14px;color:var(--platinum);opacity:0;transform:translateY(10px)}
#index.open .rows a{opacity:1;transform:none;transition:opacity .6s var(--ease-o) calc(.25s + var(--i,0) * 35ms),transform .6s var(--ease-o) calc(.25s + var(--i,0) * 35ms)}
#index .rows a .k{font-family:var(--fd);color:var(--champ);letter-spacing:.1em;font-size:13px}
#index .rows a small{display:block;color:var(--steel);font-size:11.5px;margin-top:2px}
#index .rows a .pr{font-family:var(--fd);color:var(--silver);font-size:13.5px;white-space:nowrap}
@media (max-width:760px){#index .cols{grid-template-columns:1fr}}

/* ------- lightbox ------- */
#lb{position:fixed;inset:0;top:0;right:0;bottom:0;left:0;overscroll-behavior:contain;touch-action:none;z-index:var(--overlay-z);background:rgba(5,5,6,.96);color:var(--platinum);opacity:0;visibility:hidden;transition:opacity .5s ease,visibility 0s .5s;display:grid;grid-template-rows:auto 1fr auto}
#lb.open{opacity:1;visibility:visible;transition:opacity .5s ease}
#lb .bar{display:flex;justify-content:space-between;align-items:center;padding:18px var(--gut);font:500 10.5px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--steel)}
#lb .bar b{font-family:var(--fd);font-weight:400;color:var(--platinum);letter-spacing:.14em;font-size:13px}
#lb .bar .x{display:flex;gap:8px}
#lb .bar button{width:44px;height:44px;border:1px solid var(--rule);border-radius:50%;display:grid;place-items:center;transition:.3s}
#lb .bar button:hover{border-color:var(--champ);color:var(--champ-hi)}
#lb .bar button svg{width:16px;height:16px}
#lb .st{position:relative;overflow:hidden;touch-action:none}
#lb .st img{position:absolute;inset:0;top:0;right:0;bottom:0;left:0;width:100%;height:100%;object-fit:contain;opacity:0;transition:opacity .5s ease;user-select:none;-webkit-user-drag:none;transform-origin:center}
#lb .st img.on{opacity:1}
#lb.zoomed .st img.on{cursor:grab}
#lb .nav{position:absolute;top:50%;transform:translateY(-50%);width:54px;height:54px;border:1px solid var(--rule);border-radius:50%;display:grid;place-items:center;background:rgba(8,8,10,.4);transition:.3s;z-index:2}
#lb .nav:hover{border-color:var(--champ);color:var(--champ-hi)}
#lb .nav.p{left:clamp(12px,3vw,40px)}#lb .nav.n{right:clamp(12px,3vw,40px)}
#lb .nav svg{width:18px;height:18px}
#lb .cap{display:flex;justify-content:space-between;align-items:center;gap:16px;padding:16px var(--gut) 22px;font:500 11px/1.5 var(--fs);letter-spacing:.14em;text-transform:uppercase;color:var(--steel);flex-wrap:wrap}
#lb .cap .c{color:var(--platinum)}
#lb .cap .k{font-family:var(--fd);color:var(--champ);letter-spacing:.2em}
@media (max-width:640px){#lb .nav{display:none}}

/* ------- cursor ------- */
.cur{position:fixed;left:0;top:0;z-index:var(--cursor-z);pointer-events:none;width:8px;height:8px;border-radius:50%;background:var(--champ-hi);transform:translate(-50%,-50%);mix-blend-mode:difference;display:none}
.cur.hide{visibility:hidden}
.cur2{position:fixed;left:0;top:0;z-index:calc(var(--cursor-z) - 1);pointer-events:none;width:34px;height:34px;border-radius:50%;border:1px solid rgba(239,223,184,.6);transform:translate(-50%,-50%);transition:width .3s,height .3s,background .3s,opacity .3s;display:none;place-items:center;font:600 9px/1 var(--fs);letter-spacing:.2em;text-transform:uppercase;color:var(--void)}
.cur2.big{width:74px;height:74px;background:rgba(239,223,184,.92);border-color:transparent}
.cur2.big::after{content:attr(data-l)}
@media (pointer:fine) and (min-width:900px){.cur,.cur2{display:grid}body{cursor:none}a,button,.gal figure,.plate,.shelf,.mcard,.piece{cursor:none}}

/* ------- touch / motion / print ------- */
@media (hover:none){
  body::before{display:none}
  .isl{backdrop-filter:none;-webkit-backdrop-filter:none;background:rgba(17,17,20,.96)}
  .plate .pi img{transform:none!important;will-change:auto}
  .gal figure img,.card .pl img{transition:none}
  .gal figcaption{opacity:1;transform:none}
  .lm-hint{display:none}
  #lb{background:#050506}
  #index{backdrop-filter:none;-webkit-backdrop-filter:none;background:rgba(5,5,6,.98)}
  .mcard .glare{display:none}
}
@media (prefers-reduced-motion:reduce){
  *,*::before,*::after{animation-duration:.01ms!important;animation-iteration-count:1!important;transition-duration:.01ms!important;transition-delay:0s!important;scroll-behavior:auto!important}
  .rv,.rv-stag>*,.wipe,.w-name .ch,.w-copy .eyebrow,.w-sub,.w-cta,.w-meta,.card-stage,.isl,.corner{opacity:1!important;transform:none!important;clip-path:none!important;translate:0 0!important}
  #veil{display:none}
}
@media print{#veil,.isl,.corner,.progress,.cur,.cur2,#index,#lb,#case{display:none!important}.pg{padding-block:40px}.rv,.rv-stag>*,.wipe,.w-name .ch{opacity:1!important;transform:none!important;clip-path:none!important}}
"""
