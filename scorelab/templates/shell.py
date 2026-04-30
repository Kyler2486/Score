import os, uuid
from flask import render_template_string, session
from flask_login import current_user
from scorelab.app import AVATAR_DIR, BANNER_DIR, ALLOWED_IMAGE

BASE_CSS = """
:root{--bg:#0f1117;--card:#1e2130;--border:#2d3348;--text:#e2e8f0;
  --text-muted:#94a3b8;--text-faint:#64748b;--text-xfaint:#475569;
  --input-bg:#151822;--hover-bg:#2d3348;--nav-bg:#1e2130;
  --accent:#6366f1;--accent-h:#4f46e5;--accent-text:#818cf8;--stat-bg:#151822;
  --sidebar-w:240px;}
[data-theme="light"]{--bg:#f1f5f9;--card:#ffffff;--border:#e2e8f0;--text:#0f172a;
  --text-muted:#475569;--text-faint:#64748b;--text-xfaint:#94a3b8;
  --input-bg:#f8fafc;--hover-bg:#f1f5f9;--nav-bg:#ffffff;
  --accent:#6366f1;--accent-h:#4f46e5;--accent-text:#4f46e5;--stat-bg:#f1f5f9;}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif;
  background:var(--bg);color:var(--text);min-height:100vh;
  display:flex;flex-direction:column;transition:background .2s,color .2s}
a{color:var(--accent-text);text-decoration:none}
a:hover{text-decoration:underline}
nav{width:100%;background:var(--nav-bg);border-bottom:1px solid var(--border);
  padding:12px 20px;display:flex;align-items:center;gap:12px;
  transition:background .2s,border-color .2s;flex-shrink:0;z-index:100}
.hamburger{background:none;border:none;cursor:pointer;padding:6px;
  display:flex;flex-direction:column;gap:5px;border-radius:6px;
  transition:background .15s}
.hamburger:hover{background:var(--hover-bg)}
.hamburger span{display:block;width:20px;height:2px;background:var(--text-muted);
  border-radius:2px;transition:all .25s}
.nav-brand{font-size:1.05rem;font-weight:700;color:var(--text);cursor:pointer;
  user-select:none;flex:1}
.nav-right{display:flex;align-items:center;gap:12px}
.nav-avatar{width:34px;height:34px;border-radius:50%;border:2px solid var(--border);
  display:flex;align-items:center;justify-content:center;
  background:var(--hover-bg);font-size:.9rem;color:var(--accent-text);font-weight:700;
  overflow:hidden;flex-shrink:0;transition:border-color .2s;cursor:pointer;
  text-decoration:none}
.nav-avatar img{width:100%;height:100%;object-fit:cover;display:block}
.nav-avatar:hover{border-color:var(--accent);text-decoration:none}
.nav-names{display:flex;flex-direction:column;align-items:flex-end;gap:1px}
.nav-display{color:var(--accent-text);font-weight:600;font-size:.88rem}
.nav-username{color:var(--text-xfaint);font-size:.74rem}
.nav-btn{padding:5px 12px;background:transparent;border:1px solid var(--border);
  border-radius:7px;color:var(--text-muted);font-size:.8rem;cursor:pointer;
  transition:background .15s,color .15s;white-space:nowrap}
.nav-btn:hover{background:var(--hover-bg);color:var(--text);text-decoration:none}
.app-layout{display:flex;flex:1;min-height:0;overflow:hidden}
.sidebar{width:var(--sidebar-w);min-width:var(--sidebar-w);background:var(--card);
  border-right:1px solid var(--border);transition:width .25s,min-width .25s,opacity .2s;
  overflow:hidden;display:flex;flex-direction:column;flex-shrink:0}
.sidebar.collapsed{width:0;min-width:0;opacity:0}
.sidebar-inner{width:var(--sidebar-w);padding:12px 10px;display:flex;flex-direction:column;gap:2px}
.sidebar-section{font-size:.68rem;font-weight:700;text-transform:uppercase;
  letter-spacing:.1em;color:var(--text-xfaint);padding:14px 8px 5px;margin-top:4px}
.sidebar-section:first-child{padding-top:6px}
.sidebar-item{display:flex;align-items:center;gap:10px;padding:8px 10px;border-radius:8px;
  font-size:.86rem;color:var(--text-muted);transition:background .15s,color .15s;
  white-space:nowrap;text-decoration:none}
.sidebar-item:hover{background:var(--hover-bg);color:var(--text);text-decoration:none}
.sidebar-item.active{background:var(--accent);color:#fff}
.sidebar-item.active:hover{background:var(--accent-h)}
.sidebar-icon{font-size:.95rem;width:20px;text-align:center;flex-shrink:0}
.page-content{flex:1;min-width:0;overflow-y:auto;overflow-x:hidden;display:flex;flex-direction:column;align-items:center}
.page-inner{width:100%;max-width:820px;padding:36px 24px;box-sizing:border-box;flex-shrink:0}
.page-title{font-size:1.6rem;font-weight:700;color:var(--text);margin-bottom:6px}
.page-sub{color:var(--text-muted);font-size:.93rem;margin-bottom:28px}
.card{background:var(--card);border:1px solid var(--border);border-radius:14px;padding:28px;margin-bottom:20px}
.card-title{font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.09em;
  color:var(--text-xfaint);margin-bottom:16px}
label{display:block;font-size:.84rem;color:var(--text-muted);margin-bottom:6px}
.hint{font-size:.77rem;color:var(--text-xfaint);margin-top:-10px;margin-bottom:14px}
input[type=text],input[type=email],input[type=password],input[type=number],input[type=file],select{
  width:100%;padding:10px 13px;background:var(--input-bg);border:1px solid var(--border);
  border-radius:8px;color:var(--text);font-size:.93rem;outline:none;
  transition:border-color .2s,background .2s;margin-bottom:14px}
input[type=file],select{cursor:pointer}
input:focus,select:focus{border-color:var(--accent)}
.btn{display:block;width:100%;padding:12px;background:var(--accent);color:#fff;
  font-size:.95rem;font-weight:600;border:none;border-radius:10px;cursor:pointer;
  transition:background .2s;margin-top:4px}
.btn:hover{background:var(--accent-h)}
.btn.secondary{background:transparent;border:1px solid var(--border);
  color:var(--text-muted);margin-top:8px}
.btn.secondary:hover{background:var(--hover-bg);color:var(--text)}
.btn-sm{display:inline-block;padding:7px 16px;width:auto;font-size:.83rem;margin-top:0}
.flash{padding:10px 15px;border-radius:8px;font-size:.87rem;margin-bottom:16px}
.flash.error{background:#2d1b1b;border:1px solid #7f1d1d;color:#fca5a5}
.flash.success{background:#14261f;border:1px solid #166534;color:#86efac}
.toast{position:fixed;bottom:24px;right:24px;background:#22c55e;color:#fff;
  padding:9px 16px;border-radius:8px;font-size:.86rem;font-weight:500;
  opacity:0;transform:translateY(8px);transition:opacity .2s,transform .2s;pointer-events:none}
.toast.show{opacity:1;transform:translateY(0)}
textarea{width:100%;height:340px;background:var(--input-bg);border:1px solid var(--border);
  border-radius:10px;padding:14px;color:var(--text);
  font-family:"Fira Code","Courier New",monospace;font-size:.82rem;
  line-height:1.6;resize:vertical;outline:none;transition:border-color .2s}
textarea:focus{border-color:var(--accent)}
"""

