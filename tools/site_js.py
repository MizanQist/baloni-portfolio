# Behaviour for the Baloni Private Office. Placeholders __SLUG__ etc. are filled by build_site.py.
JS = r"""
(function(){
'use strict';
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>Array.from(r.querySelectorAll(s));
const rm=matchMedia('(prefers-reduced-motion: reduce)').matches;
const touch=matchMedia('(hover: none)').matches;
const fine=matchMedia('(pointer:fine)').matches && innerWidth>=900;
const body=document.body;
let lockY=0, locks=0;
function lockScroll(){ if(locks++>0) return; lockY=window.scrollY||window.pageYOffset||0; body.style.top=(-lockY)+'px'; body.classList.add('locked'); }
function jump(y){ const de=document.documentElement, prev=de.style.scrollBehavior; de.style.scrollBehavior='auto'; window.scrollTo(0,y); de.style.scrollBehavior=prev; }
function unlockScroll(){ if(locks===0||--locks>0) return; body.classList.remove('locked'); body.style.top=''; const y=lockY; jump(y); requestAnimationFrame(()=>{ jump(y); setTimeout(()=>jump(y),60); }); }
const R=s=>(s&&window.__A&&window.__A[s.replace(/^assets\//,'')])||s;
const useM=Math.min(innerWidth,innerHeight)<=700;
const M=s=>(useM&&/^assets\/[\w-]+\.jpg$/.test(s))?s.replace('assets/','assets/m/'):s;
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));

/* ---------- greeting + clock ---------- */
(function(){
  const h=new Date().getHours(), l1=$('#wgreet');
  if(l1) l1.textContent=h<5?'Good evening,':h<12?'Good morning,':h<17?'Good afternoon,':'Good evening,';
  const ck=$('#clock'); if(!ck) return;
  const fmt=new Intl.DateTimeFormat('en-GB',{hour:'2-digit',minute:'2-digit',timeZone:'Africa/Lagos'});
  const tick=()=>{ ck.innerHTML='Abuja <b>'+fmt.format(new Date())+'</b>'; };
  tick(); setInterval(tick,15000);
})();

/* ---------- veil: the invitation is verified ---------- */
const veil=$('#veil'), vline=$('#vline'), vro=$('#vro'), vct=$('#vct'), wname=$('#wname');
const heroReady=()=>true;
let booted=false;
function boot(){
  if(booted) return; booted=true;
  body.classList.add('ready'); veil.classList.add('off');
  const chars=$$('.ch',wname).length;
  setTimeout(()=>wname.classList.add('shine'), rm?0:550+chars*32+1000);
  setActive();
  if(location.hash && $(location.hash)) setTimeout(()=>go(location.hash.slice(1),true), rm?0:700);
}
if(rm){ boot(); }
else{
  const steps=[[0,'Mizan Qist · Private Office'],[.34,'Verifying invitation · <b>'+__CLIENT_CARD__+'</b>'],[.78,'<b>Access granted</b>']];
  const t0=performance.now(), dur=1900; let si=-1;
  const tick=now=>{
    const p=Math.min(1,(now-t0)/dur), e=1-Math.pow(1-p,3);
    vline.style.transform='scaleX('+e+')'; vct.textContent=String(Math.round(e*100)).padStart(3,'0');
    while(si+1<steps.length && p>=steps[si+1][0]){ si++; vro.innerHTML=steps[si][1]; }
    if(p<1) requestAnimationFrame(tick); else setTimeout(boot,420);
  };
  requestAnimationFrame(tick);
  setTimeout(boot,4000);
}

/* ---------- navigation ---------- */
function go(id,instant){
  const el=document.getElementById(id); if(!el) return;
  closeIndex(); closeCase();
  if(id==='welcome') window.scrollTo({top:0,behavior:(instant||rm)?'auto':'smooth'});
  else el.scrollIntoView({behavior:(instant||rm)?'auto':'smooth',block:'start'});
  if(history.replaceState) history.replaceState(null,'','#'+id);
}
let shelfDragged=false;
document.addEventListener('click',e=>{
  const st=e.target.closest('.star'); if(st){ e.preventDefault(); e.stopPropagation(); toggleReq(st.dataset.id, st); return; }
  const rmv=e.target.closest('[data-rm]'); if(rmv){ toggleReq(rmv.dataset.rm); return; }
  const t=e.target.closest('[data-go]'); if(!t) return;
  if(shelfDragged){ e.preventDefault(); return; }
  e.preventDefault(); go(t.dataset.go);
});
document.addEventListener('keydown',e=>{
  if((e.key==='Enter'||e.key===' ')&&e.target.matches('[data-go][tabindex], .gi, .plate, .piece')){
    e.preventDefault();
    if(e.target.matches('.gi, .plate')) openLb(e.target); else if(e.target.matches('.piece')) openCase(e.target.dataset.id); else go(e.target.dataset.go);
  }
});

/* ---------- island nav: indicator + active section ---------- */
const isl=$('#isl'), ind=$('#ind'), tabs=$$('.tab',isl), sections=$$('[data-tab]');
function moveInd(tab){
  if(!tab){ ind.style.opacity='0'; return; }
  ind.style.opacity='1'; ind.style.left=tab.offsetLeft+'px'; ind.style.width=tab.offsetWidth+'px';
}
function setActive(){
  const vh=innerHeight; let cur=null;
  for(const s of sections){ if(s.getBoundingClientRect().top<=vh*0.45) cur=s; }
  const id=cur?cur.dataset.tab:'';
  let on=null; for(const t of tabs){ const is=t.dataset.go===id; t.classList.toggle('on',is); if(is) on=t; }
  moveInd(on);
}
addEventListener('resize',()=>setActive());

/* ---------- index overlay ---------- */
const idx=$('#index');
let lastFocus=null;
function openIndex(){ lastFocus=document.activeElement; idx.classList.add('open'); lockScroll(); setTimeout(()=>$('#idxclose').focus(),50); }
function closeIndex(){ if(!idx.classList.contains('open')) return; idx.classList.remove('open'); unlockScroll(); if(lastFocus&&lastFocus.focus){ try{ lastFocus.focus({preventScroll:true}); }catch(e){} } }
$('#idxbtn').addEventListener('click',()=>idx.classList.contains('open')?closeIndex():openIndex());
$('#idxclose').addEventListener('click',closeIndex);

/* ---------- scroll: progress, parallax, active tab ---------- */
const pbar=$('#pbar'), plates=$$('.plate .pi');
let ticking=false;
function onScroll(){
  if(ticking) return; ticking=true;
  requestAnimationFrame(()=>{
    const vh=innerHeight, y=scrollY, dh=document.documentElement.scrollHeight-vh;
    pbar.style.transform='scaleX('+(dh>0?y/dh:0)+')';
    if(!rm&&!touch) for(const pi of plates){
      const r=pi.parentElement.getBoundingClientRect();
      if(r.bottom<0||r.top>vh) continue;
      const p=clamp((r.top+r.height/2-vh/2)/vh,-1,1);
      pi.style.setProperty('--py',(p*-0.06*r.height).toFixed(1)+'px');
    }
    if(booted) setActive();
    ticking=false;
  });
}
addEventListener('scroll',onScroll,{passive:true}); onScroll();

/* ---------- reveals + counters ---------- */
const rvEls=$$('.rv, .rv-stag, .wipe');
if(rm||!('IntersectionObserver' in window)) rvEls.forEach(el=>el.classList.add('in'));
else{
  const io=new IntersectionObserver(es=>{ for(const en of es) if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); } },{rootMargin:'0px 0px -8% 0px',threshold:0});
  rvEls.forEach(el=>io.observe(el));
}
const cnt=$$('[data-count]');
function runCount(el){
  const to=parseFloat(el.dataset.count), t0=performance.now(), dur=1400;
  const step=now=>{ const p=Math.min(1,(now-t0)/dur), e=1-Math.pow(1-p,3); el.textContent=Math.round(to*e).toLocaleString('en-GB'); if(p<1) requestAnimationFrame(step); };
  requestAnimationFrame(step);
}
if(rm||!('IntersectionObserver' in window)) cnt.forEach(el=>el.textContent=parseFloat(el.dataset.count).toLocaleString('en-GB'));
else{ const io2=new IntersectionObserver(es=>{ for(const en of es) if(en.isIntersecting){ runCount(en.target); io2.unobserve(en.target); } },{threshold:.4}); cnt.forEach(el=>{ el.textContent='0'; io2.observe(el); }); }

/* ---------- the card: it answers to the hand ---------- */
(function(){
  const stage=$('#stage'), card=$('#mcard'); if(!card) return;
  let rx=0, ry=0, tx=0, ty=0, live=false, idle=true, raf=null, down=false, px=0, py=0, bx=0, by=0;
  const set=(x,y)=>{ card.style.setProperty('--rx',x.toFixed(2)+'deg'); card.style.setProperty('--ry',y.toFixed(2)+'deg');
    card.style.setProperty('--sx',(-30+y*3.2)+'%'); card.style.setProperty('--sy',(x*-2.4)+'%');
    card.style.setProperty('--gx',(50+y*2.6)+'%'); card.style.setProperty('--gy',(30-x*2.6)+'%'); };
  const ambient=now=>{ if(!idle||rm) return; const t=now/1000; set(3.2*Math.sin(t/3.1), 7*Math.sin(t/2.3)); raf=requestAnimationFrame(ambient); };
  if(!rm&&!touch) raf=requestAnimationFrame(ambient);
  function aim(cx,cy){ const r=card.getBoundingClientRect(); const dx=(cx-(r.left+r.width/2))/(r.width/2), dy=(cy-(r.top+r.height/2))/(r.height/2); set(clamp(-dy,-1,1)*11, clamp(dx,-1,1)*15); }
  if(!touch){
    stage.addEventListener('pointermove',e=>{ idle=false; if(raf){ cancelAnimationFrame(raf); raf=null; } card.classList.add('live'); aim(e.clientX,e.clientY); });
    stage.addEventListener('pointerleave',()=>{ card.classList.remove('live'); set(0,0); setTimeout(()=>{ idle=true; if(!rm) raf=requestAnimationFrame(ambient); },900); });
  } else {
    card.addEventListener('pointerdown',e=>{ down=true; px=e.clientX; py=e.clientY; card.classList.add('live'); });
    addEventListener('pointermove',e=>{ if(!down) return; const dx=e.clientX-px, dy=e.clientY-py; set(clamp(-dy/9,-14,14), clamp(dx/7,-18,18)); },{passive:true});
    addEventListener('pointerup',()=>{ if(!down) return; down=false; card.classList.remove('live'); set(0,0); });
    addEventListener('pointercancel',()=>{ if(!down) return; down=false; card.classList.remove('live'); set(0,0); });
  }
})();

/* ---------- spotlight + magnetic buttons (fine pointers) ---------- */
if(fine&&!rm){
  const w=$('#welcome');
  w.addEventListener('pointermove',e=>{ const r=w.getBoundingClientRect(); w.style.setProperty('--mx',(e.clientX-r.left)+'px'); w.style.setProperty('--my',(e.clientY-r.top)+'px'); },{passive:true});
  $$('.btn').forEach(b=>{
    b.addEventListener('pointermove',e=>{ const r=b.getBoundingClientRect(); const dx=e.clientX-(r.left+r.width/2), dy=e.clientY-(r.top+r.height/2); b.style.transform='translate('+(dx*.18).toFixed(1)+'px,'+(dy*.28).toFixed(1)+'px)'; });
    b.addEventListener('pointerleave',()=>{ b.style.transform=''; });
  });
}

/* ---------- ledger sort ---------- */
const ledger=$('#ledger tbody');
$$('.sorts button').forEach(b=>b.addEventListener('click',()=>{
  $$('.sorts button').forEach(x=>x.classList.toggle('on',x===b));
  const k=b.dataset.sort, rows=$$('tr',ledger);
  rows.sort((a,c)=>{ const va=parseFloat(a.dataset[k]), vc=parseFloat(c.dataset[k]); return va-vc || parseFloat(a.dataset.n)-parseFloat(c.dataset.n); });
  rows.forEach(r=>ledger.appendChild(r));
}));

/* ---------- shelf ---------- */
const shelf=$('#shelf');
$$('[data-shelf]').forEach(b=>b.addEventListener('click',()=>{ const c=$('.card',shelf); shelf.scrollBy({left:parseInt(b.dataset.shelf)*(c?c.offsetWidth+18:320)*1.5,behavior:rm?'auto':'smooth'}); }));
let sx=0, sl=0, sdown=false;
shelf.addEventListener('pointerdown',e=>{ if(e.pointerType==='touch') return; sdown=true; shelfDragged=false; sx=e.clientX; sl=shelf.scrollLeft; shelf.classList.add('drag'); });
addEventListener('pointermove',e=>{ if(!sdown) return; const dx=e.clientX-sx; if(Math.abs(dx)>6) shelfDragged=true; shelf.scrollLeft=sl-dx; });
addEventListener('pointerup',()=>{ if(!sdown) return; sdown=false; shelf.classList.remove('drag'); setTimeout(()=>shelfDragged=false,50); });

/* ---------- gallery filters ---------- */
$$('.gal-h .groups').forEach(g=>{
  const gal=g.closest('.gal-h').nextElementSibling;
  $$('button',g).forEach(b=>b.addEventListener('click',()=>{
    $$('button',g).forEach(x=>x.classList.toggle('on',x===b));
    const k=b.dataset.g; $$('.gi',gal).forEach(f=>f.classList.toggle('hide',k!=='*'&&f.dataset.g!==k));
  }));
});

/* ---------- the vault: filter, tilt, the case ---------- */
const pieces=$$('.piece'), PIECE={};
pieces.forEach(p=>{ PIECE[p.dataset.id]=p; });
$$('.houses button').forEach(b=>b.addEventListener('click',()=>{
  $$('.houses button').forEach(x=>x.classList.toggle('on',x===b));
  const h=b.dataset.h; pieces.forEach(p=>p.classList.toggle('dim',h!=='*'&&p.dataset.house!==h));
}));
if(fine&&!rm) pieces.forEach(p=>{
  const art=$('.art',p);
  p.addEventListener('pointermove',e=>{ const r=art.getBoundingClientRect(); const dx=(e.clientX-(r.left+r.width/2))/(r.width/2), dy=(e.clientY-(r.top+r.height/2))/(r.height/2); p.classList.add('live'); p.style.setProperty('--px',(clamp(-dy,-1,1)*7).toFixed(2)+'deg'); p.style.setProperty('--pyaw',(clamp(dx,-1,1)*9).toFixed(2)+'deg'); });
  p.addEventListener('pointerleave',()=>{ p.classList.remove('live'); p.style.setProperty('--px','0deg'); p.style.setProperty('--pyaw','0deg'); });
});
const cs=$('#case'), csArt=$('#csart'), csBody=$('#csbody'); let caseOpen=false, caseId=null, caseFocus=null;
const order=pieces.map(p=>p.dataset.id);
function openCase(id){
  const p=PIECE[id]; if(!p) return;
  caseId=id; const d=JSON.parse(p.dataset.spec);
  csArt.innerHTML=''; const art=$('.art svg, .art img',p); if(art){ const c=art.cloneNode(true); c.removeAttribute('style'); csArt.appendChild(c); }
  if(d.placeholder) csArt.insertAdjacentHTML('beforeend','<span class="ph">'+(d.image?'Maker’s photograph · to be sourced':'Blueprint · photograph to follow')+'</span>');
  $('#csk').innerHTML='Piece <b>'+d.n+'</b> · '+d.house;
  const rows=[['Reference',d.ref],['Case',d.case],['Dial',d.dial],['Movement',d.movement],['Power reserve',d.reserve],['Water resistance',d.water],['Strap',d.strap],['Year',d.year],['Condition',d.condition],['Price',d.price,'hi'],['Status',d.status,'hi']];
  csBody.innerHTML='<div class="hs">'+d.house+'</div><h3 class="md">'+d.model+'</h3><div class="rf">'+d.ref+'</div><p class="vw">'+d.view+'</p>'
    +'<dl class="spec">'+rows.map(r=>'<div><dt>'+r[0]+'</dt><dd'+(r[2]?' class="hi"':'')+'>'+r[1]+'</dd></div>').join('')+'</dl>'
    +'<div class="acts"><button type="button" class="btn solid" id="csres" data-res="'+id+'"></button><a class="btn" target="_blank" rel="noopener" id="csask">Ask '+__AGENT_FIRST__+' about this piece <i>'+ARROW+'</i></a></div>'
    +'<p class="fine">'+(d.placeholder?'A placeholder until the piece is secured: the specification is the maker’s for this reference and is confirmed on the piece itself, with box, papers and service history, before any price is quoted.':'Specification as confirmed on the piece.')+'</p>';
  $('#csask').href='https://wa.me/447931814601?text='+encodeURIComponent('Good day '+__AGENT_FIRST__+'. Please tell me more about piece '+d.n+' in my vault: '+d.house+' '+d.model+' ('+d.ref+').\n— '+__SIGNOFF__);
  renderCaseRes();
  if(!caseOpen){ caseFocus=document.activeElement; caseOpen=true; cs.classList.add('open'); lockScroll(); }
  $('.pn',cs).scrollTop=0; setTimeout(()=>$('#csclose').focus(),60);
}
function renderCaseRes(){ const b=$('#csres'); if(!b||!caseId) return; const on=req.includes(caseId); b.innerHTML=(on?'Reserved · remove from requests':'Reserve this piece')+'<i>'+(on?CHECK:STAR)+'</i>'; }
function closeCase(){ if(!caseOpen) return; caseOpen=false; caseId=null; cs.classList.remove('open'); unlockScroll(); if(caseFocus&&caseFocus.focus){ try{ caseFocus.focus({preventScroll:true}); }catch(e){} } }
document.addEventListener('click',e=>{
  const r=e.target.closest('[data-res]'); if(r){ toggleReq(r.dataset.res); renderCaseRes(); return; }
  const p=e.target.closest('.piece'); if(p&&!e.target.closest('.star')){ e.preventDefault(); openCase(p.dataset.id); }
});
$('#csclose').addEventListener('click',closeCase); $('.dim',cs).addEventListener('click',closeCase);
$('#csprev').addEventListener('click',()=>{ const i=order.indexOf(caseId); openCase(order[(i-1+order.length)%order.length]); });
$('#csnext').addEventListener('click',()=>{ const i=order.indexOf(caseId); openCase(order[(i+1)%order.length]); });
cs.addEventListener('touchmove',e=>{ if(caseOpen&&!e.target.closest('.pn')) e.preventDefault(); },{passive:false});

/* ---------- requests (residences and pieces, kept on this device) ---------- */
const KEY=__SLUG__+'.requests';
const META={};
$$('section.dz').forEach(s=>{ META[s.id]={kind:'d',n:s.dataset.n,name:s.dataset.name,sub:$('.run .c',s).textContent.trim()}; });
pieces.forEach(p=>{ const d=JSON.parse(p.dataset.spec); META[p.dataset.id]={kind:'w',n:d.n,name:d.house+' '+d.model,sub:d.ref}; });
let req=[]; try{ req=JSON.parse(localStorage.getItem(KEY)||'[]').filter(id=>META[id]); }catch(e){ req=[]; }
let intent='a private viewing';
function saveReq(){ try{ localStorage.setItem(KEY,JSON.stringify(req)); }catch(e){} }
function toggleReq(id,btn){
  const i=req.indexOf(id); if(i<0) req.push(id); else req.splice(i,1);
  req.sort((a,b)=>(META[a].kind+META[a].n).localeCompare(META[b].kind+META[b].n)); saveReq(); renderReq();
  if(btn){ btn.classList.remove('pop'); void btn.offsetWidth; btn.classList.add('pop'); }
  const n=$('#reqcount'); n.classList.remove('pop'); void n.offsetWidth; n.classList.add('pop');
}
const ARROW='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4"><path d="M4 12h16M13 5l7 7-7 7"/></svg>';
const STAR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.3"><path d="M12 2.5c.9 5.6 3.9 8.6 9.5 9.5-5.6.9-8.6 3.9-9.5 9.5-.9-5.6-3.9-8.6-9.5-9.5 5.6-.9 8.6-3.9 9.5-9.5z"/></svg>';
const CHECK='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12l5 5L19 7"/></svg>';
function message(){
  const h=new Date().getHours(), g=h<12?'Good morning':h<17?'Good afternoon':'Good evening';
  const ds=req.filter(id=>META[id].kind==='d'), ws=req.filter(id=>META[id].kind==='w');
  let t=g+' '+__AGENT_FIRST__+'. I have been through my office.';
  if(ds.length) t+='\n\nResidences:\n'+ds.map(id=>META[id].n+' · '+META[id].name+' ('+META[id].sub+')').join('\n');
  if(ws.length) t+='\n\nThe vault:\n'+ws.map(id=>'Piece '+META[id].n+' · '+META[id].name+' ('+META[id].sub+')').join('\n');
  t+=(req.length?'\n\nPlease arrange ':'\n\nPlease call me about ')+intent+'.\n— '+__SIGNOFF__;
  return t;
}
function renderReq(){
  $$('.star[data-id]').forEach(b=>{ const on=req.includes(b.dataset.id); b.classList.toggle('on',on); b.setAttribute('aria-pressed',on?'true':'false'); });
  $('#reqcount').textContent=req.length?String(req.length):'';
  const list=$('#reqlist'); list.innerHTML=req.map(id=>{ const m=META[id]; return '<li><span class="k">'+(m.kind==='w'?'P·':'')+m.n+'</span><span>'+m.name+'<small>'+m.sub+'</small></span><button type="button" class="rm" data-rm="'+id+'">Remove</button></li>'; }).join('');
  $('#reqempty').hidden=req.length>0;
  const txt=message(); $('#reqprev').textContent=txt;
  $('#reqsend').href='https://wa.me/447931814601?text='+encodeURIComponent(txt);
}
$$('.intent button').forEach(b=>b.addEventListener('click',()=>{ $$('.intent button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false')); intent=b.dataset.i; renderReq(); }));
renderReq();

/* ---------- lightbox ---------- */
const lb=$('#lb'), lbA=$('#lbA'), lbB=$('#lbB'), lbst=$('#lbst');
let lbList=[], lbI=0, lbActive=lbA, lbOpen=false, lbFocus=null, z={s:1,x:0,y:0};
function listFor(id,firstSrc,firstCap){
  const figs=$$('.gi[data-lb="'+id+'"]');
  let list=figs.map(f=>({src:M(R(f.dataset.src)),cap:f.dataset.cap,g:f.dataset.g}));
  if(firstSrc && !list.some(x=>x.src===firstSrc)) list.unshift({src:firstSrc,cap:firstCap,g:'Visualisation'});
  return list;
}
function openLb(el){
  const id=el.dataset.lb, sec=document.getElementById(id);
  const src=M(R(el.dataset.src)), cap=el.dataset.cap||($('.cap',el)?$('.cap',el).textContent:'');
  lbList=listFor(id,src,cap); if(!lbList.length) return;
  lbI=Math.max(0,lbList.findIndex(x=>x.src===src));
  $('#lbsite').textContent=(sec?sec.dataset.n+' · '+sec.dataset.name:'');
  lbFocus=document.activeElement; lbOpen=true; lb.classList.add('open'); lockScroll();
  lbA.classList.remove('on'); lbB.classList.remove('on'); lbA.removeAttribute('src'); lbB.removeAttribute('src'); lbActive=lbB;
  show(lbI); setTimeout(()=>$('#lbclose').focus(),50);
}
function resetZoom(){ z={s:1,x:0,y:0}; lb.classList.remove('zoomed'); [lbA,lbB].forEach(i=>i.style.transform=''); }
function applyZoom(){ lbActive.style.transform='translate('+z.x+'px,'+z.y+'px) scale('+z.s+')'; lb.classList.toggle('zoomed',z.s>1); }
function show(i){
  lbI=(i+lbList.length)%lbList.length; const it=lbList[lbI], myI=lbI;
  resetZoom();
  const next=lbActive===lbA?lbB:lbA, prev=lbActive;
  prev.classList.remove('on');
  const swap=()=>{ let done=false; const on=()=>{ if(done||lbI!==myI) return; done=true; next.classList.add('on'); lbActive=next; }; next.onload=on; next.onerror=on; next.alt=it.cap; next.src=it.src; if(next.complete&&next.naturalWidth) on(); else if(next.decode) next.decode().then(on).catch(()=>{}); };
  setTimeout(swap, rm?0:240);
  $('#lbcap').textContent=it.cap; $('#lbgroup').textContent=it.g; $('#lbct').textContent=String(lbI+1).padStart(2,'0')+' / '+String(lbList.length).padStart(2,'0');
  const pre=new Image(); pre.src=lbList[(lbI+1)%lbList.length].src;
}
function closeLb(){ if(!lbOpen) return; lbOpen=false; lb.classList.remove('open'); unlockScroll(); resetZoom(); if(lbFocus&&lbFocus.focus){ try{ lbFocus.focus({preventScroll:true}); }catch(e){} } }
document.addEventListener('click',e=>{ const t=e.target.closest('.gi, .plate'); if(t){ e.preventDefault(); openLb(t); } });
$('#lbclose').addEventListener('click',closeLb); $('#lbprev').addEventListener('click',()=>show(lbI-1)); $('#lbnext').addEventListener('click',()=>show(lbI+1));
$('#lbzoom').addEventListener('click',()=>{ if(z.s>1) resetZoom(); else { z.s=2.2; applyZoom(); } });
document.addEventListener('keydown',e=>{
  if(e.key==='Escape'){ if(lbOpen) closeLb(); else if(caseOpen) closeCase(); else closeIndex(); }
  if(!lbOpen) return;
  if(e.key==='ArrowRight') show(lbI+1); if(e.key==='ArrowLeft') show(lbI-1);
});
let px=0, py=0, pdown=false, zx=0, zy=0;
lb.addEventListener('touchmove',e=>{ if(lbOpen) e.preventDefault(); },{passive:false});
lbst.addEventListener('pointerdown',e=>{ if(e.target.closest('button')) return; pdown=true; px=e.clientX; py=e.clientY; zx=z.x; zy=z.y; lbst.setPointerCapture(e.pointerId); });
lbst.addEventListener('pointermove',e=>{ if(!pdown) return; const dx=e.clientX-px, dy=e.clientY-py; if(z.s>1){ z.x=zx+dx; z.y=zy+dy; applyZoom(); } });
lbst.addEventListener('pointerup',e=>{ if(!pdown) return; pdown=false; const dx=e.clientX-px; if(z.s>1) return; if(dx<-40) show(lbI+1); else if(dx>40) show(lbI-1); });
lbst.addEventListener('dblclick',e=>{ if(z.s>1) resetZoom(); else { const r=lbst.getBoundingClientRect(); z.s=2.2; z.x=(r.width/2-(e.clientX-r.left))*(z.s-1); z.y=(r.height/2-(e.clientY-r.top))*(z.s-1); applyZoom(); } });
lbst.addEventListener('wheel',e=>{ if(!lbOpen) return; e.preventDefault(); const s=clamp(z.s*(e.deltaY<0?1.12:0.89),1,4); if(s===1){ resetZoom(); return; } z.s=s; applyZoom(); },{passive:false});

/* ---------- map (Leaflet, loaded when near; packed tiles in the preview) ---------- */
(function(){
  const wrap=$('#lmapwrap'); if(!wrap) return;
  const fb=$('#mapfb'), rowsEl=$('#mrows'), rows={}, markers={}; let map=null, booted=false, streets=null, aerial=null, route=null;
  $$('.mrow',rowsEl).forEach(r=>rows[r.dataset.m]=r);
  const D=window.MQ_MAP||[], LM=window.MQ_LM||[], PACK=window.__TILES||null;
  const BLANK='data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7';
  function fail(){ fb.hidden=false; wrap.classList.add('failed'); }
  function loadScript(src,cb){ const el=document.createElement('script'); el.src=src; el.async=true; el.onload=cb; el.onerror=fail; document.head.appendChild(el); }
  function boot(){
    if(booted) return; booted=true;
    if(window.L){ try{ init(); }catch(e){ fail(); if(window.console) console.error(e); } return; }
    let pending=2; const done=()=>{ if(--pending===0){ if(window.L){ try{ init(); }catch(e){ fail(); if(window.console) console.error(e); } } else fail(); } };
    const css=document.createElement('link'); css.rel='stylesheet'; css.href='assets/leaflet/leaflet.css'; css.onload=done; css.onerror=fail; document.head.appendChild(css);
    loadScript('assets/leaflet/leaflet.js',done);
  }
  const lio=new IntersectionObserver(es=>{ if(es.some(e=>e.isIntersecting)){ boot(); lio.disconnect(); } },{rootMargin:'900px 0px'}); lio.observe(wrap);
  const coarse=matchMedia('(pointer:coarse)').matches;
  function init(){
    const maxZ=PACK?16:19;
    map=L.map('lmap',{zoomControl:false,scrollWheelZoom:false,dragging:!coarse,zoomSnap:PACK?1:.5,minZoom:PACK?6:5,maxZoom:maxZ,attributionControl:true});
    map.attributionControl.setPrefix('<a href="https://leafletjs.com" target="_blank" rel="noopener">Leaflet</a>');
    L.control.zoom({position:'topleft'}).addTo(map); L.control.scale({imperial:false,position:'bottomleft',maxWidth:130}).addTo(map);
    const OSM='&copy; <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a> contributors', ESRI='Imagery &copy; Esri, Maxar, Earthstar Geographics';
    if(PACK){
      const Packed=L.TileLayer.extend({getTileUrl:function(c){ return this.options.pack[c.z+'/'+c.x+'/'+c.y]||BLANK; }});
      streets=new Packed('',{pack:PACK.osm,maxZoom:maxZ,attribution:OSM+' · preview map, zoom limited'});
      aerial=PACK.esri?new Packed('',{pack:PACK.esri,maxZoom:maxZ,attribution:ESRI}):null;
    } else {
      streets=L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png',{maxNativeZoom:19,maxZoom:19,attribution:OSM});
      aerial=L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',{maxNativeZoom:19,maxZoom:19,attribution:ESRI});
    }
    if(!aerial) $$('[data-layer]').forEach(b=>b.closest('.seg').hidden=true);
    if(PACK) map.setMaxBounds(L.latLngBounds([[3.0,-1.0],[13.5,15.0]]));
    streets.addTo(map);
    let tilesOk=false; streets.on('tileload',()=>{ tilesOk=true; wrap.classList.add('ready'); }); streets.on('tileerror',()=>{ if(!tilesOk&&!PACK) fail(); });
    setTimeout(()=>{ if(!tilesOk){ if(PACK) wrap.classList.add('ready'); else fail(); } },9000);
    map.on('click',()=>{ map.scrollWheelZoom.enable(); wrap.classList.add('wheel'); });
    map.on('zoomend',()=>wrap.classList.toggle('far',map.getZoom()<13.5)); wrap.classList.add('far');
    LM.forEach(l=>{
      L.marker(l.ll,{icon:L.divIcon({className:'lm-ref'+(l.dest?' dest':''),html:'<i></i><b>'+l.n+'</b>',iconSize:[0,0]}),interactive:true,keyboard:false,zIndexOffset:-100}).addTo(map).bindTooltip(l.n+' · '+l.s,{direction:'top',offset:[0,-8]});
    });
    D.forEach(x=>{
      if(!x.ll) return;
      const ap=x.approx?' ap':'';
      const m=L.marker(x.ll,{icon:L.divIcon({className:'lm-pin'+ap,html:'<i>'+x.n+'</i><b>'+x.name+'</b>',iconSize:[0,0]}),alt:x.name,riseOnHover:true,zIndexOffset:1000}).addTo(map);
      const note=x.approx==='nearest'?'Nearest pin available':x.approx==='street'?'Street-level pin':x.approx==='district'?'District only · exact pin to follow':'';
      const dist=x.route?'<div class="a">'+x.route.km+' km · '+x.route.min+' min to '+(x.city==='Lagos'?'the Eko Hotel':'the Central Business District')+'</div>':'';
      m.bindPopup('<div class="lm-pop"><div class="k">'+x.n+' · '+x.status+'</div><div class="n">'+x.name+'</div><div class="a">'+x.addr+(note?' · '+note:'')+'</div>'+dist+'<div class="p">'+x.price+'</div><div class="x"><a href="#'+x.id+'" data-go="'+x.id+'">Dossier</a><a href="'+x.gmaps+'" target="_blank" rel="noopener">Google Maps</a></div></div>',{maxWidth:300,closeButton:true,offset:[0,-6]});
      m.on('click',()=>select(x.id,false)); markers[x.id]=m;
    });
    fitCity('Abuja',true);
  }
  function drawRoute(x){
    if(route){ map.removeLayer(route); route=null; }
    if(!x||!x.route||!x.route.line) return;
    route=L.layerGroup([L.polyline(x.route.line,{color:'#050506',weight:7,opacity:.55,lineJoin:'round'}),L.polyline(x.route.line,{color:'#efdfb8',weight:3,opacity:.95,lineJoin:'round',dashArray:'1 7',lineCap:'round'})]).addTo(map);
  }
  function fitCity(city,instant){
    let pts;
    if(city==='Maitama') pts=D.filter(x=>x.ll&&x.district==='Maitama').map(x=>x.ll);
    else pts=D.filter(x=>x.ll&&x.city===city).map(x=>x.ll).concat(LM.filter(l=>l.city===city&&l.dest).map(l=>l.ll));
    if(!pts.length) return;
    $$('[data-city]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.city===city?'true':'false'));
    if(pts.length===1){ instant?map.setView(pts[0],15):map.flyTo(pts[0],15,{duration:1.8}); return; }
    const b=L.latLngBounds(pts), o={padding:[44,44],maxZoom:PACK?15:16};
    instant||rm?map.fitBounds(b,o):map.flyToBounds(b,Object.assign({duration:1.6},o));
  }
  function select(id,fly){
    for(const k in rows){ rows[k].setAttribute('aria-pressed',k===id?'true':'false'); rows[k].classList.toggle('on',k===id); const e=markers[k]&&markers[k].getElement(); if(e) e.classList.toggle('on',k===id); }
    const x=D.find(z=>z.id===id); if(!x||!map||!x.ll) return;
    const cityBtn=x.district==='Maitama'?'Maitama':x.city; $$('[data-city]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.city===cityBtn?'true':'false'));
    drawRoute(x);
    const after=()=>markers[id].openPopup();
    if(fly&&!rm){ if(x.route&&x.route.line){ map.flyToBounds(L.latLngBounds(x.route.line),{padding:[60,60],maxZoom:PACK?15:16,duration:1.5}); } else map.flyTo(x.ll,x.approx==='district'?14:15,{duration:1.4}); map.once('moveend',after); }
    else { after(); }
    rows[id].scrollIntoView({block:'nearest',behavior:'smooth'});
  }
  rowsEl.addEventListener('click',e=>{ const r=e.target.closest('.mrow'); if(!r) return; if(!map){ go(r.dataset.m); return; } select(r.dataset.m,true); });
  $$('[data-layer]').forEach(b=>b.addEventListener('click',()=>{ if(!map||!aerial) return; const layer=b.dataset.layer; $$('[data-layer]').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false')); wrap.classList.toggle('aerial',layer==='aerial'); if(layer==='aerial'){ map.removeLayer(streets); aerial.addTo(map); } else { map.removeLayer(aerial); streets.addTo(map); } }));
  $$('[data-city]').forEach(b=>b.addEventListener('click',()=>{ if(!map) return; drawRoute(null); map.closePopup(); for(const k in rows){ rows[k].setAttribute('aria-pressed','false'); rows[k].classList.remove('on'); const e=markers[k]&&markers[k].getElement(); if(e) e.classList.remove('on'); } fitCity(b.dataset.city,false); }));
})();

/* ---------- cursor ---------- */
const cur=$('#cur'), cur2=$('#cur2');
if(fine && !rm){
  let mx=-100,my=-100,cx=-100,cy=-100,raf=null;
  const loop=()=>{ cx+=(mx-cx)*.18; cy+=(my-cy)*.18; cur2.style.left=cx+'px'; cur2.style.top=cy+'px'; raf=(Math.abs(mx-cx)+Math.abs(my-cy)>.2)?requestAnimationFrame(loop):null; };
  addEventListener('pointermove',e=>{ mx=e.clientX; my=e.clientY; cur.style.left=mx+'px'; cur.style.top=my+'px'; if(!raf) raf=requestAnimationFrame(loop);
    const t=e.target.closest('.gi, .plate, .card .pl, .piece, .mcard, .shelf');
    let l=''; if(t){ l=t.matches('.piece')?'Open':t.matches('.mcard')?'Tilt':t.matches('.shelf')?'Drag':'View'; }
    const big=!lbOpen&&!caseOpen&&!!t; cur2.classList.toggle('big',big); cur.classList.toggle('hide',big); if(l) cur2.dataset.l=l; },{passive:true});
  document.addEventListener('mouseleave',()=>{ cur.style.opacity='0'; cur2.style.opacity='0'; }); document.addEventListener('mouseenter',()=>{ cur.style.opacity='1'; cur2.style.opacity='1'; });
}
})();
"""