THEME_SCRIPT = """<script>
(function(){var t=localStorage.getItem('theme')||'dark';
document.documentElement.setAttribute('data-theme',t);})();</script>"""

SIDEBAR_JS = """<script>
(function(){
  var sb=document.getElementById('sidebar');
  var open=localStorage.getItem('sidebar')!=='0';
  if(!open)sb.classList.add('collapsed');
  document.getElementById('hamburger').addEventListener('click',function(){
    open=!open;localStorage.setItem('sidebar',open?'1':'0');
    sb.classList.toggle('collapsed',!open);
  });

  /* Inject installed extensions into sidebar dynamically */
  var EXT_META={
    'scale-finder':     {icon:'🎼',name:'Scale Finder',        url:'/ext/scale-finder'},
    'circle-of-fifths': {icon:'⭕',name:'Circle of Fifths',    url:'/ext/circle-of-fifths'},
    'pitch-detector':   {icon:'🎤',name:'Pitch Detector',      url:'/ext/pitch-detector'},
    'rhythm-trainer':   {icon:'🥁',name:'Rhythm Trainer',      url:'/ext/rhythm-trainer'},
    'ear-training':     {icon:'👂',name:'Ear Training',        url:'/ext/ear-training'},
    'notation-guide':   {icon:'📖',name:'Notation Reference',  url:'/ext/notation-guide'},
    'freq-calculator':  {icon:'🔢',name:'Freq Calculator',     url:'/ext/freq-calculator'},
    'time-sig-trainer': {icon:'📐',name:'Time Sig Trainer',    url:'/ext/time-sig-trainer'},
    'chord-progression':{icon:'🎹',name:'Chord Progressions',  url:'/ext/chord-progression'},
    'tuner':            {icon:'🎸',name:'Chromatic Tuner',     url:'/ext/tuner'},
    'solfege':          {icon:'🎵',name:'Solfege Trainer',     url:'/ext/solfege'},
    'form-analyzer':    {icon:'🔍',name:'Form Analyzer',       url:'/ext/form-analyzer'},
    'piano-keyboard':   {icon:'🎹',name:'Piano Keyboard',      url:'/ext/piano-keyboard'},
    'metronome-visual': {icon:'📊',name:'Visual Metronome',    url:'/ext/metronome-visual'},
    'music-quiz':       {icon:'🧠',name:'Theory Quiz',         url:'/ext/music-quiz'},
    'tempo-converter':  {icon:'⚡',name:'Tempo Converter',     url:'/ext/tempo-converter'},
    'midi-player':      {icon:'🎹',name:'MIDI Player',          url:'/ext/midi-player'},
    'note-reading':     {icon:'🎼',name:'Note Reading',         url:'/ext/note-reading'},
    'guitar-tuner':     {icon:'🎸',name:'Guitar Tuner',         url:'/ext/guitar-tuner'},
    'drum-machine':     {icon:'🥁',name:'Drum Machine',         url:'/ext/drum-machine'},
    'arpeggiator':      {icon:'🎵',name:'Arpeggiator',          url:'/ext/arpeggiator'},
    'music-flashcards': {icon:'🃏',name:'Music Flashcards',     url:'/ext/music-flashcards'},
  };
  var installed=JSON.parse(localStorage.getItem('installedExtensions')||'[]');
  if(installed.length){
    var inner=document.querySelector('.sidebar-inner');
    var logoutForm=inner.querySelector('form[action="/logout"]');
    var extSection=document.createElement('div');
    extSection.className='sidebar-section';extSection.textContent='Extensions';
    inner.insertBefore(extSection,logoutForm.previousElementSibling);
    installed.forEach(function(id){
      var m=EXT_META[id];if(!m)return;
      var a=document.createElement('a');a.className='sidebar-item';a.href=m.url;
      a.innerHTML='<span class="sidebar-icon">'+m.icon+'</span>'+m.name;
      inner.insertBefore(a,logoutForm.previousElementSibling);
    });
  }

  var path=window.location.pathname;
  document.querySelectorAll('.sidebar-item').forEach(function(a){
    var href=a.getAttribute('href');
    if(href===path||(path.startsWith(href)&&href!=='/')){a.classList.add('active');}
    else if(href==='/'&&path==='/'){a.classList.add('active');}
  });
})();
</script>"""

EASTER_EGG_JS = """<script>
(function(){
  function eggToast(msg,dur){
    var el=document.getElementById('eggToast');
    if(!el){el=document.createElement('div');el.id='eggToast';
      Object.assign(el.style,{position:'fixed',bottom:'80px',left:'50%',
        transform:'translateX(-50%) translateY(20px)',background:'#6366f1',
        color:'#fff',padding:'11px 20px',borderRadius:'12px',fontWeight:'600',
        fontSize:'1rem',zIndex:'9999',opacity:'0',
        transition:'opacity .3s,transform .3s',pointerEvents:'none',
        boxShadow:'0 8px 24px rgba(99,102,241,.4)',whiteSpace:'nowrap'});
      document.body.appendChild(el);}
    el.textContent=msg;el.style.opacity='1';el.style.transform='translateX(-50%) translateY(0)';
    clearTimeout(el._t);el._t=setTimeout(function(){
      el.style.opacity='0';el.style.transform='translateX(-50%) translateY(20px)';},dur||3000);}

  /* Konami code → note rain */
  var kk=[38,38,40,40,37,39,37,39,66,65],ks=['ArrowUp','ArrowUp','ArrowDown','ArrowDown','ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'],ki=0;
  document.addEventListener('keydown',function(e){
    var match=(e.keyCode===kk[ki]||e.key===ks[ki]);
    if(match){ki++;if(ki===kk.length){ki=0;noteRain();}}else{ki=0;if(e.keyCode===kk[0]||e.key===ks[0])ki=1;}});
  function noteRain(){
    var n='♩♪♫♬𝅘𝅥𝅮𝄞',s=document.createElement('style');
    if(!document.getElementById('nkf')){s.id='nkf';
      s.textContent='@keyframes nf{to{top:110vh;opacity:0;transform:rotate(720deg)}}';
      document.head.appendChild(s);}
    for(var i=0;i<40;i++){(function(i){setTimeout(function(){
      var el=document.createElement('div');
      el.textContent=n[Math.floor(Math.random()*n.length)];
      Object.assign(el.style,{position:'fixed',left:Math.random()*100+'vw',top:'-40px',
        fontSize:(1.5+Math.random()*2.5)+'rem',
        color:'hsl('+Math.floor(Math.random()*60+230)+',80%,70%)',
        zIndex:'9998',pointerEvents:'none',animation:'nf '+(2+Math.random()*2)+'s linear forwards'});
      document.body.appendChild(el);setTimeout(function(){el.remove();},4500);},i*80);})(i);}
    eggToast('🎵 Achievement Unlocked: Konami Composer!',4000);}

  /* Logo ×5 → disco */
  var lc=0,lt;
  document.addEventListener('DOMContentLoaded',function(){
    var b=document.querySelector('.nav-brand');if(!b)return;
    b.addEventListener('click',function(){
      lc++;clearTimeout(lt);lt=setTimeout(function(){lc=0;},1500);
      if(lc>=5){lc=0;disco();}});});
  function disco(){
    var cols=['#f43f5e','#f97316','#eab308','#22c55e','#06b6d4','#6366f1','#a855f7'],i=0,
        el=document.body,ot=el.style.transition;
    el.style.transition='background .15s';
    var iv=setInterval(function(){el.style.background=cols[i%cols.length];i++;},150);
    setTimeout(function(){clearInterval(iv);el.style.background='';el.style.transition=ot;},3000);
    eggToast('🪩 DISCO MODE ACTIVATED',3000);}

  /* Avatar ×7 → spin — single click navigates after short delay, 7 rapid clicks spins */
  var ac=0,at,navT;
  document.addEventListener('DOMContentLoaded',function(){
    var av=document.getElementById('navAvatar');if(!av)return;
    av.addEventListener('click',function(){
      ac++;clearTimeout(at);clearTimeout(navT);
      at=setTimeout(function(){ac=0;},1200);
      if(ac>=7){
        ac=0;spinAv(av);
      } else {
        navT=setTimeout(function(){
          window.location.href='/profile';
        },320);
      }
    });});
  function spinAv(av){if(av._s)return;av._s=true;
    var s=document.createElement('style');
    s.textContent='.nav-avatar{animation:avs 1s ease-in-out 3!important}'
      +'@keyframes avs{0%{transform:rotate(0) scale(1)}50%{transform:rotate(180deg) scale(1.3)}100%{transform:rotate(360deg) scale(1)}}';
    document.head.appendChild(s);eggToast('😵‍💫 Dizzy!',2000);
    setTimeout(function(){s.remove();av._s=false;},3200);}

  /* Type "music" anywhere */
  var typed='';
  document.addEventListener('keypress',function(e){
    typed=(typed+e.key).slice(-5);
    if(typed==='music')eggToast('🔍 Try visiting /secret …',4000);});

  /* Type "clef" → clef rain */
  var typed2='';
  document.addEventListener('keypress',function(e){
    typed2=(typed2+e.key).slice(-4);
    if(typed2==='clef'){clefRain();}});
  function clefRain(){
    var clefs=['𝄞','𝄢','𝄡','𝄣','𝄤'],s=document.createElement('style');
    if(!document.getElementById('clef-kf')){s.id='clef-kf';
      s.textContent='@keyframes cleff{0%{opacity:1;top:-60px}100%{opacity:0;top:110vh}}';
      document.head.appendChild(s);}
    for(var i=0;i<25;i++){(function(i){setTimeout(function(){
      var el=document.createElement('div');
      el.textContent=clefs[Math.floor(Math.random()*clefs.length)];
      Object.assign(el.style,{position:'fixed',left:Math.random()*100+'vw',top:'-60px',
        fontSize:(2+Math.random()*3)+'rem',
        color:'hsl('+Math.floor(Math.random()*40+40)+',90%,65%)',
        zIndex:'9998',pointerEvents:'none',
        animation:'cleff '+(2.5+Math.random()*2)+'s linear forwards'});
      document.body.appendChild(el);setTimeout(function(){el.remove();},5000);},i*120);})(i);}
    eggToast('𝄞 Clef rain! You speak music.',3500);}

  /* Double-click nav brand → Matrix music rain */
  document.addEventListener('DOMContentLoaded',function(){
    var b=document.querySelector('.nav-brand');if(!b)return;
    b.addEventListener('dblclick',function(){matrixRain();});});
  function matrixRain(){
    var canvas=document.createElement('canvas');
    Object.assign(canvas.style,{position:'fixed',inset:'0',zIndex:'9990',
      pointerEvents:'none',opacity:'0.7'});
    canvas.width=window.innerWidth;canvas.height=window.innerHeight;
    document.body.appendChild(canvas);
    var ctx=canvas.getContext('2d'),cols=Math.floor(canvas.width/16),
        drops=Array(cols).fill(1);
    var chars='♩♪♫♬𝄞𝄢ABCDEFG#b♮';
    var iv=setInterval(function(){
      ctx.fillStyle='rgba(15,17,23,0.05)';ctx.fillRect(0,0,canvas.width,canvas.height);
      ctx.fillStyle='#6366f1';ctx.font='14px monospace';
      drops.forEach(function(y,i){
        var ch=chars[Math.floor(Math.random()*chars.length)];
        ctx.fillText(ch,i*16,y*16);
        if(y*16>canvas.height&&Math.random()>0.975) drops[i]=0;
        drops[i]++;});},50);
    setTimeout(function(){clearInterval(iv);canvas.remove();},5000);
    eggToast('🎹 Matrix Music Mode',3000);}

  /* Idle hint */
  if(window.location.pathname==='/'){
    var msgs=['Try the Konami Code ↑↑↓↓←→←→BA 🎮',
      'Click the 🎵 logo 5 times for a surprise…',
      'Visit /secret if you dare 👀',
      'Click your avatar 7 times quickly…',
      'Type "clef" for a musical surprise 𝄞',
      'Double-click the logo for Matrix mode 💊'];
    setTimeout(function(){eggToast(msgs[Math.floor(Math.random()*msgs.length)],5000);},45000);}
})();</script>"""

# ── Shared shell ──────────────────────────────────────────────────────────────

SIDEBAR_HTML = """
<aside class="sidebar" id="sidebar">
  <div class="sidebar-inner">
    <div class="sidebar-section">Tools</div>
    <a class="sidebar-item" href="/"><span class="sidebar-icon">🎵</span>MusicXML → Text</a>
    <a class="sidebar-item" href="/tools/mxl"><span class="sidebar-icon">📦</span>MXL → XML</a>
    <a class="sidebar-item" href="/tools/metadata"><span class="sidebar-icon">📋</span>Metadata Viewer</a>
    <a class="sidebar-item" href="/tools/transpose"><span class="sidebar-icon">🎼</span>Transpose</a>
    <a class="sidebar-item" href="/tools/stats"><span class="sidebar-icon">📊</span>Note Statistics</a>
    <a class="sidebar-item" href="/tools/interval"><span class="sidebar-icon">🎯</span>Interval Trainer</a>
    <a class="sidebar-item" href="/tools/chord"><span class="sidebar-icon">🎸</span>Chord Reference</a>
    <a class="sidebar-item" href="/tools/bpm"><span class="sidebar-icon">🥁</span>BPM Tapper</a>
    <a class="sidebar-item" href="/tools/metronome"><span class="sidebar-icon">⏱️</span>Metronome</a>
    <a class="sidebar-item" href="/tools/viewer"><span class="sidebar-icon">🎶</span>Sheet Music Viewer</a>
    <a class="sidebar-item" href="/tools/tuner"><span class="sidebar-icon">🎸</span>Chromatic Tuner</a>
    <a class="sidebar-item" href="/tools/oscilloscope"><span class="sidebar-icon">📡</span>Oscilloscope</a>
    <a class="sidebar-item" href="/extensions"><span class="sidebar-icon">🧩</span>Extensions</a>
    <div class="sidebar-section">Account</div>
    <a class="sidebar-item" href="/profile"><span class="sidebar-icon">👤</span>Profile</a>
    <a class="sidebar-item" href="/settings"><span class="sidebar-icon">⚙️</span>Settings</a>
    {% if current_user.is_admin %}<a class="sidebar-item" href="/admin"><span class="sidebar-icon">🛡️</span>Admin Panel</a>{% endif %}
    <form method="POST" action="/logout" style="margin:0">
      <button type="submit" style="background:none;border:none;width:100%;text-align:left;cursor:pointer;padding:0">
        <span class="sidebar-item" style="display:flex"><span class="sidebar-icon">🚪</span>Log out</span>
      </button>
    </form>
  </div>
</aside>"""

NAV_HTML = """
<nav>
  <button class="hamburger" id="hamburger" aria-label="Toggle sidebar">
    <span></span><span></span><span></span>
  </button>
  <span class="nav-brand" title="Click 5× for disco, dbl-click for Matrix 💊">🎵 ScoreLab</span>
  <div class="nav-right">
    <div class="nav-avatar" id="navAvatar" title="Click 7 times quickly…" style="cursor:pointer">
      {% if avatar_url %}<img src="{{ avatar_url }}" alt="av"/>
      {% else %}{{ display_name[0].upper() }}{% endif %}
    </div>
    <div class="nav-names">
      <span class="nav-display">{{ display_name }}</span>
      <span class="nav-username">@{{ username }}</span>
    </div>
  </div>
</nav>"""

def make_shell(content_tpl, extra_css='', extra_js='', **ctx):
    full = (
        '<!DOCTYPE html><html lang="en"><head>'
        + THEME_SCRIPT
        + '<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>'
        + '<title>ScoreLab</title>'
        + f'<style>{BASE_CSS}{extra_css}</style>'
        + '</head><body>'
        + NAV_HTML
        + '<div class="app-layout">'
        + SIDEBAR_HTML
        + '<div class="page-content"><div class="page-inner">'
        + content_tpl
        + '</div></div></div>'
        + '<div class="toast" id="toast"></div>'
        + SIDEBAR_JS + EASTER_EGG_JS + extra_js
        + '</body></html>'
    )
    return render_template_string(full, **ctx)

def nav_ctx(user=None):
    u = user or current_user
    return dict(display_name=u.display_name, username=u.username, avatar_url=u.avatar_url)

def save_upload(f, directory, user_id):
    ext = f.filename.rsplit('.', 1)[-1].lower()
    if ext not in ALLOWED_IMAGE: return None, 'Unsupported file type.'
    filename = f"{user_id}_{uuid.uuid4().hex[:8]}.{ext}"
    f.save(os.path.join(directory, filename)); return filename, None

def delete_file(directory, filename):
    if filename:
        try: os.remove(os.path.join(directory, filename))
        except FileNotFoundError: pass


def ext_stub(icon, name, desc):
    return (
        '<div class="page-title">'+icon+' '+name+'</div>'
        +'<p class="page-sub">'+desc+'</p>'
        +'<div class="card" style="text-align:center;padding:48px 28px">'
        +'<div style="font-size:3.5rem;margin-bottom:14px">'+icon+'</div>'
        +'<div style="font-size:1.1rem;font-weight:700;color:var(--text);margin-bottom:8px">Coming soon</div>'
        +'<div style="color:var(--text-muted);max-width:400px;margin:0 auto">This extension is installed. Full functionality coming soon.</div>'
        +'</div>')
