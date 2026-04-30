from scorelab.templates.shell import BASE_CSS, THEME_SCRIPT, EASTER_EGG_JS

EXTENSIONS_CSS = """
.ext-hero{text-align:center;padding:8px 0 28px}
.ext-hero h2{font-size:1.1rem;color:var(--text-muted);font-weight:400;margin-top:6px}
.ext-tabs{display:flex;gap:4px;margin-bottom:24px;background:var(--input-bg);
  border:1px solid var(--border);border-radius:10px;padding:4px}
.ext-tab{flex:1;padding:8px;text-align:center;border-radius:7px;font-size:.85rem;
  font-weight:500;cursor:pointer;transition:background .15s,color .15s;
  border:none;background:transparent;color:var(--text-muted)}
.ext-tab.active{background:var(--accent);color:#fff}
.ext-tab:hover:not(.active){background:var(--hover-bg);color:var(--text)}
.ext-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:16px}
.ext-card{background:var(--card);border:1px solid var(--border);border-radius:14px;
  padding:20px;display:flex;flex-direction:column;gap:10px;transition:border-color .2s,transform .15s}
.ext-card:hover{border-color:var(--accent);transform:translateY(-2px)}
.ext-card-top{display:flex;align-items:flex-start;gap:12px}
.ext-icon{font-size:2rem;line-height:1;flex-shrink:0;width:48px;height:48px;
  display:flex;align-items:center;justify-content:center;
  background:var(--input-bg);border-radius:10px;border:1px solid var(--border)}
.ext-info{flex:1;min-width:0}
.ext-name{font-size:.95rem;font-weight:700;color:var(--text)}
.ext-author{font-size:.74rem;color:var(--text-xfaint);margin-top:2px}
.ext-desc{font-size:.82rem;color:var(--text-faint);line-height:1.5}
.ext-tags{display:flex;flex-wrap:wrap;gap:5px}
.ext-tag{font-size:.72rem;padding:2px 8px;background:var(--input-bg);
  border:1px solid var(--border);border-radius:999px;color:var(--text-faint)}
.ext-footer{display:flex;align-items:center;justify-content:space-between;margin-top:4px}
.ext-rating{font-size:.78rem;color:var(--text-faint)}
.ext-install-btn{padding:6px 16px;border-radius:7px;font-size:.82rem;font-weight:600;
  border:none;cursor:pointer;transition:background .15s}
.ext-install-btn.install{background:var(--accent);color:#fff}
.ext-install-btn.install:hover{background:var(--accent-h)}
.ext-install-btn.installed{background:var(--input-bg);color:#22c55e;border:1px solid #166534}
.ext-install-btn.installed:hover{background:#14261f;color:#86efac}
.ext-badge-new{display:inline-block;background:#1e1b4b;border:1px solid #4338ca;
  color:#a5b4fc;border-radius:999px;padding:1px 7px;font-size:.68rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;margin-left:6px;vertical-align:middle}
.ext-badge-hot{display:inline-block;background:#422006;border:1px solid #92400e;
  color:#fde68a;border-radius:999px;padding:1px 7px;font-size:.68rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.06em;margin-left:6px;vertical-align:middle}
.ext-search{margin-bottom:18px}
.ext-search input{margin-bottom:0}
.installed-section{margin-bottom:28px}
.installed-empty{text-align:center;padding:32px;color:var(--text-faint);font-size:.9rem}
"""

EXTENSIONS_CONTENT = """
<div class="page-title">Extensions <span style="font-size:1rem;color:var(--text-faint);font-weight:400">Store</span></div>
<p class="page-sub">Add extra tools to your sidebar. Extensions are saved to your browser and don't require a reload.</p>

<div class="ext-tabs">
  <button class="ext-tab active" id="tabAll" onclick="showTab('all')">🧩 All Extensions</button>
  <button class="ext-tab" id="tabInstalled" onclick="showTab('installed')">✅ Installed</button>
</div>

<div id="panelAll">
  <div class="ext-search">
    <input type="text" id="extSearch" placeholder="Search extensions…" style="margin-bottom:0"/>
  </div>
  <div class="ext-grid" id="extGrid"></div>
</div>

<div id="panelInstalled" style="display:none">
  <div id="installedList"></div>
</div>

<script>
(function(){
  var EXTENSIONS=[
    {id:'scale-finder',icon:'🎼',name:'Scale Finder',author:'ScoreLab',
     desc:'Type any note and get all scales that contain it, with degrees highlighted.',
     tags:['theory','scales','reference'],rating:'4.8',badge:'hot',
     url:'/tools/scale-finder'},
    {id:'circle-of-fifths',icon:'⭕',name:'Circle of Fifths',author:'ScoreLab',
     desc:'Interactive circle of fifths — click any key to see its relatives, chords, and notes.',
     tags:['theory','visual','reference'],rating:'4.9',badge:'hot',
     url:'/tools/circle-of-fifths'},
    {id:'pitch-detector',icon:'🎤',name:'Pitch Detector',author:'ScoreLab',
     desc:'Use your microphone to detect the pitch of notes you sing or play in real time.',
     tags:['audio','mic','detection'],rating:'4.5',badge:'new',
     url:'/tools/pitch-detector'},
    {id:'rhythm-trainer',icon:'🥁',name:'Rhythm Trainer',author:'ScoreLab',
     desc:'Tap along to rhythmic patterns displayed on screen. Great for developing your sense of time.',
     tags:['rhythm','training','interactive'],rating:'4.6',
     url:'/tools/rhythm-trainer'},
    {id:'ear-training',icon:'👂',name:'Ear Training Suite',author:'ScoreLab',
     desc:'Full ear training: chord quality ID, melody dictation, and harmonic progression recognition.',
     tags:['training','ear','chords'],rating:'4.7',badge:'new',
     url:'/tools/ear-training'},
    {id:'notation-guide',icon:'📖',name:'Notation Reference',author:'ScoreLab',
     desc:'A searchable guide to music notation symbols, Italian terms, and dynamic markings.',
     tags:['reference','notation','symbols'],rating:'4.4',
     url:'/tools/notation-guide'},
    {id:'freq-calculator',icon:'🔢',name:'Frequency Calculator',author:'ScoreLab',
     desc:'Convert between note names, MIDI numbers, and Hz frequencies. Supports custom temperaments.',
     tags:['math','frequency','midi'],rating:'4.3',
     url:'/tools/freq-calc'},
    {id:'time-sig-trainer',icon:'📐',name:'Time Sig Trainer',author:'ScoreLab',
     desc:'Practice identifying and conducting common and odd time signatures.',
     tags:['rhythm','training','time'],rating:'4.5',
     url:'/tools/time-sig'},
    {id:'chord-progression',icon:'🎹',name:'Chord Progression Builder',author:'ScoreLab',
     desc:'Build and play back chord progressions with Roman numeral analysis and voice leading.',
     tags:['chords','theory','composition'],rating:'4.8',badge:'hot',
     url:'/tools/progression'},
    {id:'tuner',icon:'🎸',name:'Chromatic Tuner',author:'ScoreLab',
     desc:'Microphone-based chromatic tuner with cents display. Works for any instrument.',
     tags:['tuner','mic','audio'],rating:'4.9',badge:'hot',
     url:'/tools/tuner'},
    {id:'solfege',icon:'🎵',name:'Solfège Trainer',author:'ScoreLab',
     desc:'Practice Do-Re-Mi solfège sight-singing with both fixed and moveable-do systems.',
     tags:['solfège','vocal','training'],rating:'4.2',
     url:'/tools/solfege'},
    {id:'form-analyzer',icon:'🔍',name:'Form Analyzer',author:'ScoreLab',
     desc:'Upload a MusicXML file and get an automatic analysis of the musical form (ABA, AABB, etc.).',
     tags:['analysis','musicxml','form'],rating:'4.1',badge:'new',
     url:'/ext/form-analyzer'},
    {id:'piano-keyboard',icon:'🎹',name:'Piano Keyboard',author:'ScoreLab',
     desc:'Playable on-screen piano. Computer keyboard support (A=C, W=C#, S=D...). Multiple sounds and chord shortcuts.',
     tags:['piano','interactive','keyboard'],rating:'4.7',badge:'new',
     url:'/ext/piano-keyboard'},
    {id:'metronome-visual',icon:'📊',name:'Visual Metronome',author:'ScoreLab',
     desc:'A pendulum-style visual metronome with color flash on the beat and tap tempo support.',
     tags:['metronome','visual','tempo'],rating:'4.5',
     url:'/ext/metronome-visual'},
    {id:'music-quiz',icon:'🧠',name:'Music Theory Quiz',author:'ScoreLab',
     desc:'25+ questions: note names, key signatures, intervals, chords, rhythm, terminology. Score and streak tracking.',
     tags:['quiz','theory','education'],rating:'4.6',badge:'hot',
     url:'/ext/music-quiz'},
    {id:'tempo-converter',icon:'⚡',name:'Tempo Converter',author:'ScoreLab',
     desc:'Convert BPM to note durations in ms and Hz, plus equivalent tempos across beat units.',
     tags:['tempo','math','utility'],rating:'4.3',
     url:'/ext/tempo-converter'},
    {id:'midi-player',icon:'🎹',name:'MIDI Player',author:'ScoreLab',
     desc:'Upload any .mid file to play it back with a piano roll visualizer, live keyboard, per-track mute, and tempo display.',
     tags:['midi','player','piano roll'],rating:'4.8',badge:'hot',
     url:'/ext/midi-player'},
    {id:'guitar-tuner',icon:'🎸',name:'Guitar Tuner',author:'ScoreLab',
     desc:'Standard and alternate guitar tunings with a chromatic tuner and string-by-string guide.',
     tags:['guitar','tuner','strings'],rating:'4.6',badge:'new',
     url:'/ext/guitar-tuner'},
    {id:'drum-machine',icon:'🥁',name:'Drum Machine',author:'ScoreLab',
     desc:'16-step drum sequencer with kick, snare, hi-hat, and more. Program grooves and adjust tempo.',
     tags:['drums','sequencer','rhythm'],rating:'4.9',badge:'hot',
     url:'/ext/drum-machine'},
    {id:'arpeggiator',icon:'🎵',name:'Arpeggiator',author:'ScoreLab',
     desc:'Pick a chord and pattern, hear it arpeggiated in real time. Great for composition ideas.',
     tags:['arpeggio','composition','chords'],rating:'4.5',
     url:'/ext/arpeggiator'},
    {id:'music-flashcards',icon:'🃏',name:'Music Flashcards',author:'ScoreLab',
     desc:'Spaced repetition flashcards for note names, key signatures, intervals, and chord symbols.',
     tags:['flashcards','theory','study'],rating:'4.4',
     url:'/ext/music-flashcards'},
  ];

  var installed=JSON.parse(localStorage.getItem('installedExtensions')||'[]');

  function isInstalled(id){return installed.indexOf(id)!==-1;}

  function install(id){
    if(!isInstalled(id)){installed.push(id);localStorage.setItem('installedExtensions',JSON.stringify(installed));}
    renderAll();renderInstalled();
    showToast('🧩 Extension installed!');
  }
  function uninstall(id){
    installed=installed.filter(function(x){return x!==id;});
    localStorage.setItem('installedExtensions',JSON.stringify(installed));
    renderAll();renderInstalled();
    showToast('Extension removed');
  }
  function showToast(msg){
    var t=document.getElementById('toast');if(!t)return;
    t.textContent=msg;t.classList.add('show');setTimeout(function(){t.classList.remove('show');},2000);}

  function extCard(ext){
    var inst=isInstalled(ext.id);
    var badge=ext.badge==='hot'?'<span class="ext-badge-hot">HOT</span>'
               :ext.badge==='new'?'<span class="ext-badge-new">NEW</span>':'';
    var div=document.createElement('div');div.className='ext-card';
    div.innerHTML='<div class="ext-card-top">'
      +'<div class="ext-icon">'+ext.icon+'</div>'
      +'<div class="ext-info"><div class="ext-name">'+ext.name+badge+'</div>'
      +'<div class="ext-author">by '+ext.author+'</div></div></div>'
      +'<div class="ext-desc">'+ext.desc+'</div>'
      +'<div class="ext-tags">'+ext.tags.map(function(t){return'<span class="ext-tag">'+t+'</span>';}).join('')+'</div>'
      +'<div class="ext-footer"><span class="ext-rating">★ '+ext.rating+'</span>'
      +'<button class="ext-install-btn '+(inst?'installed':'install')+'" data-id="'+ext.id+'">'
      +(inst?'✓ Installed':'+ Install')+'</button></div>';
    div.querySelector('.ext-install-btn').addEventListener('click',function(){
      if(isInstalled(ext.id))uninstall(ext.id);else install(ext.id);});
    return div;
  }

  function renderAll(){
    var q=(document.getElementById('extSearch')||{value:''}).value.toLowerCase();
    var grid=document.getElementById('extGrid');grid.innerHTML='';
    EXTENSIONS.filter(function(e){
      return !q||e.name.toLowerCase().includes(q)||e.desc.toLowerCase().includes(q)||e.tags.join(' ').includes(q);
    }).forEach(function(e){grid.appendChild(extCard(e));});
  }

  function renderInstalled(){
    var el=document.getElementById('installedList');el.innerHTML='';
    var list=EXTENSIONS.filter(function(e){return isInstalled(e.id);});
    if(!list.length){el.innerHTML='<div class="installed-empty">No extensions installed yet.<br>Browse the store to add some!</div>';return;}
    var grid=document.createElement('div');grid.className='ext-grid';
    list.forEach(function(e){grid.appendChild(extCard(e));});
    el.appendChild(grid);
  }

  window.showTab=function(tab){
    document.getElementById('tabAll').classList.toggle('active',tab==='all');
    document.getElementById('tabInstalled').classList.toggle('active',tab==='installed');
    document.getElementById('panelAll').style.display=tab==='all'?'':'none';
    document.getElementById('panelInstalled').style.display=tab==='installed'?'':'none';
    if(tab==='installed')renderInstalled();
  };

  document.getElementById('extSearch').addEventListener('input',renderAll);
  renderAll();
})();
</script>
"""

# ── Landing page (public, no login required) ─────────────────────────────────
LANDING_TEMPLATE = """<!DOCTYPE html><html lang="en"><head>
""" + THEME_SCRIPT + """
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>ScoreLab — The Musician's Toolkit</title>
<style>
""" + BASE_CSS + """
body{align-items:stretch;padding:0}
.land-nav{width:100%;background:var(--nav-bg);border-bottom:1px solid var(--border);
  padding:14px 32px;display:flex;align-items:center;gap:16px;flex-shrink:0}
.land-logo{font-size:1.15rem;font-weight:800;color:var(--text);flex:1}
.land-nav-btns{display:flex;gap:10px}
.land-btn{padding:8px 20px;border-radius:8px;font-size:.88rem;font-weight:600;cursor:pointer;transition:all .15s;text-decoration:none;display:inline-block}
.land-btn.outline{background:transparent;border:1px solid var(--border);color:var(--text-muted)}
.land-btn.outline:hover{background:var(--hover-bg);color:var(--text);text-decoration:none}
.land-btn.solid{background:var(--accent);border:1px solid var(--accent);color:#fff}
.land-btn.solid:hover{background:var(--accent-h);text-decoration:none}
/* Hero */
.hero{text-align:center;padding:80px 24px 60px;position:relative;overflow:hidden}
.hero::before{content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 0%,rgba(99,102,241,.18),transparent 65%);pointer-events:none}
.hero-badge{display:inline-block;background:#1e1b4b;border:1px solid #4338ca;color:#a5b4fc;
  border-radius:999px;padding:5px 16px;font-size:.78rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.08em;margin-bottom:20px}
.hero h1{font-size:clamp(2.2rem,5vw,3.8rem);font-weight:800;color:var(--text);
  line-height:1.1;margin-bottom:18px;letter-spacing:-.02em}
.hero h1 span{color:var(--accent-text)}
.hero p{font-size:1.1rem;color:var(--text-muted);max-width:560px;margin:0 auto 32px;line-height:1.6}
.hero-btns{display:flex;gap:12px;justify-content:center;flex-wrap:wrap}
.hero-btn{padding:14px 32px;border-radius:12px;font-size:1rem;font-weight:700;
  cursor:pointer;transition:all .2s;text-decoration:none;display:inline-block}
.hero-btn.primary{background:var(--accent);color:#fff;border:none}
.hero-btn.primary:hover{background:var(--accent-h);transform:translateY(-2px);text-decoration:none}
.hero-btn.secondary{background:transparent;color:var(--text-muted);border:1px solid var(--border)}
.hero-btn.secondary:hover{background:var(--hover-bg);color:var(--text);text-decoration:none}
.hero-note{font-size:7rem;position:absolute;opacity:.05;user-select:none;pointer-events:none}
.hero-note.n1{top:20px;left:5%}
.hero-note.n2{top:40px;right:8%;font-size:5rem}
.hero-note.n3{bottom:10px;left:15%;font-size:4rem}
/* Tools grid */
.features{padding:0 24px 60px;max-width:1080px;margin:0 auto}
.features h2{font-size:1.5rem;font-weight:700;color:var(--text);text-align:center;margin-bottom:8px}
.features .sub{text-align:center;color:var(--text-muted);margin-bottom:36px;font-size:.95rem}
.feat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px}
.feat-card{background:var(--card);border:1px solid var(--border);border-radius:14px;
  padding:20px 18px;transition:border-color .2s,transform .15s}
.feat-card:hover{border-color:var(--accent);transform:translateY(-3px)}
.feat-icon{font-size:2rem;margin-bottom:10px}
.feat-name{font-size:.95rem;font-weight:700;color:var(--text);margin-bottom:5px}
.feat-desc{font-size:.8rem;color:var(--text-faint);line-height:1.5}
/* Stats */
.stats-row{display:flex;justify-content:center;gap:40px;flex-wrap:wrap;
  padding:40px 24px;background:var(--card);border-top:1px solid var(--border);
  border-bottom:1px solid var(--border);margin:0 0 60px}
.stat-item{text-align:center}
.stat-item .num{font-size:2.2rem;font-weight:800;color:var(--accent-text)}
.stat-item .lbl{font-size:.82rem;color:var(--text-faint);margin-top:4px}
/* CTA */
.cta{text-align:center;padding:60px 24px 80px}
.cta h2{font-size:1.8rem;font-weight:800;color:var(--text);margin-bottom:12px}
.cta p{color:var(--text-muted);margin-bottom:28px;font-size:.95rem}
/* Footer */
footer{text-align:center;padding:24px;color:var(--text-xfaint);font-size:.82rem;
  border-top:1px solid var(--border)}
</style>
</head><body>

<nav class="land-nav">
  <div class="land-logo">🎵 ScoreLab</div>
  <div class="land-nav-btns">
    <a href="/login" class="land-btn outline">Log in</a>
    <a href="/register" class="land-btn solid">Get started free</a>
  </div>
</nav>

<div class="hero">
  <div class="hero-note n1">𝄞</div>
  <div class="hero-note n2">♪</div>
  <div class="hero-note n3">♫</div>
  <div class="hero-badge">🎹 Free · No credit card</div>
  <h1>The toolkit every<br/><span>musician needs</span></h1>
  <p>Convert MusicXML files, train your ear, tune your instrument, explore chords, and more — all in your browser.</p>
  <div class="hero-btns">
    <a href="/register" class="hero-btn primary">Start for free →</a>
    <a href="/login" class="hero-btn secondary">Log in</a>
  </div>
</div>

<div class="stats-row">
  <div class="stat-item"><div class="num">10+</div><div class="lbl">Built-in Tools</div></div>
  <div class="stat-item"><div class="num">12+</div><div class="lbl">Extensions</div></div>
  <div class="stat-item"><div class="num">100%</div><div class="lbl">Browser-based</div></div>
  <div class="stat-item"><div class="num">0</div><div class="lbl">Cost</div></div>
</div>

<div class="features">
  <h2>Everything you need</h2>
  <p class="sub">A growing suite of music tools, all in one place.</p>
  <div class="feat-grid">
    <div class="feat-card"><div class="feat-icon">🎵</div><div class="feat-name">MusicXML → Text</div><div class="feat-desc">Parse any MusicXML file into clean text for AI or analysis.</div></div>
    <div class="feat-card"><div class="feat-icon">🎶</div><div class="feat-name">Sheet Music Viewer</div><div class="feat-desc">Render and play back MusicXML scores directly in your browser.</div></div>
    <div class="feat-card"><div class="feat-icon">🎼</div><div class="feat-name">Transpose</div><div class="feat-desc">Shift any MusicXML file up or down by semitones and download it.</div></div>
    <div class="feat-card"><div class="feat-icon">🎯</div><div class="feat-name">Interval Trainer</div><div class="feat-desc">Hear piano intervals and train your ear to identify them.</div></div>
    <div class="feat-card"><div class="feat-icon">🎸</div><div class="feat-name">Chord Reference</div><div class="feat-desc">Browse and hear every chord type for any root note.</div></div>
    <div class="feat-card"><div class="feat-icon">⏱️</div><div class="feat-name">Metronome</div><div class="feat-desc">Precision Web Audio metronome with presets and multiple sounds.</div></div>
    <div class="feat-card"><div class="feat-icon">📊</div><div class="feat-name">Note Statistics</div><div class="feat-desc">Analyze note frequency and duration distributions in a score.</div></div>
    <div class="feat-card"><div class="feat-icon">🧩</div><div class="feat-name">Extensions</div><div class="feat-desc">Install extra tools from the extensions store.</div></div>
  </div>
</div>

<div class="cta">
  <h2>Ready to play?</h2>
  <p>Create a free account and start using every tool instantly.</p>
  <a href="/register" class="hero-btn primary">Get started — it's free</a>
</div>

<footer>
  🎵 ScoreLab · Built for musicians · <a href="/login">Log in</a> · <a href="/register">Sign up</a>
</footer>

""" + EASTER_EGG_JS + """
</body></html>"""



# ── Extension content templates ───────────────────────────────────────────────

EXT_SCALE_FINDER = """
<div class="page-title">🎼 Scale Finder</div>
<p class="page-sub">Pick a root note and scale type to see all the notes and hear it played.</p>
<div class="card">
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin-bottom:20px">
    <div style="flex:1;min-width:120px"><label>Root Note</label>
      <select id="sfRoot" style="margin-bottom:0">
        <option>C</option><option>C#</option><option>D</option><option>D#</option>
        <option>E</option><option>F</option><option>F#</option><option>G</option>
        <option>G#</option><option>A</option><option>A#</option><option>B</option>
      </select></div>
    <div style="flex:2;min-width:180px"><label>Scale Type</label>
      <select id="sfType" style="margin-bottom:0">
        <option value="major">Major</option><option value="natural_minor">Natural Minor</option>
        <option value="harmonic_minor">Harmonic Minor</option><option value="melodic_minor">Melodic Minor</option>
        <option value="dorian">Dorian</option><option value="phrygian">Phrygian</option>
        <option value="lydian">Lydian</option><option value="mixolydian">Mixolydian</option>
        <option value="locrian">Locrian</option><option value="pentatonic_major">Pentatonic Major</option>
        <option value="pentatonic_minor">Pentatonic Minor</option><option value="blues">Blues</option>
        <option value="whole_tone">Whole Tone</option><option value="chromatic">Chromatic</option>
      </select></div>
  </div>
  <button class="btn" id="sfPlayBtn" style="margin-bottom:20px">\u25b6 Play Scale</button>
  <div id="sfResult"></div>
</div>
<script>
(function(){
  var SCALES={
    major:{intervals:[0,2,4,5,7,9,11,12],degrees:['1','2','3','4','5','6','7','8']},
    natural_minor:{intervals:[0,2,3,5,7,8,10,12],degrees:['1','2','b3','4','5','b6','b7','8']},
    harmonic_minor:{intervals:[0,2,3,5,7,8,11,12],degrees:['1','2','b3','4','5','b6','7','8']},
    melodic_minor:{intervals:[0,2,3,5,7,9,11,12],degrees:['1','2','b3','4','5','6','7','8']},
    dorian:{intervals:[0,2,3,5,7,9,10,12],degrees:['1','2','b3','4','5','6','b7','8']},
    phrygian:{intervals:[0,1,3,5,7,8,10,12],degrees:['1','b2','b3','4','5','b6','b7','8']},
    lydian:{intervals:[0,2,4,6,7,9,11,12],degrees:['1','2','3','#4','5','6','7','8']},
    mixolydian:{intervals:[0,2,4,5,7,9,10,12],degrees:['1','2','3','4','5','6','b7','8']},
    locrian:{intervals:[0,1,3,5,6,8,10,12],degrees:['1','b2','b3','4','b5','b6','b7','8']},
    pentatonic_major:{intervals:[0,2,4,7,9,12],degrees:['1','2','3','5','6','8']},
    pentatonic_minor:{intervals:[0,3,5,7,10,12],degrees:['1','b3','4','5','b7','8']},
    blues:{intervals:[0,3,5,6,7,10,12],degrees:['1','b3','4','b5','5','b7','8']},
    whole_tone:{intervals:[0,2,4,6,8,10,12],degrees:['1','2','3','#4','#5','b7','8']},
    chromatic:{intervals:[0,1,2,3,4,5,6,7,8,9,10,11,12],degrees:['1','b2','2','b3','3','4','b5','5','b6','6','b7','7','8']},
  };
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null,currentNotes=[];
  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function noteFreq(semi){return 261.63*Math.pow(2,semi/12);}
  function pianoNote(ctx,freq,startAt,dur,vol){
    var master=ctx.createGain();master.connect(ctx.destination);
    var end=startAt+dur;master.gain.setValueAtTime(0,startAt);master.gain.linearRampToValueAtTime(vol,startAt+0.005);master.gain.exponentialRampToValueAtTime(vol*0.3,startAt+0.12);master.gain.setValueAtTime(vol*0.3,end-0.15);master.gain.exponentialRampToValueAtTime(0.0001,end);
    [{m:1,a:1},{m:2,a:.55},{m:3,a:.28},{m:4,a:.14}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=freq*h.m;g.gain.value=h.a;g.gain.setValueAtTime(h.a,startAt);g.gain.exponentialRampToValueAtTime(h.a*(h.m===1?.7:.04),startAt+0.1*h.m*.6);o.connect(g);g.connect(master);o.start(startAt);o.stop(end+0.1);});}
  function render(){
    var rootIdx=NOTES.indexOf(document.getElementById('sfRoot').value);
    var scale=SCALES[document.getElementById('sfType').value];
    currentNotes=scale.intervals.map(function(s,i){return{semi:rootIdx+s,name:NOTES[(rootIdx+s)%12],deg:scale.degrees[i]};});
    var html='<div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px">';
    currentNotes.forEach(function(n){
      var isRoot=(n.deg==='1'||n.deg==='8');
      html+='<div style="text-align:center;background:'+(isRoot?'var(--accent)':'var(--input-bg)')+';border:1px solid '+(isRoot?'var(--accent)':'var(--border)')+';border-radius:10px;padding:12px 16px;min-width:52px">'
        +'<div style="font-size:1.1rem;font-weight:700;color:'+(isRoot?'#fff':'var(--accent-text)')+'">'+n.name+'</div>'
        +'<div style="font-size:.72rem;color:'+(isRoot?'rgba(255,255,255,.7)':'var(--text-faint)')+'">'+n.deg+'</div></div>';
    });
    html+='</div>';
    var steps=[];for(var i=0;i<scale.intervals.length-1;i++){var d=scale.intervals[i+1]-scale.intervals[i];steps.push(d===1?'H':d===2?'W':'W+'+(d-2));}
    html+='<div style="font-size:.82rem;color:var(--text-faint)">Formula: <span style="color:var(--accent-text);font-family:monospace">'+steps.join(' - ')+'</span></div>';
    document.getElementById('sfResult').innerHTML=html;
  }
  document.getElementById('sfRoot').addEventListener('change',render);
  document.getElementById('sfType').addEventListener('change',render);
  document.getElementById('sfPlayBtn').addEventListener('click',function(){
    var ctx=getCtx(),now=ctx.currentTime;
    currentNotes.forEach(function(n,i){pianoNote(ctx,noteFreq(n.semi-12),now+i*0.32,0.55,0.45);});
  });
  render();
})();
</script>
"""

EXT_CIRCLE_CSS = """
.cof-info{background:var(--input-bg);border:1px solid var(--border);border-radius:12px;padding:16px;min-height:80px;margin-top:16px}
.cof-info h3{font-size:1rem;font-weight:700;color:var(--accent-text);margin-bottom:8px}
.cof-note-pills{display:flex;flex-wrap:wrap;gap:6px}
.cof-pill{padding:4px 10px;border-radius:6px;font-size:.82rem;font-weight:600;background:var(--stat-bg);border:1px solid var(--border);color:var(--text-muted)}
.cof-pill.major{background:var(--accent);color:#fff;border-color:var(--accent)}
"""

EXT_CIRCLE_CONTENT = """
<div class="page-title">\u2b55 Circle of Fifths</div>
<p class="page-sub">Click any key to see its notes, relative minor, and diatonic chords.</p>
<div class="card">
  <div style="display:flex;flex-direction:column;align-items:center">
    <svg id="cofSvg" viewBox="0 0 400 400" width="340" height="340" style="cursor:pointer"></svg>
    <div class="cof-info" id="cofInfo" style="width:100%"><div style="color:var(--text-faint);font-size:.9rem">Click a key to explore it.</div></div>
  </div>
</div>
<script>
(function(){
  var MAJOR=['C','G','D','A','E','B','F#','C#','Ab','Eb','Bb','F'];
  var MINOR=['Am','Em','Bm','F#m','C#m','G#m','D#m','A#m','Fm','Cm','Gm','Dm'];
  var KEY_NOTES={'C':['C','D','E','F','G','A','B'],'G':['G','A','B','C','D','E','F#'],'D':['D','E','F#','G','A','B','C#'],'A':['A','B','C#','D','E','F#','G#'],'E':['E','F#','G#','A','B','C#','D#'],'B':['B','C#','D#','E','F#','G#','A#'],'F#':['F#','G#','A#','B','C#','D#','F'],'C#':['C#','D#','F','F#','G#','A#','C'],'Ab':['Ab','Bb','C','Db','Eb','F','G'],'Eb':['Eb','F','G','Ab','Bb','C','D'],'Bb':['Bb','C','D','Eb','F','G','A'],'F':['F','G','A','Bb','C','D','E']};
  var CHORDS_ROMAN=['I','ii','iii','IV','V','vi','vii\u00b0'];
  var CHORDS_Q=['','m','m','','','m','\u00b0'];
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null,selected=null;
  var svg=document.getElementById('cofSvg'),cx=200,cy=200;
  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function noteFreq(semi){return 261.63*Math.pow(2,semi/12);}
  function pianoNote(ctx,freq,start,dur,vol){var master=ctx.createGain();master.connect(ctx.destination);var end=start+dur;master.gain.setValueAtTime(0,start);master.gain.linearRampToValueAtTime(vol,start+0.005);master.gain.exponentialRampToValueAtTime(vol*0.3,start+0.12);master.gain.setValueAtTime(vol*0.3,end-0.15);master.gain.exponentialRampToValueAtTime(0.0001,end);[{m:1,a:1},{m:2,a:.55},{m:3,a:.28}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=freq*h.m;g.gain.value=h.a;o.connect(g);g.connect(master);o.start(start);o.stop(end+0.1);});}
  function polar(a,r){return{x:cx+r*Math.cos(a),y:cy+r*Math.sin(a)};}
  function buildCircle(){
    svg.innerHTML='';
    var bg=document.createElementNS('http://www.w3.org/2000/svg','circle');bg.setAttribute('cx',cx);bg.setAttribute('cy',cy);bg.setAttribute('r',190);bg.setAttribute('fill','var(--card)');bg.setAttribute('stroke','var(--border)');bg.setAttribute('stroke-width','1');svg.appendChild(bg);
    for(var i=0;i<12;i++){
      var a=(i/12)*Math.PI*2-Math.PI/2,na=((i+1)/12)*Math.PI*2-Math.PI/2,mid=(a+na)/2;
      var p=function(ang,r){return polar(ang,r);};
      function addSlice(r1,r2,fill,stroke,idx){
        var pts=[p(a,r2),p(na,r2),p(na,r1),p(a,r1)];
        var path=document.createElementNS('http://www.w3.org/2000/svg','path');
        path.setAttribute('d','M '+pts[0].x+' '+pts[0].y+' A '+r2+' '+r2+' 0 0 1 '+pts[1].x+' '+pts[1].y+' L '+pts[2].x+' '+pts[2].y+' A '+r1+' '+r1+' 0 0 0 '+pts[3].x+' '+pts[3].y+' Z');
        path.setAttribute('fill',fill);path.setAttribute('stroke',stroke||'var(--border)');path.setAttribute('stroke-width','1.5');
        path.setAttribute('data-idx',idx);path.style.cursor='pointer';
        path.addEventListener('click',function(){selectKey(parseInt(this.getAttribute('data-idx')));});
        svg.appendChild(path);
      }
      addSlice(125,185,selected===i?'var(--accent)':'var(--input-bg)',null,i);
      addSlice(88,123,selected===i?'#1e1b4b':'var(--stat-bg)','var(--border)',i);
      function addLabel(ang,r,text,size,weight,fill,pEvents){
        var lp=polar(ang,r),t=document.createElementNS('http://www.w3.org/2000/svg','text');
        t.setAttribute('x',lp.x);t.setAttribute('y',lp.y);t.setAttribute('text-anchor','middle');t.setAttribute('dominant-baseline','middle');
        t.setAttribute('font-size',size||'14');t.setAttribute('font-weight',weight||'700');t.setAttribute('fill',fill||'var(--text)');if(pEvents)t.setAttribute('pointer-events','none');
        t.textContent=text;svg.appendChild(t);}
      addLabel(mid,155,MAJOR[i],'14','700',selected===i?'#fff':'var(--text)',true);
      addLabel(mid,106,MINOR[i],'10','500',selected===i?'#a5b4fc':'var(--text-muted)',true);
    }
    var cc=document.createElementNS('http://www.w3.org/2000/svg','circle');cc.setAttribute('cx',cx);cc.setAttribute('cy',cy);cc.setAttribute('r',86);cc.setAttribute('fill','var(--card)');cc.setAttribute('stroke','var(--border)');cc.setAttribute('stroke-width','1');svg.appendChild(cc);
    var ct=document.createElementNS('http://www.w3.org/2000/svg','text');ct.setAttribute('x',cx);ct.setAttribute('y',cy);ct.setAttribute('text-anchor','middle');ct.setAttribute('dominant-baseline','middle');ct.setAttribute('font-size','11');ct.setAttribute('fill','var(--text-faint)');ct.textContent='Circle of Fifths';svg.appendChild(ct);
  }
  function selectKey(idx){
    selected=idx;buildCircle();
    var key=MAJOR[idx],notes=KEY_NOTES[key]||[];
    var ctx=getCtx(),now=ctx.currentTime;
    var ri=NOTES.indexOf(key.replace('b',''));if(ri<0){var en={'Ab':'G#','Eb':'D#','Bb':'A#'};ri=NOTES.indexOf(en[key])||0;}
    [0,4,7].forEach(function(s,j){pianoNote(ctx,noteFreq(ri+s),now+j*0.03,1.2,0.32);});
    var info=document.getElementById('cofInfo');
    info.innerHTML='<h3>'+key+' Major &nbsp;<span style="font-size:.8rem;color:var(--text-faint);font-weight:400">relative: '+MINOR[idx]+'</span></h3>'
      +'<div class="cof-note-pills" style="margin-bottom:10px">'+notes.map(function(n,i){return'<span class="cof-pill'+(i===0?' major':'')+'">'+n+'</span>';}).join('')+'</div>'
      +'<div style="font-size:.78rem;color:var(--text-faint);margin-bottom:5px">Diatonic chords:</div>'
      +'<div class="cof-note-pills">'+notes.map(function(n,i){return'<span class="cof-pill'+(i===0?' major':'')+'">'+n+CHORDS_Q[i]+'<sub style="font-size:.65rem"> '+CHORDS_ROMAN[i]+'</sub></span>';}).join('')+'</div>';
  }
  buildCircle();
})();
</script>
"""

EXT_TUNER_CONTENT = """
<div class="page-title">🎸 Chromatic Tuner</div>
<p class="page-sub">Play or sing any note — the tuner detects its pitch in real time using your microphone.</p>
<div class="card" style="text-align:center">
  <div id="tunerStatus" style="color:var(--text-faint);font-size:.9rem;margin-bottom:20px">Click Start to begin</div>
  <div style="font-size:5rem;font-weight:800;color:var(--accent-text);line-height:1;margin-bottom:4px" id="tunerNote">\u2014</div>
  <div style="font-size:1rem;color:var(--text-muted);margin-bottom:20px" id="tunerOctave"></div>
  <div style="position:relative;height:28px;background:var(--input-bg);border:1px solid var(--border);border-radius:14px;overflow:hidden;margin:0 auto 6px;max-width:380px">
    <div style="position:absolute;left:50%;top:0;bottom:0;width:2px;background:var(--border);transform:translateX(-50%)"></div>
    <div id="centsBar" style="position:absolute;height:100%;width:3px;background:var(--accent);border-radius:14px;left:50%;transition:left .08s"></div>
  </div>
  <div style="display:flex;justify-content:space-between;max-width:380px;margin:0 auto 16px;font-size:.75rem;color:var(--text-faint)">
    <span>-50\u00a2</span><span id="centsLabel">0\u00a2</span><span>+50\u00a2</span>
  </div>
  <div id="tunerInTune" style="font-size:1rem;font-weight:700;min-height:28px;margin-bottom:20px"></div>
  <div style="display:flex;gap:10px;justify-content:center">
    <button class="btn btn-sm" id="tunerStart" style="width:auto;padding:10px 28px">🎤 Start</button>
    <button class="btn btn-sm secondary" id="tunerStop" style="width:auto;padding:10px 28px;margin-top:0" disabled>Stop</button>
  </div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null,analyser=null,stream=null,rafId=null,buf=null;
  function freqToNote(freq){var n=12*Math.log2(freq/440)+69,midi=Math.round(n),cents=Math.round((n-midi)*100);return{name:NOTES[((midi%12)+12)%12],octave:Math.floor(midi/12)-1,cents:cents};}
  function autoCorrelate(buf,sr){
    var N=buf.length,M=Math.floor(N/2),rms=0;
    for(var i=0;i<N;i++)rms+=buf[i]*buf[i];rms=Math.sqrt(rms/N);if(rms<0.01)return -1;
    var best=-1,bestC=-1,lastC=1,found=false;
    for(var o=0;o<M;o++){var c=0;for(var i=0;i<M;i++)c+=Math.abs(buf[i]-buf[i+o]);c=1-(c/M);
      if(c>0.9&&c>lastC){found=true;if(c>bestC){bestC=c;best=o;}}else if(found)break;lastC=c;}
    return best<0?-1:sr/best;
  }
  function tick(){
    analyser.getFloatTimeDomainData(buf);
    var freq=autoCorrelate(buf,audioCtx.sampleRate);
    if(freq>80&&freq<2000){
      var n=freqToNote(freq);
      document.getElementById('tunerNote').textContent=n.name;
      document.getElementById('tunerOctave').textContent='Octave '+n.octave+' \u00b7 '+Math.round(freq)+' Hz';
      var pct=50+n.cents;if(pct<2)pct=2;if(pct>98)pct=98;
      var bar=document.getElementById('centsBar');bar.style.left=pct+'%';
      bar.style.background=Math.abs(n.cents)<=5?'#22c55e':Math.abs(n.cents)<=15?'#eab308':'#ef4444';
      document.getElementById('centsLabel').textContent=(n.cents>=0?'+':'')+n.cents+'\u00a2';
      var el=document.getElementById('tunerInTune');
      if(Math.abs(n.cents)<=5){el.textContent='\u2705 In tune!';el.style.color='#22c55e';}
      else if(n.cents<0){el.textContent='\u25b2 Tune up '+Math.abs(n.cents)+'\u00a2';el.style.color='#eab308';}
      else{el.textContent='\u25bc Tune down '+n.cents+'\u00a2';el.style.color='#eab308';}
      document.getElementById('tunerStatus').textContent='Listening\u2026';
    } else {
      document.getElementById('tunerNote').textContent='\u2014';
      document.getElementById('tunerOctave').textContent='';document.getElementById('tunerInTune').textContent='';
    }
    rafId=requestAnimationFrame(tick);
  }
  document.getElementById('tunerStart').addEventListener('click',function(){
    navigator.mediaDevices.getUserMedia({audio:true,video:false}).then(function(s){
      stream=s;audioCtx=new(window.AudioContext||window.webkitAudioContext)();
      analyser=audioCtx.createAnalyser();analyser.fftSize=2048;buf=new Float32Array(analyser.fftSize);
      audioCtx.createMediaStreamSource(s).connect(analyser);
      document.getElementById('tunerStart').disabled=true;document.getElementById('tunerStop').disabled=false;
      tick();
    }).catch(function(e){document.getElementById('tunerStatus').textContent='Mic denied: '+e.message;});
  });
  document.getElementById('tunerStop').addEventListener('click',function(){
    cancelAnimationFrame(rafId);if(stream)stream.getTracks().forEach(function(t){t.stop();});if(audioCtx)audioCtx.close();
    document.getElementById('tunerStart').disabled=false;document.getElementById('tunerStop').disabled=true;
    document.getElementById('tunerNote').textContent='\u2014';document.getElementById('tunerOctave').textContent='';document.getElementById('tunerStatus').textContent='Stopped';
  });
})();
</script>
"""

EXT_FREQ_CONTENT = """
<div class="page-title">🔢 Frequency Calculator</div>
<p class="page-sub">Convert between note names, MIDI numbers, and Hz frequencies.</p>
<div class="card">
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin-bottom:16px">
    <div><label>Note</label><select id="fcNote" style="margin-bottom:0"><option>C</option><option>C#</option><option>D</option><option>D#</option><option>E</option><option>F</option><option>F#</option><option>G</option><option>G#</option><option selected>A</option><option>A#</option><option>B</option></select></div>
    <div><label>Octave</label><select id="fcOctave" style="margin-bottom:0"><option>0</option><option>1</option><option>2</option><option>3</option><option selected>4</option><option>5</option><option>6</option><option>7</option><option>8</option></select></div>
    <div><label>A4 (Hz)</label><input type="number" id="fcA4" value="440" min="400" max="480" step="0.5" style="margin-bottom:0"/></div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px">
    <div><label>MIDI Number</label><input type="number" id="fcMidi" value="69" min="0" max="127" style="margin-bottom:0"/></div>
    <div><label>Frequency (Hz)</label><input type="number" id="fcFreq" value="440.00" step="0.01" style="margin-bottom:0"/></div>
  </div>
  <button class="btn btn-sm" id="fcPlay" style="width:auto;padding:10px 24px;display:inline-block">\u25b6 Play Note</button>
  <div id="fcInfo" style="margin-top:16px;font-size:.86rem;color:var(--text-muted);line-height:1.8"></div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null,upd=false;
  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function midi2freq(m,a4){return a4*Math.pow(2,(m-69)/12);}
  function note2midi(n,o){return NOTES.indexOf(n)+(o+1)*12;}
  function freq2midi(f,a4){return 69+12*Math.log2(f/a4);}
  function showInfo(n,o,midi,freq,cents){
    var w=(343/freq).toFixed(4),p=(1000/freq).toFixed(4);
    var c=cents!=null?'<br>Cents offset: <strong>'+(cents>=0?'+':'')+cents+'\u00a2</strong>':'';
    document.getElementById('fcInfo').innerHTML='<strong>'+n+o+'</strong> \u00b7 MIDI <strong>'+midi+'</strong> \u00b7 <strong>'+freq.toFixed(2)+' Hz</strong>'+c+'<br>Wavelength: <strong>'+w+' m</strong> \u00b7 Period: <strong>'+p+' ms</strong>';}
  function fromNoteOctave(){if(upd)return;upd=true;var n=document.getElementById('fcNote').value,o=parseInt(document.getElementById('fcOctave').value),a4=parseFloat(document.getElementById('fcA4').value)||440,midi=note2midi(n,o),freq=midi2freq(midi,a4);document.getElementById('fcMidi').value=midi;document.getElementById('fcFreq').value=freq.toFixed(2);showInfo(n,o,midi,freq);upd=false;}
  function fromMidi(){if(upd)return;upd=true;var midi=parseInt(document.getElementById('fcMidi').value)||69,a4=parseFloat(document.getElementById('fcA4').value)||440,freq=midi2freq(midi,a4),ni=((midi%12)+12)%12,o=Math.floor(midi/12)-1;document.getElementById('fcNote').value=NOTES[ni];document.getElementById('fcOctave').value=o;document.getElementById('fcFreq').value=freq.toFixed(2);showInfo(NOTES[ni],o,midi,freq);upd=false;}
  function fromFreq(){if(upd)return;upd=true;var freq=parseFloat(document.getElementById('fcFreq').value)||440,a4=parseFloat(document.getElementById('fcA4').value)||440,me=freq2midi(freq,a4),midi=Math.round(me),cents=Math.round((me-midi)*100),ni=((midi%12)+12)%12,o=Math.floor(midi/12)-1;document.getElementById('fcNote').value=NOTES[ni];document.getElementById('fcOctave').value=o;document.getElementById('fcMidi').value=midi;showInfo(NOTES[ni],o,midi,freq,cents);upd=false;}
  document.getElementById('fcNote').addEventListener('change',fromNoteOctave);
  document.getElementById('fcOctave').addEventListener('change',fromNoteOctave);
  document.getElementById('fcA4').addEventListener('input',fromNoteOctave);
  document.getElementById('fcMidi').addEventListener('input',fromMidi);
  document.getElementById('fcFreq').addEventListener('input',fromFreq);
  document.getElementById('fcPlay').addEventListener('click',function(){
    var freq=parseFloat(document.getElementById('fcFreq').value)||440,ctx=getCtx(),now=ctx.currentTime;
    var master=ctx.createGain();master.connect(ctx.destination);master.gain.setValueAtTime(0,now);master.gain.linearRampToValueAtTime(0.4,now+0.005);master.gain.exponentialRampToValueAtTime(0.12,now+0.2);master.gain.exponentialRampToValueAtTime(0.0001,now+1.5);
    [{m:1,a:1},{m:2,a:.5},{m:3,a:.25},{m:4,a:.12}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=freq*h.m;g.gain.value=h.a;o.connect(g);g.connect(master);o.start(now);o.stop(now+1.6);});
  });
  fromNoteOctave();
})();
</script>
"""

EXT_PROGRESSION_CSS = """
.prog-slot{background:var(--input-bg);border:2px dashed var(--border);border-radius:12px;padding:14px;text-align:center;cursor:pointer;transition:all .15s;min-height:80px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}
.prog-slot:hover{border-color:var(--accent);background:var(--hover-bg)}
.prog-slot.filled{border-style:solid;border-color:var(--accent);background:var(--card)}
.prog-slot .cn{font-size:1rem;font-weight:700;color:var(--accent-text)}
.prog-slot .rv{font-size:.72rem;color:var(--text-faint)}
.prog-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-bottom:20px}
.prog-pill{padding:6px 10px;border:1px solid var(--border);border-radius:8px;font-size:.82rem;font-weight:600;cursor:pointer;background:var(--input-bg);color:var(--text-muted);transition:all .15s}
.prog-pill:hover{background:var(--accent);color:#fff;border-color:var(--accent)}
.prog-palette{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
"""

EXT_PROGRESSION_CONTENT = """
<div class="page-title">🎹 Chord Progression Builder</div>
<p class="page-sub">Build a chord progression from the palette and play it back.</p>
<div class="card">
  <div style="display:flex;gap:10px;margin-bottom:16px;flex-wrap:wrap">
    <div><label>Key</label><select id="progRoot" style="width:auto;margin-bottom:0"><option>C</option><option>C#</option><option>D</option><option>D#</option><option>E</option><option>F</option><option>F#</option><option>G</option><option>G#</option><option>A</option><option>A#</option><option>B</option></select></div>
    <div><label>Mode</label><select id="progMode" style="width:auto;margin-bottom:0"><option value="major">Major</option><option value="minor">Minor</option></select></div>
    <div><label>Tempo</label><select id="progTempo" style="width:auto;margin-bottom:0"><option value="0.5">Slow</option><option value="0.75" selected>Medium</option><option value="1.0">Fast</option><option value="1.5">Very fast</option></select></div>
  </div>
  <div class="card-title">Palette</div>
  <div class="prog-palette" id="progPalette"></div>
  <div class="card-title">Progression (up to 8 chords — click a chord to remove)</div>
  <div class="prog-grid" id="progGrid"></div>
  <div style="display:flex;gap:8px">
    <button class="btn btn-sm" id="progPlay" style="width:auto;padding:10px 24px">\u25b6 Play</button>
    <button class="btn btn-sm secondary" id="progClear" style="width:auto;padding:10px 24px;margin-top:0">Clear</button>
  </div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var MAJ_SCALE=[0,2,4,5,7,9,11],MIN_SCALE=[0,2,3,5,7,8,10];
  var MAJ_Q=['maj','min','min','maj','maj','min','dim'],MIN_Q=['min','dim','maj','min','min','maj','maj'];
  var MAJ_R=['I','ii','iii','IV','V','vi','vii\u00b0'],MIN_R=['i','ii\u00b0','III','iv','v','VI','VII'];
  var INT={maj:[0,4,7],min:[0,3,7],dim:[0,3,6],dom7:[0,4,7,10]};
  var audioCtx=null,prog=[];
  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function freq(semi){return 130.81*Math.pow(2,semi/12);}
  function pianoNote(ctx,f,start,dur,vol){var master=ctx.createGain();master.connect(ctx.destination);var end=start+dur;master.gain.setValueAtTime(0,start);master.gain.linearRampToValueAtTime(vol,start+0.008);master.gain.exponentialRampToValueAtTime(vol*0.35,start+0.15);master.gain.setValueAtTime(vol*0.35,end-0.2);master.gain.exponentialRampToValueAtTime(0.0001,end);[{m:1,a:1},{m:2,a:.55},{m:3,a:.28},{m:4,a:.14}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=f*h.m;g.gain.value=h.a;g.gain.setValueAtTime(h.a,start);g.gain.exponentialRampToValueAtTime(h.a*(h.m===1?.7:.04),start+0.12*h.m*.55);o.connect(g);g.connect(master);o.start(start);o.stop(end+0.1);});}
  function buildPalette(){
    var root=NOTES.indexOf(document.getElementById('progRoot').value);
    var mode=document.getElementById('progMode').value;
    var scale=mode==='major'?MAJ_SCALE:MIN_SCALE,quals=mode==='major'?MAJ_Q:MIN_Q,romans=mode==='major'?MAJ_R:MIN_R;
    var el=document.getElementById('progPalette');el.innerHTML='';
    scale.forEach(function(s,i){
      var ni=(root+s)%12,q=quals[i],name=NOTES[ni]+(q==='min'?'m':q==='dim'?'\u00b0':'');
      var btn=document.createElement('button');btn.className='prog-pill';
      btn.innerHTML=name+'<span style="font-size:.68rem;opacity:.7;margin-left:3px">'+romans[i]+'</span>';
      btn.addEventListener('click',function(){if(prog.length<8){prog.push({root:ni,quality:q,name:name,roman:romans[i]});renderGrid();}});
      el.appendChild(btn);
    });
    /* V7 */
    var v=(root+MAJ_SCALE[4])%12;var btn2=document.createElement('button');btn2.className='prog-pill';btn2.textContent=NOTES[v]+'7';
    btn2.addEventListener('click',function(){if(prog.length<8){prog.push({root:v,quality:'dom7',name:NOTES[v]+'7',roman:'V7'});renderGrid();}});
    el.appendChild(btn2);
  }
  function renderGrid(){
    var el=document.getElementById('progGrid');el.innerHTML='';
    for(var i=0;i<8;i++){
      var slot=document.createElement('div');
      if(i<prog.length){
        var c=prog[i];slot.className='prog-slot filled';
        slot.innerHTML='<div class="cn">'+c.name+'</div><div class="rv">'+c.roman+'</div><div style="font-size:.68rem;color:var(--text-xfaint)">click to remove</div>';
        slot.addEventListener('click',(function(idx){return function(){prog.splice(idx,1);renderGrid();};})(i));
      } else {slot.className='prog-slot';slot.innerHTML='<div style="color:var(--text-xfaint);font-size:.78rem">+ add</div>';}
      el.appendChild(slot);
    }
  }
  document.getElementById('progPlay').addEventListener('click',function(){
    if(!prog.length)return;
    var ctx=getCtx(),now=ctx.currentTime+0.05,beat=parseFloat(document.getElementById('progTempo').value)||0.75,cd=beat*2;
    prog.forEach(function(c,i){(INT[c.quality]||[0,4,7]).forEach(function(s,j){pianoNote(ctx,freq(c.root+s),now+i*cd+j*0.025,cd*0.88,0.3);});});
  });
  document.getElementById('progClear').addEventListener('click',function(){prog=[];renderGrid();});
  document.getElementById('progRoot').addEventListener('change',buildPalette);
  document.getElementById('progMode').addEventListener('change',buildPalette);
  buildPalette();renderGrid();
})();
</script>
"""

EXT_NOTATION_CONTENT = """
<div class="page-title">📖 Notation Reference</div>
<p class="page-sub">A searchable guide to music notation symbols, Italian terms, and dynamic markings.</p>
<div class="card">
  <input type="text" id="notSearch" placeholder="Search symbols, terms, meanings\u2026" style="margin-bottom:16px"/>
  <div id="notGrid"></div>
</div>
<script>
(function(){
  var E=[
    {s:'ppp',n:'ppp',c:'Dynamic',d:'Pianississimo \u2014 extremely soft'},
    {s:'pp',n:'pp',c:'Dynamic',d:'Pianissimo \u2014 very soft'},
    {s:'p',n:'piano',c:'Dynamic',d:'Soft'},
    {s:'mp',n:'mezzo-piano',c:'Dynamic',d:'Moderately soft'},
    {s:'mf',n:'mezzo-forte',c:'Dynamic',d:'Moderately loud'},
    {s:'f',n:'forte',c:'Dynamic',d:'Loud'},
    {s:'ff',n:'fortissimo',c:'Dynamic',d:'Very loud'},
    {s:'fff',n:'fortississimo',c:'Dynamic',d:'Extremely loud'},
    {s:'fp',n:'fortepiano',c:'Dynamic',d:'Loud, then immediately soft'},
    {s:'sfz',n:'sforzando',c:'Dynamic',d:'Sudden strong accent'},
    {s:'<',n:'crescendo',c:'Dynamic',d:'Gradually get louder'},
    {s:'>',n:'decrescendo',c:'Dynamic',d:'Gradually get softer'},
    {s:'Largo',n:'Largo',c:'Tempo',d:'Very slow \u2014 ~40\u201360 BPM'},
    {s:'Adagio',n:'Adagio',c:'Tempo',d:'Slow and stately \u2014 ~66\u201376 BPM'},
    {s:'Andante',n:'Andante',c:'Tempo',d:'Walking pace \u2014 ~76\u2013108 BPM'},
    {s:'Moderato',n:'Moderato',c:'Tempo',d:'Moderate \u2014 ~108\u2013120 BPM'},
    {s:'Allegro',n:'Allegro',c:'Tempo',d:'Fast and lively \u2014 ~120\u2013156 BPM'},
    {s:'Vivace',n:'Vivace',c:'Tempo',d:'Lively \u2014 ~156\u2013176 BPM'},
    {s:'Presto',n:'Presto',c:'Tempo',d:'Very fast \u2014 ~168\u2013200 BPM'},
    {s:'rit.',n:'ritardando',c:'Tempo',d:'Gradually slowing down'},
    {s:'accel.',n:'accelerando',c:'Tempo',d:'Gradually speeding up'},
    {s:'a tempo',n:'a tempo',c:'Tempo',d:'Return to original tempo'},
    {s:'𝄞',n:'Treble clef',c:'Clef',d:'G clef \u2014 for higher pitched instruments'},
    {s:'𝄢',n:'Bass clef',c:'Clef',d:'F clef \u2014 for lower pitched instruments'},
    {s:'#',n:'Sharp',c:'Accidental',d:'Raise a note by one semitone'},
    {s:'\u266d',n:'Flat',c:'Accidental',d:'Lower a note by one semitone'},
    {s:'\u266e',n:'Natural',c:'Accidental',d:'Cancel a previous sharp or flat'},
    {s:'𝄐',n:'Fermata',c:'Expression',d:'Hold the note longer than its value'},
    {s:'tr',n:'Trill',c:'Ornament',d:'Rapid alternation between two adjacent notes'},
    {s:'legato',n:'legato',c:'Articulation',d:'Play smoothly and connected'},
    {s:'\u2022',n:'staccato',c:'Articulation',d:'Play short and detached'},
    {s:'>',n:'accent',c:'Articulation',d:'Emphasize the note'},
    {s:'D.C.',n:'Da Capo',c:'Repeat',d:'Return to the beginning'},
    {s:'D.S.',n:'Dal Segno',c:'Repeat',d:'Return to the sign'},
    {s:'Fine',n:'Fine',c:'Repeat',d:'The end \u2014 stop here after D.C. or D.S.'},
  ];
  function render(q){
    q=(q||'').toLowerCase();
    var filtered=E.filter(function(e){return !q||e.n.toLowerCase().includes(q)||e.d.toLowerCase().includes(q)||e.c.toLowerCase().includes(q);});
    var byCat={};filtered.forEach(function(e){(byCat[e.c]=byCat[e.c]||[]).push(e);});
    var html='';
    Object.keys(byCat).forEach(function(cat){
      html+='<div style="margin-bottom:18px"><div class="card-title">'+cat+'</div><table style="width:100%;border-collapse:collapse;font-size:.88rem">';
      byCat[cat].forEach(function(e){html+='<tr style="border-bottom:1px solid var(--border)"><td style="padding:8px 12px;font-size:1.2rem;width:40px;text-align:center">'+e.s+'</td><td style="padding:8px 12px;font-weight:600;color:var(--accent-text);width:130px">'+e.n+'</td><td style="padding:8px 12px;color:var(--text-muted)">'+e.d+'</td></tr>';});
      html+='</table></div>';
    });
    document.getElementById('notGrid').innerHTML=html||'<div style="color:var(--text-faint);padding:20px;text-align:center">No results.</div>';
  }
  document.getElementById('notSearch').addEventListener('input',function(){render(this.value);});
  render();
})();
</script>
"""


# ── Rhythm Trainer ────────────────────────────────────────────────────────────
EXT_RHYTHM_CSS = """
.rhythm-display{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin:20px 0}
.beat-cell{width:52px;height:52px;border-radius:10px;border:2px solid var(--border);
  background:var(--input-bg);display:flex;align-items:center;justify-content:center;
  font-size:1.3rem;transition:background .05s,transform .05s;cursor:default}
.beat-cell.active{background:var(--accent);border-color:var(--accent);transform:scale(1.15)}
.beat-cell.accent{background:#22c55e;border-color:#166534;transform:scale(1.2)}
.beat-cell.filled{background:var(--hover-bg);border-color:var(--accent-text)}
.rhythm-tap{width:100%;padding:50px 0;font-size:1.5rem;font-weight:800;
  background:var(--accent);color:#fff;border:none;border-radius:14px;cursor:pointer;
  transition:background .1s,transform .05s;user-select:none;margin-top:12px}
.rhythm-tap:active{background:var(--accent-h);transform:scale(.98)}
.rhythm-score{display:flex;gap:24px;justify-content:center;margin-bottom:16px}
.rhythm-stat .val{font-size:2rem;font-weight:800;color:var(--accent-text);text-align:center}
.rhythm-stat .lbl{font-size:.74rem;color:var(--text-faint);text-align:center;text-transform:uppercase}
"""

EXT_RHYTHM_CONTENT = """
<div class="page-title">🥁 Rhythm Trainer</div>
<p class="page-sub">Watch the pattern, then tap it back in time. The dots show the beat — filled = tap, empty = rest.</p>
<div class="card">
  <div class="rhythm-score">
    <div class="rhythm-stat"><div class="val" id="rScore">0</div><div class="lbl">Score</div></div>
    <div class="rhythm-stat"><div class="val" id="rLevel">1</div><div class="lbl">Level</div></div>
    <div class="rhythm-stat"><div class="val" id="rStreak">0</div><div class="lbl">Streak</div></div>
  </div>
  <div id="rStatus" style="text-align:center;color:var(--text-muted);margin-bottom:12px;font-size:.9rem">Press Start to begin</div>
  <div class="rhythm-display" id="rBeats"></div>
  <div style="display:flex;gap:10px;margin-top:8px">
    <button class="btn btn-sm" id="rStart" style="width:auto;padding:10px 28px">▶ Start</button>
    <select id="rTimeSig" style="width:auto;margin-bottom:0">
      <option value="4">4/4</option><option value="3">3/4</option>
      <option value="5">5/4</option><option value="6">6/8</option>
    </select>
    <select id="rTempo" style="width:auto;margin-bottom:0">
      <option value="600">Slow</option><option value="450" selected>Medium</option>
      <option value="300">Fast</option>
    </select>
  </div>
  <button class="rhythm-tap" id="rTap" disabled>TAP</button>
  <div id="rFeedback" style="text-align:center;font-size:1rem;font-weight:700;min-height:28px;margin-top:12px"></div>
</div>
<script>
(function(){
  var audioCtx=null,beats=4,tempo=450,pattern=[],userTaps=[],tapIdx=0;
  var score=0,level=1,streak=0,phase='idle',playTimer=null,tapTimer=null;
  var beatDots=[],currentBeat=-1,playInterval=null;

  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function click(freq,vol){var ctx=getCtx(),now=ctx.currentTime,o=ctx.createOscillator(),g=ctx.createGain();o.type='square';o.frequency.value=freq;g.gain.setValueAtTime(vol,now);g.gain.exponentialRampToValueAtTime(0.0001,now+0.05);o.connect(g);g.connect(ctx.destination);o.start(now);o.stop(now+0.06);}

  function genPattern(){
    pattern=[];
    var numBeats=beats*(level<3?1:level<5?2:3);
    for(var i=0;i<numBeats;i++) pattern.push(Math.random()>(0.45-level*0.02)?1:0);
    pattern[0]=1;/* always start with a tap */
    return pattern;
  }

  function buildDots(){
    var el=document.getElementById('rBeats');el.innerHTML='';beatDots=[];
    pattern.forEach(function(p,i){
      var d=document.createElement('div');d.className='beat-cell'+(p?' filled':'');
      d.textContent=p?'♩':'·';beatDots.push(d);el.appendChild(d);
    });
  }

  function playPattern(cb){
    var i=0;currentBeat=-1;
    buildDots();
    document.getElementById('rStatus').textContent='Watch the pattern…';
    playInterval=setInterval(function(){
      if(currentBeat>=0&&beatDots[currentBeat]) beatDots[currentBeat].classList.remove('active','accent');
      if(i>=pattern.length){clearInterval(playInterval);setTimeout(cb,400);return;}
      currentBeat=i;
      beatDots[i].classList.add(i===0?'accent':'active');
      if(pattern[i])click(i===0?800:600,0.3);
      else click(200,0.1);
      i++;
    },tempo);
  }

  function startTapping(){
    userTaps=[];tapIdx=0;
    beatDots.forEach(function(d){d.classList.remove('active','accent','filled');d.textContent='·';});
    document.getElementById('rStatus').textContent='Now tap the pattern! (' +pattern.filter(function(x){return x;}).length+' taps)';
    document.getElementById('rTap').disabled=false;
    document.getElementById('rFeedback').textContent='';
    phase='tapping';
    tapTimer=setTimeout(function(){if(phase==='tapping')grade();},tempo*pattern.length+1000);
  }

  function tap(){
    if(phase!=='tapping')return;
    /* Find next expected tap position */
    while(tapIdx<pattern.length&&pattern[tapIdx]===0)tapIdx++;
    if(tapIdx<pattern.length){
      userTaps.push(tapIdx);
      beatDots[tapIdx].classList.add('active');
      beatDots[tapIdx].textContent='♩';
      click(800,0.35);
      tapIdx++;
      if(userTaps.length===pattern.filter(function(x){return x;}).length) grade();
    }
  }

  function grade(){
    clearTimeout(tapTimer);phase='idle';
    document.getElementById('rTap').disabled=true;
    var expected=[];pattern.forEach(function(p,i){if(p)expected.push(i);});
    var correct=0;
    expected.forEach(function(e,i){if(userTaps[i]===e)correct++;});
    var pct=expected.length?Math.round(correct/expected.length*100):0;
    if(pct>=80){score+=level*10;streak++;if(streak%3===0)level=Math.min(10,level+1);
      document.getElementById('rFeedback').textContent='✅ '+pct+'% correct! +'+level*10+' pts';
      document.getElementById('rFeedback').style.color='#22c55e';}
    else{streak=0;
      document.getElementById('rFeedback').textContent='❌ '+pct+'% — try again!';
      document.getElementById('rFeedback').style.color='#ef4444';}
    document.getElementById('rScore').textContent=score;
    document.getElementById('rLevel').textContent=level;
    document.getElementById('rStreak').textContent=streak;
    document.getElementById('rStatus').textContent='Press Start for next pattern';
    document.getElementById('rStart').disabled=false;
  }

  document.getElementById('rStart').addEventListener('click',function(){
    this.disabled=true;phase='playing';
    beats=parseInt(document.getElementById('rTimeSig').value);
    tempo=parseInt(document.getElementById('rTempo').value);
    genPattern();
    playPattern(startTapping);
  });
  document.getElementById('rTap').addEventListener('click',tap);
  document.addEventListener('keydown',function(e){if(e.code==='Space'&&phase==='tapping'){e.preventDefault();tap();}});
})();
</script>
"""

# ── Ear Training ──────────────────────────────────────────────────────────────
EXT_EAR_CSS = """
.ear-choices{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:16px}
.ear-btn{padding:12px;background:var(--input-bg);border:1px solid var(--border);
  border-radius:10px;color:var(--text);font-size:.9rem;font-weight:500;cursor:pointer;transition:all .15s}
.ear-btn:hover{background:var(--hover-bg);border-color:var(--accent)}
.ear-btn.correct{background:#14261f;border-color:#166534;color:#86efac}
.ear-btn.wrong{background:#2d1b1b;border-color:#7f1d1d;color:#fca5a5}
.ear-mode-btns{display:flex;gap:6px;margin-bottom:18px;flex-wrap:wrap}
.ear-mode-btn{padding:7px 14px;border:1px solid var(--border);border-radius:8px;
  background:transparent;color:var(--text-muted);font-size:.83rem;cursor:pointer;transition:all .15s}
.ear-mode-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
"""

EXT_EAR_CONTENT = """
<div class="page-title">👂 Ear Training Suite</div>
<p class="page-sub">Train your ears across three modes: chord quality, interval recognition, and scale ID.</p>
<div class="card">
  <div class="ear-mode-btns">
    <button class="ear-mode-btn active" onclick="setMode('chord')">🎹 Chord Quality</button>
    <button class="ear-mode-btn" onclick="setMode('interval')">🎯 Intervals</button>
    <button class="ear-mode-btn" onclick="setMode('scale')">🎼 Scales</button>
  </div>
  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:16px">
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="earCorrect">0</div><div style="font-size:.74rem;color:var(--text-faint)">CORRECT</div></div>
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="earStreak">0</div><div style="font-size:.74rem;color:var(--text-faint)">STREAK 🔥</div></div>
  </div>
  <div id="earQuestion" style="text-align:center;color:var(--text-muted);font-size:.95rem;margin-bottom:8px">Select a mode and click Play</div>
  <div style="text-align:center;margin-bottom:12px;display:flex;gap:8px;justify-content:center">
    <button class="btn btn-sm" id="earPlay" style="width:auto;padding:10px 24px">▶ Play</button>
    <button class="btn btn-sm" id="earNew" style="width:auto;padding:10px 24px;background:var(--input-bg);border:1px solid var(--border);color:var(--text-muted)">New Question</button>
  </div>
  <div class="ear-choices" id="earChoices"></div>
  <div id="earFeedback" style="text-align:center;font-size:.95rem;font-weight:700;min-height:28px;margin-top:12px"></div>
</div>
<script>
(function(){
  var audioCtx=null,mode='chord',current=null,answered=false,correct=0,streak=0;
  var CHORDS={Major:[0,4,7],Minor:[0,3,7],Dominant7:[0,4,7,10],Major7:[0,4,7,11],Minor7:[0,3,7,10],Diminished:[0,3,6],Augmented:[0,4,8],Sus4:[0,5,7]};
  var INTERVALS=[{n:'Unison',s:0},{n:'Minor 2nd',s:1},{n:'Major 2nd',s:2},{n:'Minor 3rd',s:3},{n:'Major 3rd',s:4},{n:'Perfect 4th',s:5},{n:'Tritone',s:6},{n:'Perfect 5th',s:7},{n:'Minor 6th',s:8},{n:'Major 6th',s:9},{n:'Minor 7th',s:10},{n:'Major 7th',s:11},{n:'Octave',s:12}];
  var SCALES={Major:[0,2,4,5,7,9,11],'Natural Minor':[0,2,3,5,7,8,10],'Harmonic Minor':[0,2,3,5,7,8,11],Dorian:[0,2,3,5,7,9,10],Phrygian:[0,1,3,5,7,8,10],Lydian:[0,2,4,6,7,9,11],Mixolydian:[0,2,4,5,7,9,10],'Pentatonic Major':[0,2,4,7,9],'Pentatonic Minor':[0,3,5,7,10],Blues:[0,3,5,6,7,10]};

  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function freq(semi){return 261.63*Math.pow(2,semi/12);}
  function pianoNote(ctx,f,start,dur,vol){
    var master=ctx.createGain();master.connect(ctx.destination);
    var end=start+dur;master.gain.setValueAtTime(0,start);master.gain.linearRampToValueAtTime(vol,start+0.008);master.gain.exponentialRampToValueAtTime(vol*0.3,start+0.12);master.gain.setValueAtTime(vol*0.3,end-0.2);master.gain.exponentialRampToValueAtTime(0.0001,end);
    [{m:1,a:1},{m:2,a:.55},{m:3,a:.28},{m:4,a:.14}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=f*h.m;g.gain.value=h.a;g.gain.setValueAtTime(h.a,start);g.gain.exponentialRampToValueAtTime(h.amp*(h.m===1?.7:.04)||0.001,start+0.12*h.m*.55);o.connect(g);g.connect(master);o.start(start);o.stop(end+0.1);});
  }
  function shuffle(a){return a.slice().sort(function(){return Math.random()-.5;});}

  window.setMode=function(m){
    mode=m;answered=false;current=null;
    document.querySelectorAll('.ear-mode-btn').forEach(function(b){b.classList.toggle('active',b.textContent.toLowerCase().includes(m.slice(0,4)));});
    document.getElementById('earQuestion').textContent='Click Play to hear a '+(m==='chord'?'chord':m==='interval'?'interval':'scale');
    document.getElementById('earChoices').innerHTML='';
    document.getElementById('earFeedback').textContent='';
    newQuestion();
  };

  function newQuestion(){
    answered=false;
    document.getElementById('earFeedback').textContent='';
    var choices,correctName;
    if(mode==='chord'){
      var names=Object.keys(CHORDS),ci=Math.floor(Math.random()*names.length);
      correctName=names[ci];current={type:'chord',name:correctName,intervals:CHORDS[correctName]};
      choices=shuffle(names).slice(0,4);if(!choices.includes(correctName))choices[0]=correctName;choices=shuffle(choices);
    } else if(mode==='interval'){
      var ii=Math.floor(Math.random()*INTERVALS.length);
      current={type:'interval',name:INTERVALS[ii].n,semis:INTERVALS[ii].s};
      choices=shuffle(INTERVALS).slice(0,4).map(function(x){return x.n;});
      if(!choices.includes(current.name))choices[0]=current.name;choices=shuffle(choices);
    } else {
      var snames=Object.keys(SCALES),si=Math.floor(Math.random()*snames.length);
      correctName=snames[si];current={type:'scale',name:correctName,intervals:SCALES[correctName]};
      choices=shuffle(snames).slice(0,4);if(!choices.includes(correctName))choices[0]=correctName;choices=shuffle(choices);
    }
    document.getElementById('earQuestion').textContent='What '+mode+' is this?';
    var el=document.getElementById('earChoices');el.innerHTML='';
    choices.forEach(function(c){
      var btn=document.createElement('button');btn.className='ear-btn';btn.textContent=c;
      btn.addEventListener('click',function(){if(!answered)answer(c,btn);});
      el.appendChild(btn);
    });
  }

  function playSound(){
    if(!current)return;
    var ctx=getCtx(),now=ctx.currentTime;
    if(current.type==='chord'){
      current.intervals.forEach(function(s,i){pianoNote(ctx,freq(s),now+i*0.02,1.4,0.32);});
    } else if(current.type==='interval'){
      pianoNote(ctx,freq(0),now,0.8,0.4);
      pianoNote(ctx,freq(current.semis),now+0.7,0.8,0.4);
      setTimeout(function(){var n=getCtx().currentTime;pianoNote(getCtx(),freq(0),n,1,0.3);pianoNote(getCtx(),freq(current.semis),n,1,0.3);},1600);
    } else {
      current.intervals.concat([12]).forEach(function(s,i){pianoNote(ctx,freq(s),now+i*0.22,0.5,0.4);});
    }
  }

  function answer(chosen,btn){
    if(answered)return;answered=true;
    var ok=(chosen===current.name);
    if(ok){correct++;streak++;}else{streak=0;}
    btn.classList.add(ok?'correct':'wrong');
    if(!ok){document.querySelectorAll('.ear-btn').forEach(function(b){if(b.textContent===current.name)b.classList.add('correct');});}
    document.getElementById('earCorrect').textContent=correct;
    document.getElementById('earStreak').textContent=streak;
    document.getElementById('earFeedback').textContent=ok?'✅ Correct!':'❌ It was: '+current.name;
    document.getElementById('earFeedback').style.color=ok?'#22c55e':'#ef4444';
  }

  document.getElementById('earPlay').addEventListener('click',function(){if(!current)newQuestion();playSound();});
  document.getElementById('earNew').addEventListener('click',function(){newQuestion();setTimeout(playSound,200);});
  newQuestion();
})();
</script>
"""

# ── Time Sig Trainer ──────────────────────────────────────────────────────────
EXT_TIMESIG_CONTENT = """
<div class="page-title">📐 Time Sig Trainer</div>
<p class="page-sub">Listen to a rhythm pattern and identify its time signature.</p>
<div class="card">
  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:20px">
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="tsCorrect">0</div><div style="font-size:.74rem;color:var(--text-faint)">CORRECT</div></div>
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="tsStreak">0</div><div style="font-size:.74rem;color:var(--text-faint)">STREAK</div></div>
  </div>
  <div id="tsStatus" style="text-align:center;color:var(--text-muted);margin-bottom:16px">Press Play to hear a rhythm</div>
  <div style="text-align:center;margin-bottom:20px">
    <button class="btn btn-sm" id="tsPlay" style="width:auto;padding:10px 28px;display:inline-block">▶ Play Rhythm</button>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px" id="tsChoices"></div>
  <div id="tsFeedback" style="text-align:center;font-size:.95rem;font-weight:700;min-height:28px;margin-top:14px"></div>
</div>
<script>
(function(){
  var audioCtx=null,current=null,answered=false,correct=0,streak=0;
  var TIME_SIGS=[
    {name:'2/4',beats:2,desc:'March feel — strong, weak'},
    {name:'3/4',beats:3,desc:'Waltz feel — 1-2-3'},
    {name:'4/4',beats:4,desc:'Common time — most popular'},
    {name:'5/4',beats:5,desc:'Asymmetric — "Take Five"'},
    {name:'6/8',beats:6,desc:'Compound duple — lilting'},
    {name:'7/8',beats:7,desc:'Asymmetric — Balkan feel'},
  ];
  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function click(freq,vol,time){var ctx=getCtx(),o=ctx.createOscillator(),g=ctx.createGain();o.type='square';o.frequency.value=freq;g.gain.setValueAtTime(vol,time);g.gain.exponentialRampToValueAtTime(0.0001,time+0.06);o.connect(g);g.connect(ctx.destination);o.start(time);o.stop(time+0.08);}
  function shuffle(a){return a.slice().sort(function(){return Math.random()-.5;});}

  function playRhythm(ts){
    var ctx=getCtx(),now=ctx.currentTime+0.1,beatLen=0.42;
    for(var rep=0;rep<3;rep++){
      for(var b=0;b<ts.beats;b++){
        var t=now+rep*(ts.beats*beatLen)+b*beatLen;
        click(b===0?1200:800,b===0?0.6:0.35,t);
      }
    }
  }

  function newQuestion(){
    answered=false;current=TIME_SIGS[Math.floor(Math.random()*TIME_SIGS.length)];
    document.getElementById('tsFeedback').textContent='';
    document.getElementById('tsStatus').textContent='What time signature is this?';
    var choices=shuffle(TIME_SIGS).slice(0,4);
    if(!choices.find(function(x){return x.name===current.name;}))choices[0]=current;
    choices=shuffle(choices);
    var el=document.getElementById('tsChoices');el.innerHTML='';
    choices.forEach(function(c){
      var btn=document.createElement('button');
      btn.style.cssText='padding:16px;background:var(--input-bg);border:1px solid var(--border);border-radius:10px;color:var(--text);font-size:1.2rem;font-weight:700;cursor:pointer;transition:all .15s';
      btn.textContent=c.name;
      btn.addEventListener('click',function(){if(!answered)answer(c,btn);});
      el.appendChild(btn);
    });
  }

  function answer(chosen,btn){
    if(answered)return;answered=true;
    var ok=(chosen.name===current.name);
    if(ok){correct++;streak++;}else streak=0;
    btn.style.background=ok?'#14261f':'#2d1b1b';
    btn.style.borderColor=ok?'#166534':'#7f1d1d';
    btn.style.color=ok?'#86efac':'#fca5a5';
    if(!ok){document.querySelectorAll('#tsChoices button').forEach(function(b){if(b.textContent===current.name){b.style.background='#14261f';b.style.borderColor='#166534';b.style.color='#86efac';}});}
    document.getElementById('tsCorrect').textContent=correct;
    document.getElementById('tsStreak').textContent=streak;
    document.getElementById('tsFeedback').textContent=(ok?'✅ Correct! ':'❌ It was '+current.name+' — ')+current.desc;
    document.getElementById('tsFeedback').style.color=ok?'#22c55e':'#ef4444';
  }

  document.getElementById('tsPlay').addEventListener('click',function(){newQuestion();setTimeout(function(){playRhythm(current);},100);});
  newQuestion();
})();
</script>
"""

# ── Solfege Trainer ───────────────────────────────────────────────────────────
EXT_SOLFEGE_CONTENT = """
<div class="page-title">🎵 Solfège Trainer</div>
<p class="page-sub">Hear a note in the scale and identify its solfège syllable. Uses moveable-do in C major.</p>
<div class="card">
  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:16px">
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="solCorrect">0</div><div style="font-size:.74rem;color:var(--text-faint)">CORRECT</div></div>
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="solStreak">0</div><div style="font-size:.74rem;color:var(--text-faint)">STREAK 🔥</div></div>
  </div>
  <div style="display:flex;gap:8px;justify-content:center;margin-bottom:18px;flex-wrap:wrap">
    <button class="btn btn-sm" id="solNew" style="width:auto;padding:10px 22px">New Note</button>
    <button class="btn btn-sm" id="solPlay" style="width:auto;padding:10px 22px;background:var(--input-bg);border:1px solid var(--border);color:var(--text-muted)" disabled>▶ Replay</button>
  </div>
  <div id="solStatus" style="text-align:center;color:var(--text-muted);margin-bottom:14px">Click "New Note" to begin</div>
  <div id="solChoices" style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px"></div>
  <div id="solFeedback" style="text-align:center;font-size:.95rem;font-weight:700;min-height:28px;margin-top:12px"></div>
</div>
<script>
(function(){
  var audioCtx=null,current=null,answered=false,correct=0,streak=0;
  var SOLFEGE=[
    {name:'Do',semi:0,note:'C'},{name:'Re',semi:2,note:'D'},{name:'Mi',semi:4,note:'E'},
    {name:'Fa',semi:5,note:'F'},{name:'Sol',semi:7,note:'G'},{name:'La',semi:9,note:'A'},
    {name:'Ti',semi:11,note:'B'},{name:'Do'',semi:12,note:'C''}
  ];
  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function freq(semi){return 261.63*Math.pow(2,semi/12);}
  function pianoNote(ctx,f,start,dur,vol){
    var master=ctx.createGain();master.connect(ctx.destination);
    var end=start+dur;master.gain.setValueAtTime(0,start);master.gain.linearRampToValueAtTime(vol,start+0.005);master.gain.exponentialRampToValueAtTime(vol*0.3,start+0.12);master.gain.setValueAtTime(vol*0.3,end-0.15);master.gain.exponentialRampToValueAtTime(0.0001,end);
    [{m:1,a:1},{m:2,a:.55},{m:3,a:.28},{m:4,a:.14}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=f*h.m;g.gain.value=h.a;o.connect(g);g.connect(master);o.start(start);o.stop(end+0.1);});
  }
  function shuffle(a){return a.slice().sort(function(){return Math.random()-.5;});}

  /* Play the scale first to establish key context, then the note */
  function playWithContext(s){
    var ctx=getCtx(),now=ctx.currentTime;
    /* Quick scale hint */
    [0,2,4,5,7,9,11,12].forEach(function(note,i){pianoNote(ctx,freq(note),now+i*0.12,0.2,0.2);});
    /* Then the target note */
    pianoNote(ctx,freq(s),now+1.2,1.0,0.5);
  }

  function newQuestion(){
    answered=false;
    current=SOLFEGE[Math.floor(Math.random()*SOLFEGE.length)];
    document.getElementById('solFeedback').textContent='';
    document.getElementById('solStatus').textContent='Which solfège syllable is this note?';
    document.getElementById('solPlay').disabled=false;
    var choices=shuffle(SOLFEGE).slice(0,4);
    if(!choices.find(function(x){return x.name===current.name;}))choices[0]=current;
    choices=shuffle(choices);
    var el=document.getElementById('solChoices');el.innerHTML='';
    choices.forEach(function(c){
      var btn=document.createElement('button');
      btn.style.cssText='padding:14px 8px;background:var(--input-bg);border:1px solid var(--border);border-radius:10px;color:var(--accent-text);font-size:1.1rem;font-weight:700;cursor:pointer;transition:all .15s';
      btn.innerHTML=c.name+'<div style="font-size:.72rem;color:var(--text-faint);font-weight:400">'+c.note+'</div>';
      btn.addEventListener('click',function(){if(!answered)answer(c,btn);});
      el.appendChild(btn);
    });
    playWithContext(current.semi);
  }

  function answer(chosen,btn){
    if(answered)return;answered=true;
    var ok=(chosen.name===current.name);
    if(ok){correct++;streak++;}else streak=0;
    btn.style.background=ok?'#14261f':'#2d1b1b';
    btn.style.borderColor=ok?'#166534':'#7f1d1d';
    if(!ok){document.querySelectorAll('#solChoices button').forEach(function(b){if(b.textContent.startsWith(current.name))b.style.background='#14261f';});}
    document.getElementById('solCorrect').textContent=correct;
    document.getElementById('solStreak').textContent=streak;
    document.getElementById('solFeedback').textContent=ok?'✅ Correct! That\'s '+current.name+' ('+current.note+')':'❌ It was '+current.name+' — '+current.note;
    document.getElementById('solFeedback').style.color=ok?'#22c55e':'#ef4444';
  }

  document.getElementById('solNew').addEventListener('click',newQuestion);
  document.getElementById('solPlay').addEventListener('click',function(){if(current)playWithContext(current.semi);});
})();
</script>
"""

# ── Form Analyzer ─────────────────────────────────────────────────────────────
EXT_FORM_CONTENT = """
<div class="page-title">🔍 Form Analyzer</div>
<p class="page-sub">Upload a MusicXML file to get an automatic analysis of its musical structure and form.</p>
<div class="card">
  <form method="POST" enctype="multipart/form-data" action="/ext/form-analyzer" id="formUpload">
    <label>MusicXML File (.xml or .musicxml)</label>
    <input type="file" name="file" accept=".xml,.musicxml" required id="formFile"/>
    <button class="btn" type="submit">Analyze Form</button>
  </form>
</div>
{% if result %}
<div class="card">
  <div class="card-title">Form Analysis</div>
  <div style="margin-bottom:16px">
    <div style="font-size:1.1rem;font-weight:700;color:var(--accent-text);margin-bottom:4px">{{ result.form_label }}</div>
    <div style="font-size:.86rem;color:var(--text-muted)">{{ result.measures }} measures · {{ result.sections|length }} sections detected</div>
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px">
    {% for sec in result.sections %}
    <div style="background:var(--input-bg);border:1px solid var(--border);border-radius:8px;padding:8px 14px;text-align:center">
      <div style="font-size:1rem;font-weight:700;color:var(--accent-text)">{{ sec.label }}</div>
      <div style="font-size:.74rem;color:var(--text-faint)">mm. {{ sec.start }}–{{ sec.end }}</div>
    </div>
    {% endfor %}
  </div>
  {% if result.key %}<div style="font-size:.86rem;color:var(--text-muted);margin-bottom:6px">Key: <strong>{{ result.key }}</strong></div>{% endif %}
  {% if result.tempo %}<div style="font-size:.86rem;color:var(--text-muted)">Tempo: <strong>{{ result.tempo }} BPM</strong></div>{% endif %}
</div>
{% endif %}
{% if error %}<div class="flash error">{{ error }}</div>{% endif %}
"""


# ── MIDI Player Extension ─────────────────────────────────────────────────────
EXT_MIDI_CSS = """
.midi-drop{border:2px dashed var(--border);border-radius:12px;padding:36px 24px;
  text-align:center;cursor:pointer;position:relative;transition:border-color .2s,background .2s}
.midi-drop.drag-over{border-color:var(--accent);background:var(--hover-bg)}
.midi-drop input[type=file]{position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%}
.midi-transport{display:flex;align-items:center;gap:10px;padding:12px 16px;margin-top:14px;
  background:var(--input-bg);border:1px solid var(--border);border-radius:10px;flex-wrap:wrap}
.midi-btn{width:38px;height:38px;border-radius:50%;border:none;font-size:.9rem;
  cursor:pointer;transition:background .15s;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.midi-btn.primary{background:var(--accent);color:#fff}
.midi-btn.primary:hover{background:var(--accent-h)}
.midi-btn.primary:disabled{background:var(--border);cursor:not-allowed;color:var(--text-faint)}
.midi-btn.sec{background:var(--input-bg);color:var(--text-muted);border:1px solid var(--border)}
.midi-btn.sec:hover{background:var(--hover-bg);color:var(--text)}
.midi-prog{flex:1;min-width:80px;accent-color:var(--accent)}
.midi-time{font-size:.78rem;color:var(--text-faint);font-family:monospace;min-width:90px;text-align:center}
.midi-vol{width:60px;accent-color:var(--accent)}
.midi-info{font-size:.75rem;color:var(--text-faint);width:100%;padding-top:2px}
.midi-track-list{display:flex;flex-direction:column;gap:6px;margin-top:14px}
.midi-track{display:flex;align-items:center;gap:10px;padding:8px 12px;
  background:var(--input-bg);border:1px solid var(--border);border-radius:8px}
.midi-track-color{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.midi-track-name{flex:1;font-size:.85rem;color:var(--text);font-weight:500}
.midi-track-notes{font-size:.75rem;color:var(--text-faint)}
.midi-track-mute{font-size:.75rem;padding:3px 8px;border:1px solid var(--border);
  border-radius:5px;background:transparent;color:var(--text-muted);cursor:pointer;transition:all .15s}
.midi-track-mute.muted{background:#2d1b1b;border-color:#7f1d1d;color:#fca5a5}
/* Piano roll */
.piano-roll{background:var(--input-bg);border:1px solid var(--border);border-radius:10px;
  margin-top:14px;overflow:hidden;position:relative;height:160px}
.piano-roll canvas{display:block;width:100%;height:100%}
.pr-cursor{position:absolute;top:0;bottom:0;width:2px;background:rgba(99,102,241,.8);pointer-events:none;display:none}
/* Keyboard */
.midi-keyboard{display:flex;height:80px;margin-top:10px;background:var(--card);
  border:1px solid var(--border);border-radius:8px;overflow:hidden;padding:4px 4px 0}
.mk2-inner{position:relative;display:flex;height:72px;flex:1;overflow:hidden}
.mk2-w{flex:1;min-width:0;background:#fff;border:1px solid #ccc;border-radius:0 0 5px 5px;
  position:relative;transition:background .04s}
.mk2-w.lit{background:#818cf8}
.mk2-b{position:absolute;background:#1a1a2e;border:1px solid #475569;border-radius:0 0 4px 4px;
  width:58%;height:58%;top:0;left:57%;z-index:2;transition:background .04s}
.mk2-b.lit{background:#6366f1}
"""

EXT_MIDI_CONTENT = """
<div class="page-title">🎹 MIDI Player</div>
<p class="page-sub">Upload a .mid or .midi file to play it back with a piano roll, live keyboard, and per-track controls.</p>
<div class="card">
  <div class="midi-drop" id="midiDrop">
    <input type="file" id="midiFile" accept=".mid,.midi"/>
    <div style="font-size:2.2rem;margin-bottom:10px">🎹</div>
    <p><strong>Click to upload</strong> or drag and drop</p>
    <p style="font-size:.8rem;margin-top:4px">Supports .mid and .midi files</p>
  </div>
  <div id="midiMeta" style="display:none;margin-top:12px;font-size:.85rem;color:var(--text-muted)"></div>
</div>

<div id="midiPlayer" style="display:none">
  <!-- Transport -->
  <div class="midi-transport">
    <button class="midi-btn primary" id="mPlay" disabled>▶</button>
    <button class="midi-btn sec" id="mStop" disabled>■</button>
    <button class="midi-btn sec" id="mRewind" title="Rewind">⏮</button>
    <input type="range" class="midi-prog" id="mProgress" value="0" min="0" max="100" step="0.1"/>
    <span class="midi-time" id="mTime">0:00 / 0:00</span>
    <span style="font-size:.75rem;color:var(--text-faint);flex-shrink:0">Vol</span>
    <input type="range" class="midi-vol" id="mVol" min="0" max="1" step="0.05" value="0.75"/>
    <div class="midi-info" id="mInfo">Ready</div>
  </div>

  <!-- Piano roll -->
  <div class="piano-roll" id="pianoRoll">
    <canvas id="prCanvas"></canvas>
    <div class="pr-cursor" id="prCursor"></div>
  </div>

  <!-- Keyboard -->
  <div class="midi-keyboard">
    <div class="mk2-inner" id="mk2Inner"></div>
  </div>

  <!-- Track list -->
  <div id="midiTracks" class="midi-track-list"></div>
</div>

<script>
(function(){
  /* ── MIDI Parser ── */
  function parseMidi(buf){
    var view=new DataView(buf),pos=0;
    function read(n){var v=0;for(var i=0;i<n;i++)v=(v<<8)|view.getUint8(pos++);return v;}
    function readVLQ(){var v=0,b;do{b=view.getUint8(pos++);v=(v<<7)|(b&0x7f);}while(b&0x80);return v;}
    /* Header */
    pos=0;read(4);/* MThd */
    var hlen=read(4),fmt=read(2),numTracks=read(2),tpq=read(2);
    var tracks=[];
    for(var t=0;t<numTracks;t++){
      read(4);/* MTrk */
      var tlen=read(4),tend=pos+tlen,events=[],tick=0;
      var lastStatus=0;
      while(pos<tend){
        var delta=readVLQ();tick+=delta;
        var status=view.getUint8(pos);
        if(status&0x80){status=view.getUint8(pos++);lastStatus=status;}else{status=lastStatus;}
        var type=status>>4,ch=status&0xf;
        if(type===0x9){var note=view.getUint8(pos++),vel=view.getUint8(pos++);events.push({tick:tick,type:vel>0?'noteon':'noteoff',ch:ch,note:note,vel:vel});}
        else if(type===0x8){var note=view.getUint8(pos++);pos++;events.push({tick:tick,type:'noteoff',ch:ch,note:note});}
        else if(type===0xa){pos+=2;}
        else if(type===0xb){pos+=2;}
        else if(type===0xc){pos++;}
        else if(type===0xd){pos++;}
        else if(type===0xe){pos+=2;}
        else if(type===0xf){
          if(ch===0xf){/* meta */
            var mt=view.getUint8(pos++),ml=readVLQ();
            if(mt===0x51&&ml===3){/* tempo */
              var us=(view.getUint8(pos)<<16)|(view.getUint8(pos+1)<<8)|view.getUint8(pos+2);
              events.push({tick:tick,type:'tempo',us:us});
            } else if(mt===0x03){/* track name */
              var nm='';for(var i=0;i<ml;i++)nm+=String.fromCharCode(view.getUint8(pos+i));
              events.push({tick:tick,type:'name',name:nm});
            }
            pos+=ml;
          } else {var slen=readVLQ();pos+=slen;}
        } else pos++;
      }
      pos=tend;tracks.push(events);
    }
    return{fmt:fmt,tpq:tpq,tracks:tracks};
  }

  function buildNoteEvents(midi){
    /* Flatten all tracks into absolute-time note events */
    var tempo=500000,tpq=midi.tpq;
    var allEvents=[];
    midi.tracks.forEach(function(track,ti){
      var usPerTick=tempo/tpq;
      track.forEach(function(ev){allEvents.push(Object.assign({},ev,{track:ti}));});
    });
    allEvents.sort(function(a,b){return a.tick-b.tick||(a.type==='noteoff'?-1:1);});
    /* Convert ticks to seconds */
    var notes=[],openNotes={},curTempo=500000,lastTick=0,curTime=0;
    allEvents.forEach(function(ev){
      var dtick=ev.tick-lastTick;
      curTime+=dtick*(curTempo/tpq)/1e6;
      lastTick=ev.tick;
      if(ev.type==='tempo')curTempo=ev.us;
      else if(ev.type==='noteon'){
        var key=ev.track+'_'+ev.ch+'_'+ev.note;
        openNotes[key]={time:curTime,note:ev.note,vel:ev.vel,track:ev.track,ch:ev.ch};
      } else if(ev.type==='noteoff'){
        var key=ev.track+'_'+ev.ch+'_'+ev.note;
        if(openNotes[key]){
          var o=openNotes[key];
          notes.push({time:o.time,dur:Math.max(0.05,curTime-o.time),note:o.note,vel:o.vel,track:o.track,ch:o.ch,freq:440*Math.pow(2,(o.note-69)/12)});
          delete openNotes[key];
        }
      }
    });
    notes.sort(function(a,b){return a.time-b.time;});
    return notes;
  }

  /* ── State ── */
  var audioCtx=null,masterGain=null;
  var noteEvents=[],totalDuration=0;
  var isPlaying=false,playOffset=0,playStartTime=0;
  var rafId=null,schedTimer=null,schedIdx=0;
  var mutedTracks=new Set();
  var LOOKAHEAD=0.35,SCHED_MS=80;
  var TRACK_COLORS=['#6366f1','#22c55e','#f59e0b','#ef4444','#06b6d4','#a855f7','#ec4899','#14b8a6'];

  function getCtx(){
    if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;
  }
  function getMaster(){
    var ctx=getCtx();
    if(!masterGain||masterGain.context.state==='closed'){masterGain=ctx.createGain();masterGain.connect(ctx.destination);}
    masterGain.gain.value=parseFloat(document.getElementById('mVol').value);return masterGain;
  }

  function playNote(ctx,freq,vel,startAt,durSec){
    var g=ctx.createGain(),end=startAt+durSec,v=(vel/127)*0.7;
    g.connect(getMaster());
    g.gain.setValueAtTime(0,startAt);g.gain.linearRampToValueAtTime(v,startAt+0.006);
    g.gain.exponentialRampToValueAtTime(v*0.3,startAt+0.1);
    g.gain.setValueAtTime(v*0.3,Math.max(startAt+0.11,end-0.08));
    g.gain.exponentialRampToValueAtTime(0.0001,end);
    [[1,1],[2,.5],[3,.25],[4,.12],[5,.06]].forEach(function(h){
      var o=ctx.createOscillator(),hg=ctx.createGain();
      o.type='sine';o.frequency.value=freq*h[0];hg.gain.value=h[1];
      hg.gain.setValueAtTime(h[1],startAt);
      hg.gain.exponentialRampToValueAtTime(Math.max(0.0001,h[1]*(h[0]===1?.6:.025)),startAt+0.08*h[0]*.5);
      o.connect(hg);hg.connect(g);o.start(startAt);o.stop(end+0.05);
    });
  }

  function schedLoop(){
    if(!isPlaying)return;
    var ctx=getCtx(),now=ctx.currentTime,until=now+LOOKAHEAD;
    while(schedIdx<noteEvents.length){
      var ev=noteEvents[schedIdx];
      if(playStartTime+ev.time>until)break;
      var at=playStartTime+ev.time;
      if(at>=now-0.01&&!mutedTracks.has(ev.track))
        playNote(ctx,ev.freq,ev.vel,Math.max(at,now+0.001),ev.dur);
      /* Key light */
      var delay=(at-now)*1000;
      (function(note,dur){setTimeout(function(){litKey(note,true);setTimeout(function(){litKey(note,false);},Math.min(dur*1000,600));},Math.max(0,delay));})(ev.note,ev.dur);
      schedIdx++;
    }
    schedTimer=setTimeout(schedLoop,SCHED_MS);
  }

  function rafTick(){
    if(!isPlaying)return;
    var ctx=getCtx(),el=ctx.currentTime-playStartTime;
    if(el>=totalDuration){stopAudio();document.getElementById('mProgress').value=0;document.getElementById('mTime').textContent='0:00 / '+fmt(totalDuration);return;}
    document.getElementById('mProgress').value=el;
    document.getElementById('mTime').textContent=fmt(el)+' / '+fmt(totalDuration);
    drawRollCursor(el);
    rafId=requestAnimationFrame(rafTick);
  }

  function startAudio(offset){
    stopAudio();if(!noteEvents.length)return;
    var ctx=getCtx();playOffset=offset||0;playStartTime=ctx.currentTime-playOffset;
    schedIdx=0;while(schedIdx<noteEvents.length&&noteEvents[schedIdx].time<playOffset-0.02)schedIdx++;
    isPlaying=true;document.getElementById('mPlay').textContent='⏸';
    schedLoop();rafTick();
  }

  function stopAudio(){
    isPlaying=false;clearTimeout(schedTimer);cancelAnimationFrame(rafId);
    masterGain=null;document.getElementById('mPlay').textContent='▶';
    document.querySelectorAll('.mk2-w,.mk2-b').forEach(function(k){k.classList.remove('lit');});
    document.getElementById('prCursor').style.display='none';
  }

  /* ── Piano Roll ── */
  var rollCanvas=null,rollCtx2=null;
  function drawRoll(notes,duration){
    var canvas=document.getElementById('prCanvas');
    var roll=document.getElementById('pianoRoll');
    canvas.width=roll.clientWidth||600;canvas.height=roll.clientHeight||160;
    rollCanvas=canvas;rollCtx2=canvas.getContext('2d');
    var W=canvas.width,H=canvas.height;
    /* Find note range */
    var minNote=127,maxNote=0;
    notes.forEach(function(n){minNote=Math.min(minNote,n.note);maxNote=Math.max(maxNote,n.note);});
    minNote=Math.max(0,minNote-3);maxNote=Math.min(127,maxNote+3);
    var noteRange=maxNote-minNote||24;
    /* Background */
    rollCtx2.fillStyle='#0f1117';rollCtx2.fillRect(0,0,W,H);
    /* Grid lines */
    for(var r=minNote;r<=maxNote;r++){
      var y=H-(r-minNote)/noteRange*H;
      var semi=r%12;
      if([1,3,6,8,10].includes(semi))rollCtx2.fillStyle='rgba(255,255,255,0.04)';
      else rollCtx2.fillStyle='rgba(255,255,255,0.02)';
      rollCtx2.fillRect(0,y-H/noteRange/2,W,H/noteRange);
    }
    /* Notes */
    var trackSet=new Set(notes.map(function(n){return n.track;}));
    var trackArr=Array.from(trackSet);
    notes.forEach(function(n){
      var x=n.time/duration*W;
      var w=Math.max(2,n.dur/duration*W);
      var y=H-(n.note-minNote+0.8)/noteRange*H;
      var h=Math.max(2,H/noteRange*0.85);
      var ci=trackArr.indexOf(n.track)%TRACK_COLORS.length;
      rollCtx2.fillStyle=TRACK_COLORS[ci];
      rollCtx2.globalAlpha=0.4+n.vel/127*0.6;
      rollCtx2.beginPath();rollCtx2.roundRect(x,y,w,h,1);rollCtx2.fill();
    });
    rollCtx2.globalAlpha=1;
  }

  function drawRollCursor(elapsed){
    var c=document.getElementById('prCursor');
    if(!rollCanvas||!totalDuration){c.style.display='none';return;}
    var pct=elapsed/totalDuration;
    c.style.left=Math.round(pct*rollCanvas.width)+'px';
    c.style.display='block';
  }

  /* ── Keyboard ── */
  function buildKeyboard(){
    var inner=document.getElementById('mk2Inner');inner.innerHTML='';
    var WHITE=[0,2,4,5,7,9,11],HAS_B=[0,1,3,4,5];
    for(var oct=2;oct<=7;oct++){
      WHITE.forEach(function(s,wi){
        var midi=(oct+1)*12+s;
        var w=document.createElement('div');w.className='mk2-w';w.dataset.midi=midi;
        inner.appendChild(w);
        if(HAS_B.includes(wi)){
          var b=document.createElement('div');b.className='mk2-b';b.dataset.midi=midi+1;
          w.style.position='relative';w.appendChild(b);
        }
      });
    }
  }
  function litKey(note,on){
    document.querySelectorAll('[data-midi="'+note+'"]').forEach(function(k){k.classList.toggle('lit',on);});
  }

  /* ── Track list ── */
  function buildTrackList(notes,trackNames){
    var tracksEl=document.getElementById('midiTracks');tracksEl.innerHTML='';
    var trackSet={};
    notes.forEach(function(n){if(!trackSet[n.track])trackSet[n.track]=0;trackSet[n.track]++;});
    Object.keys(trackSet).forEach(function(ti){
      var ci=parseInt(ti)%TRACK_COLORS.length;
      var name=trackNames[ti]||'Track '+(parseInt(ti)+1);
      var row=document.createElement('div');row.className='midi-track';
      row.innerHTML='<div class="midi-track-color" style="background:'+TRACK_COLORS[ci]+'"></div>'
        +'<div class="midi-track-name">'+name+'</div>'
        +'<div class="midi-track-notes">'+trackSet[ti]+' notes</div>'
        +'<button class="midi-track-mute" data-track="'+ti+'">Mute</button>';
      row.querySelector('.midi-track-mute').addEventListener('click',function(){
        var t=parseInt(this.dataset.track);
        if(mutedTracks.has(t)){mutedTracks.delete(t);this.classList.remove('muted');this.textContent='Mute';}
        else{mutedTracks.add(t);this.classList.add('muted');this.textContent='Unmute';}
      });
      tracksEl.appendChild(row);
    });
  }

  /* ── File loading ── */
  function loadMidi(file){
    stopAudio();mutedTracks.clear();
    document.getElementById('midiPlayer').style.display='none';
    document.getElementById('midiMeta').style.display='none';
    var r=new FileReader();
    r.onload=function(e){
      try{
        var midi=parseMidi(e.target.result);
        noteEvents=buildNoteEvents(midi);
        /* Extract track names */
        var trackNames={};
        midi.tracks.forEach(function(track,ti){
          var nm=track.find(function(ev){return ev.type==='name';});
          if(nm)trackNames[ti]=nm.name;
        });
        totalDuration=noteEvents.length?noteEvents[noteEvents.length-1].time+noteEvents[noteEvents.length-1].dur:0;
        document.getElementById('mProgress').max=totalDuration||100;
        document.getElementById('mTime').textContent='0:00 / '+fmt(totalDuration);
        document.getElementById('mInfo').textContent=noteEvents.length+' notes · '+midi.tracks.length+' tracks · '+fmt(totalDuration)+' · '+midi.tpq+' TPQ';
        document.getElementById('midiMeta').style.display='block';
        document.getElementById('midiMeta').textContent='Loaded: '+file.name+' · '+noteEvents.length+' notes';
        document.getElementById('midiPlayer').style.display='block';
        document.getElementById('mPlay').disabled=false;
        document.getElementById('mStop').disabled=false;
        buildKeyboard();
        buildTrackList(noteEvents,trackNames);
        setTimeout(function(){drawRoll(noteEvents,totalDuration);},100);
      }catch(ex){document.getElementById('midiMeta').textContent='Error parsing MIDI: '+ex.message;document.getElementById('midiMeta').style.display='block';}
    };
    r.readAsArrayBuffer(file);
  }

  var drop2=document.getElementById('midiDrop'),fi=document.getElementById('midiFile');
  drop2.addEventListener('dragover',function(e){e.preventDefault();drop2.classList.add('drag-over');});
  drop2.addEventListener('dragleave',function(){drop2.classList.remove('drag-over');});
  drop2.addEventListener('drop',function(e){e.preventDefault();drop2.classList.remove('drag-over');var f=e.dataTransfer.files[0];if(f)loadMidi(f);});
  fi.addEventListener('change',function(){if(this.files[0])loadMidi(this.files[0]);});

  document.getElementById('mPlay').addEventListener('click',function(){
    if(isPlaying){var ctx=getCtx();playOffset=ctx.currentTime-playStartTime;stopAudio();}
    else startAudio(playOffset);
  });
  document.getElementById('mStop').addEventListener('click',function(){stopAudio();playOffset=0;document.getElementById('mProgress').value=0;document.getElementById('mTime').textContent='0:00 / '+fmt(totalDuration);});
  document.getElementById('mRewind').addEventListener('click',function(){var was=isPlaying;stopAudio();playOffset=0;if(was)startAudio(0);});
  document.getElementById('mProgress').addEventListener('input',function(){
    var was=isPlaying;if(was)stopAudio();
    playOffset=parseFloat(this.value);document.getElementById('mTime').textContent=fmt(playOffset)+' / '+fmt(totalDuration);
    if(was)startAudio(playOffset);
  });
  document.getElementById('mVol').addEventListener('input',function(){if(masterGain)masterGain.gain.value=parseFloat(this.value);});

  function fmt(s){if(!s||isNaN(s))return'0:00';return Math.floor(s/60)+':'+(Math.floor(s%60)<10?'0':'')+Math.floor(s%60);}
})();
</script>
"""


# ── Guitar Tuner ──────────────────────────────────────────────────────────────
EXT_GUITAR_CONTENT = """
<div class="page-title">🎸 Guitar Tuner</div>
<p class="page-sub">Chromatic tuner with string-by-string guides for standard and alternate tunings.</p>
<div class="card">
  <div style="margin-bottom:16px">
    <label>Tuning</label>
    <select id="gtTuning" style="margin-bottom:0">
      <option value="E2,A2,D3,G3,B3,E4">Standard (EADGBe)</option>
      <option value="D2,A2,D3,G3,B3,D4">Drop D</option>
      <option value="D2,G2,C3,F3,A3,D4">D Standard</option>
      <option value="C2,G2,C3,F3,A3,D4">Drop C</option>
      <option value="Eb2,Ab2,Db3,Gb3,Bb3,Eb4">Eb Standard</option>
      <option value="E2,A2,D3,G3,G3,E4">Open G</option>
      <option value="E2,B2,E3,G3,B3,E4">Open E</option>
    </select>
  </div>
  <div id="gtStrings" style="display:flex;flex-direction:column;gap:8px;margin-bottom:20px"></div>
  <div style="border-top:1px solid var(--border);padding-top:16px">
    <div style="font-size:.9rem;font-weight:600;color:var(--text);margin-bottom:12px">Live Tuner</div>
    <div style="font-size:3.5rem;font-weight:800;color:var(--accent-text);text-align:center;min-height:56px" id="gtNote">—</div>
    <div style="position:relative;height:24px;background:var(--input-bg);border:1px solid var(--border);border-radius:12px;overflow:hidden;max-width:380px;margin:10px auto 4px">
      <div style="position:absolute;left:50%;top:0;bottom:0;width:2px;background:var(--border);transform:translateX(-50%)"></div>
      <div id="gtNeedle" style="position:absolute;top:3px;bottom:3px;width:4px;border-radius:2px;background:var(--accent);left:50%;transform:translateX(-50%);transition:left .08s,background .1s"></div>
    </div>
    <div style="display:flex;justify-content:space-between;max-width:380px;margin:0 auto 10px;font-size:.7rem;color:var(--text-xfaint)"><span>-50</span><span>0</span><span>+50</span></div>
    <div id="gtStatus" style="text-align:center;color:var(--text-faint);font-size:.85rem;margin-bottom:12px">Click Start to tune</div>
    <div style="display:flex;gap:8px;justify-content:center">
      <button class="btn btn-sm" id="gtStart" style="width:auto;padding:10px 24px">🎤 Start</button>
      <button class="btn btn-sm secondary" id="gtStop" disabled style="width:auto;padding:10px 24px;margin-top:0">Stop</button>
    </div>
  </div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var NOTE_FREQ={'C':261.63,'C#':277.18,'D':293.66,'D#':311.13,'E':329.63,'F':349.23,'F#':369.99,'G':392.00,'G#':415.30,'A':440.00,'A#':466.16,'B':493.88};
  var audioCtx=null,analyser=null,stream=null,rafId=null,buf=null,running=false;

  function parseNote(str){var m=str.match(/([A-G#]+)([0-9]+)/);if(!m)return 440;var n=NOTE_FREQ[m[1]]||440;return n*Math.pow(2,parseInt(m[2])-4);}

  function buildStrings(){
    var el=document.getElementById('gtStrings');el.innerHTML='';
    var tuning=document.getElementById('gtTuning').value.split(',');
    var labels=['6 (low)','5','4','3','2','1 (high)'];
    tuning.forEach(function(note,i){
      var freq=parseNote(note);
      var row=document.createElement('div');
      row.style.cssText='display:flex;align-items:center;gap:10px;padding:10px 14px;background:var(--input-bg);border:1px solid var(--border);border-radius:8px';
      row.innerHTML='<div style="width:60px;font-size:.82rem;color:var(--text-faint)">String '+labels[i]+'</div>'
        +'<div style="font-size:1.2rem;font-weight:700;color:var(--accent-text);width:36px">'+note.replace(/[0-9]/,'')+'</div>'
        +'<div style="font-size:.8rem;color:var(--text-faint)">'+Math.round(freq)+' Hz</div>';
      el.appendChild(row);
    });
  }

  function noteFromFreq(f){var n=12*Math.log2(f/440)+69;var midi=Math.round(n);return{name:NOTES[((midi%12)+12)%12],octave:Math.floor(midi/12)-1,cents:Math.round((n-midi)*100)};}

  function autoCorrelate(buf,sr){
    var N=buf.length,M=Math.floor(N/2),rms=0;
    for(var i=0;i<N;i++)rms+=buf[i]*buf[i];rms=Math.sqrt(rms/N);if(rms<0.008)return -1;
    var best=-1,bestC=-1,lastC=1,found=false;
    for(var o=2;o<M;o++){var c=0;for(var i=0;i<M;i++)c+=Math.abs(buf[i]-buf[i+o]);c=1-c/M;
      if(c>0.9&&c>lastC){found=true;if(c>bestC){bestC=c;best=o;}}else if(found)break;lastC=c;}
    return best<0||bestC<0.9?-1:sr/best;
  }

  function tick(){
    if(!running)return;
    analyser.getFloatTimeDomainData(buf);
    var f=autoCorrelate(buf,audioCtx.sampleRate);
    if(f>50&&f<1200){
      var n=noteFromFreq(f);
      document.getElementById('gtNote').textContent=n.name+n.octave;
      var pct=50+Math.max(-50,Math.min(50,n.cents));
      var needle=document.getElementById('gtNeedle');needle.style.left=pct+'%';
      var abs=Math.abs(n.cents);
      needle.style.background=abs<=4?'#22c55e':abs<=15?'#eab308':'#ef4444';
      document.getElementById('gtStatus').textContent=abs<=4?'✅ In tune!':(n.cents<0?'▲ Tune up '+abs+'¢':'▼ Tune down '+abs+'¢');
    }
    rafId=requestAnimationFrame(tick);
  }

  document.getElementById('gtTuning').addEventListener('change',buildStrings);
  document.getElementById('gtStart').addEventListener('click',function(){
    navigator.mediaDevices.getUserMedia({audio:{echoCancellation:false,noiseSuppression:false},video:false})
    .then(function(s){stream=s;audioCtx=new(window.AudioContext||window.webkitAudioContext)();analyser=audioCtx.createAnalyser();analyser.fftSize=4096;buf=new Float32Array(analyser.fftSize);audioCtx.createMediaStreamSource(s).connect(analyser);running=true;document.getElementById('gtStart').disabled=true;document.getElementById('gtStop').disabled=false;tick();})
    .catch(function(e){document.getElementById('gtStatus').textContent='Mic denied.';});
  });
  document.getElementById('gtStop').addEventListener('click',function(){
    running=false;cancelAnimationFrame(rafId);if(stream)stream.getTracks().forEach(function(t){t.stop();});if(audioCtx)audioCtx.close();
    document.getElementById('gtStart').disabled=false;document.getElementById('gtStop').disabled=true;document.getElementById('gtNote').textContent='—';document.getElementById('gtStatus').textContent='Stopped';
  });
  buildStrings();
})();
</script>
"""

# ── Drum Machine ──────────────────────────────────────────────────────────────
EXT_DRUM_CSS = """
.drum-grid{display:grid;gap:6px;margin:16px 0}
.drum-row{display:flex;align-items:center;gap:6px}
.drum-label{width:72px;font-size:.78rem;font-weight:600;color:var(--text-muted);text-align:right;flex-shrink:0}
.drum-steps{display:flex;gap:4px;flex:1}
.drum-step{flex:1;height:36px;border-radius:6px;border:1px solid var(--border);
  background:var(--input-bg);cursor:pointer;transition:background .1s;min-width:0}
.drum-step.on{background:var(--accent);border-color:var(--accent)}
.drum-step.accent{background:#22c55e;border-color:#166534}
.drum-step.playing{outline:2px solid #fff;outline-offset:1px}
.drum-step:nth-child(4n+1){border-left:2px solid var(--border)}
.drum-transport{display:flex;align-items:center;gap:10px;margin-top:14px;flex-wrap:wrap}
.drum-vol{width:70px;accent-color:var(--accent)}
"""

EXT_DRUM_CONTENT = """
<div class="page-title">🥁 Drum Machine</div>
<p class="page-sub">16-step sequencer. Click steps to toggle them. Right-click a step for an accent. Adjust BPM and swing.</p>
<div class="card">
  <div class="drum-grid" id="drumGrid"></div>
  <div class="drum-transport">
    <button class="btn btn-sm" id="dmPlay" style="width:auto;padding:10px 24px">▶ Play</button>
    <button class="btn btn-sm secondary" id="dmStop" style="width:auto;padding:10px 24px;margin-top:0">■ Stop</button>
    <button class="btn btn-sm secondary" id="dmClear" style="width:auto;padding:10px 16px;margin-top:0">Clear</button>
    <label style="font-size:.82rem;color:var(--text-muted);margin-bottom:0">BPM</label>
    <input type="number" id="dmBpm" value="120" min="40" max="240" style="width:70px;margin-bottom:0"/>
    <label style="font-size:.82rem;color:var(--text-muted);margin-bottom:0">Swing</label>
    <input type="range" id="dmSwing" min="0" max="0.3" step="0.01" value="0" style="width:80px;accent-color:var(--accent);margin-bottom:0"/>
    <label style="font-size:.82rem;color:var(--text-muted);margin-bottom:0">Vol</label>
    <input type="range" class="drum-vol" id="dmVol" min="0" max="1" step="0.05" value="0.8"/>
  </div>
  <div id="dmCurrentStep" style="font-size:.78rem;color:var(--text-faint);margin-top:8px;text-align:center"></div>
</div>
<script>
(function(){
  var DRUMS=[
    {name:'Kick',     color:'#6366f1', gen:function(ctx,t,v){kick(ctx,t,v);}},
    {name:'Snare',    color:'#f59e0b', gen:function(ctx,t,v){snare(ctx,t,v);}},
    {name:'Hi-hat',   color:'#22c55e', gen:function(ctx,t,v){hihat(ctx,t,v,false);}},
    {name:'Open HH',  color:'#06b6d4', gen:function(ctx,t,v){hihat(ctx,t,v,true);}},
    {name:'Clap',     color:'#ec4899', gen:function(ctx,t,v){clap(ctx,t,v);}},
    {name:'Tom Hi',   color:'#a855f7', gen:function(ctx,t,v){tom(ctx,t,v,200);}},
    {name:'Tom Lo',   color:'#ef4444', gen:function(ctx,t,v){tom(ctx,t,v,100);}},
    {name:'Cowbell',  color:'#eab308', gen:function(ctx,t,v){cowbell(ctx,t,v);}},
  ];
  var STEPS=16;
  var pattern=DRUMS.map(function(){return new Array(STEPS).fill(0);});/* 0=off,1=on,2=accent */
  var audioCtx=null,isPlaying=false,currentStep=0,nextStepTime=0,timerId=null,rafId=null;

  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function vol(){return parseFloat(document.getElementById('dmVol').value);}

  /* ── Drum synthesis ── */
  function kick(ctx,t,v){
    var o=ctx.createOscillator(),g=ctx.createGain();
    o.frequency.setValueAtTime(150,t);o.frequency.exponentialRampToValueAtTime(30,t+0.2);
    g.gain.setValueAtTime(v*2,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.4);
    o.connect(g);g.connect(ctx.destination);o.start(t);o.stop(t+0.5);
  }
  function snare(ctx,t,v){
    /* Noise */
    var buf=ctx.createBuffer(1,ctx.sampleRate*0.2,ctx.sampleRate);
    var d=buf.getChannelData(0);for(var i=0;i<d.length;i++)d[i]=Math.random()*2-1;
    var src=ctx.createBufferSource(),g=ctx.createGain(),filt=ctx.createBiquadFilter();
    filt.type='highpass';filt.frequency.value=800;
    g.gain.setValueAtTime(v,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.2);
    src.buffer=buf;src.connect(filt);filt.connect(g);g.connect(ctx.destination);src.start(t);src.stop(t+0.22);
    /* Tone */
    var o=ctx.createOscillator(),g2=ctx.createGain();
    o.frequency.value=200;g2.gain.setValueAtTime(v*0.5,t);g2.gain.exponentialRampToValueAtTime(0.001,t+0.08);
    o.connect(g2);g2.connect(ctx.destination);o.start(t);o.stop(t+0.1);
  }
  function hihat(ctx,t,v,open){
    var buf=ctx.createBuffer(1,ctx.sampleRate*0.05,ctx.sampleRate);
    var d=buf.getChannelData(0);for(var i=0;i<d.length;i++)d[i]=Math.random()*2-1;
    var src=ctx.createBufferSource(),g=ctx.createGain(),filt=ctx.createBiquadFilter();
    filt.type='highpass';filt.frequency.value=7000;
    var dur=open?0.3:0.05;
    g.gain.setValueAtTime(v*0.7,t);g.gain.exponentialRampToValueAtTime(0.001,t+dur);
    src.buffer=buf;src.connect(filt);filt.connect(g);g.connect(ctx.destination);src.start(t);src.stop(t+dur+0.02);
  }
  function clap(ctx,t,v){
    for(var i=0;i<3;i++){(function(i){
      var buf=ctx.createBuffer(1,ctx.sampleRate*0.02,ctx.sampleRate);
      var d=buf.getChannelData(0);for(var j=0;j<d.length;j++)d[j]=Math.random()*2-1;
      var src=ctx.createBufferSource(),g=ctx.createGain(),filt=ctx.createBiquadFilter();
      filt.type='bandpass';filt.frequency.value=1200;
      g.gain.setValueAtTime(v*0.6,t+i*0.01);g.gain.exponentialRampToValueAtTime(0.001,t+i*0.01+0.08);
      src.buffer=buf;src.connect(filt);filt.connect(g);g.connect(ctx.destination);src.start(t+i*0.01);src.stop(t+i*0.01+0.1);
    })(i);}
  }
  function tom(ctx,t,v,freq){
    var o=ctx.createOscillator(),g=ctx.createGain();
    o.frequency.setValueAtTime(freq,t);o.frequency.exponentialRampToValueAtTime(freq*0.5,t+0.2);
    g.gain.setValueAtTime(v*1.5,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.3);
    o.connect(g);g.connect(ctx.destination);o.start(t);o.stop(t+0.35);
  }
  function cowbell(ctx,t,v){
    var o=ctx.createOscillator(),o2=ctx.createOscillator(),g=ctx.createGain();
    o.type='square';o.frequency.value=562;o2.type='square';o2.frequency.value=845;
    g.gain.setValueAtTime(v*0.5,t);g.gain.exponentialRampToValueAtTime(0.001,t+0.5);
    o.connect(g);o2.connect(g);g.connect(ctx.destination);o.start(t);o2.start(t);o.stop(t+0.55);o2.stop(t+0.55);
  }

  /* ── Sequencer ── */
  function stepDuration(){
    var bpm=parseInt(document.getElementById('dmBpm').value)||120;
    return(60/bpm)/4;/* 16th note */
  }
  function scheduler(){
    var ctx=getCtx(),swing=parseFloat(document.getElementById('dmSwing').value)||0;
    while(nextStepTime<ctx.currentTime+0.2){
      var t=nextStepTime;
      var isOdd=currentStep%2===1;
      var swingOffset=isOdd?swing*stepDuration():0;
      DRUMS.forEach(function(drum,di){
        var v=pattern[di][currentStep];
        if(v>0)drum.gen(ctx,t+swingOffset,v===2?vol()*1.4:vol());
      });
      /* Visual */
      (function(step){setTimeout(function(){
        document.querySelectorAll('.drum-step').forEach(function(el){el.classList.remove('playing');});
        document.querySelectorAll('.drum-step[data-step="'+step+'"]').forEach(function(el){el.classList.add('playing');});
        document.getElementById('dmCurrentStep').textContent='Step '+(step+1)+' / '+STEPS;
      },(t-ctx.currentTime)*1000);})(currentStep);
      currentStep=(currentStep+1)%STEPS;
      nextStepTime+=stepDuration();
    }
    timerId=setTimeout(scheduler,50);
  }

  function buildGrid(){
    var grid=document.getElementById('drumGrid');grid.innerHTML='';
    DRUMS.forEach(function(drum,di){
      var row=document.createElement('div');row.className='drum-row';
      var label=document.createElement('div');label.className='drum-label';label.textContent=drum.name;
      row.appendChild(label);
      var steps=document.createElement('div');steps.className='drum-steps';
      for(var s=0;s<STEPS;s++){
        var btn=document.createElement('button');btn.className='drum-step';
        btn.dataset.drum=di;btn.dataset.step=s;
        if(pattern[di][s]===1)btn.classList.add('on');
        if(pattern[di][s]===2)btn.classList.add('accent');
        btn.style.background=pattern[di][s]?drum.color:'';
        btn.style.borderColor=pattern[di][s]?drum.color:'';
        btn.addEventListener('click',function(){
          var d=parseInt(this.dataset.drum),st=parseInt(this.dataset.step);
          pattern[d][st]=(pattern[d][st]+1)%2;
          this.style.background=pattern[d][st]?DRUMS[d].color:'';
          this.style.borderColor=pattern[d][st]?DRUMS[d].color:'';
          this.classList.toggle('on',pattern[d][st]===1);
        });
        btn.addEventListener('contextmenu',function(e){
          e.preventDefault();
          var d=parseInt(this.dataset.drum),st=parseInt(this.dataset.step);
          pattern[d][st]=pattern[d][st]===2?0:2;
          this.style.background=pattern[d][st]?'#22c55e':'';
          this.style.borderColor=pattern[d][st]?'#166534':'';
          this.classList.toggle('accent',pattern[d][st]===2);
          this.classList.toggle('on',false);
        });
        steps.appendChild(btn);
      }
      row.appendChild(steps);grid.appendChild(row);
    });
    /* Default pattern */
    pattern[0][0]=pattern[0][8]=1;/* Kick */
    pattern[1][4]=pattern[1][12]=1;/* Snare */
    for(var s=0;s<16;s+=2)pattern[2][s]=1;/* Hi-hat */
    buildGrid.refresh();
  }
  buildGrid.refresh=function(){
    document.querySelectorAll('.drum-step').forEach(function(btn){
      var d=parseInt(btn.dataset.drum),s=parseInt(btn.dataset.step);
      btn.style.background=pattern[d][s]?DRUMS[d].color:'';
      btn.style.borderColor=pattern[d][s]?DRUMS[d].color:'';
      btn.classList.toggle('on',pattern[d][s]===1);
      btn.classList.toggle('accent',pattern[d][s]===2);
    });
  };

  document.getElementById('dmPlay').addEventListener('click',function(){
    if(isPlaying)return;isPlaying=true;
    var ctx=getCtx();currentStep=0;nextStepTime=ctx.currentTime+0.05;
    scheduler();document.getElementById('dmPlay').disabled=true;
  });
  document.getElementById('dmStop').addEventListener('click',function(){
    isPlaying=false;clearTimeout(timerId);
    document.getElementById('dmPlay').disabled=false;
    document.querySelectorAll('.drum-step').forEach(function(el){el.classList.remove('playing');});
    document.getElementById('dmCurrentStep').textContent='';
  });
  document.getElementById('dmClear').addEventListener('click',function(){
    pattern=DRUMS.map(function(){return new Array(STEPS).fill(0);});
    buildGrid.refresh();
  });

  buildGrid();
})();
</script>
"""

# ── Arpeggiator ───────────────────────────────────────────────────────────────
EXT_ARP_CONTENT = """
<div class="page-title">🎵 Arpeggiator</div>
<p class="page-sub">Pick a chord and pattern, hear it arpeggiated in real time. Great for getting composition ideas.</p>
<div class="card">
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:16px">
    <div><label>Root Note</label>
      <select id="arpRoot" style="margin-bottom:0">
        <option>C</option><option>C#</option><option>D</option><option>D#</option>
        <option>E</option><option>F</option><option>F#</option><option>G</option>
        <option>G#</option><option>A</option><option>A#</option><option>B</option>
      </select></div>
    <div><label>Chord Type</label>
      <select id="arpChord" style="margin-bottom:0">
        <option value="0,4,7">Major</option><option value="0,3,7">Minor</option>
        <option value="0,4,7,11">Major 7th</option><option value="0,4,7,10">Dom 7th</option>
        <option value="0,3,7,10">Minor 7th</option><option value="0,4,8">Augmented</option>
        <option value="0,3,6">Diminished</option><option value="0,2,7">Sus2</option>
        <option value="0,5,7">Sus4</option><option value="0,4,7,9">6th</option>
        <option value="0,4,7,14">Add9</option><option value="0,2,4,7,9">Pentatonic</option>
      </select></div>
    <div><label>Pattern</label>
      <select id="arpPattern" style="margin-bottom:0">
        <option value="up">Up ↑</option><option value="down">Down ↓</option>
        <option value="updown">Up-Down ↑↓</option><option value="downup">Down-Up ↓↑</option>
        <option value="random">Random</option><option value="chord">Chord (all)</option>
        <option value="up2">Up ×2 octaves</option>
      </select></div>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-bottom:20px">
    <div><label>BPM</label><input type="number" id="arpBpm" value="120" min="40" max="300" style="margin-bottom:0"/></div>
    <div><label>Note Length</label>
      <select id="arpLen" style="margin-bottom:0">
        <option value="8">8th note</option><option value="4" selected>Quarter</option>
        <option value="2">Half</option><option value="16">16th note</option>
      </select></div>
    <div><label>Octave</label>
      <select id="arpOct" style="margin-bottom:0">
        <option value="3">Octave 3</option><option value="4" selected>Octave 4</option>
        <option value="5">Octave 5</option>
      </select></div>
  </div>
  <div style="display:flex;gap:10px;margin-bottom:14px;align-items:center">
    <button class="btn btn-sm" id="arpPlay" style="width:auto;padding:10px 24px">▶ Play</button>
    <button class="btn btn-sm secondary" id="arpStop" style="width:auto;padding:10px 24px;margin-top:0">■ Stop</button>
    <span style="font-size:.82rem;color:var(--text-muted);margin-left:4px">Vol</span>
    <input type="range" id="arpVol" min="0" max="1" step="0.05" value="0.6" style="width:80px;accent-color:var(--accent);margin-bottom:0"/>
  </div>
  <div id="arpDisplay" style="display:flex;gap:6px;flex-wrap:wrap;min-height:44px"></div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null,isPlaying=false,arpIdx=0,nextTime=0,timerId=null;
  var sequence=[],dispEls=[];

  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function freq(midi){return 440*Math.pow(2,(midi-69)/12);}

  function pianoNote(ctx,f,start,dur,vol){
    var g=ctx.createGain(),end=start+dur;g.connect(ctx.destination);
    g.gain.setValueAtTime(0,start);g.gain.linearRampToValueAtTime(vol,start+0.006);
    g.gain.exponentialRampToValueAtTime(vol*0.3,start+0.1);g.gain.setValueAtTime(vol*0.3,Math.max(start+0.11,end-0.08));g.gain.exponentialRampToValueAtTime(0.0001,end);
    [[1,1],[2,.5],[3,.25],[4,.12]].forEach(function(h){var o=ctx.createOscillator(),hg=ctx.createGain();o.type='sine';o.frequency.value=f*h[0];hg.gain.value=h[1];hg.gain.setValueAtTime(h[1],start);hg.gain.exponentialRampToValueAtTime(Math.max(0.0001,h[1]*(h[0]===1?.6:.03)),start+0.08*h[0]*.5);o.connect(hg);hg.connect(g);o.start(start);o.stop(end+0.05);});
  }

  function buildSequence(){
    var root=NOTES.indexOf(document.getElementById('arpRoot').value);
    var oct=parseInt(document.getElementById('arpOct').value);
    var baseMidi=(oct+1)*12+root;
    var intervals=document.getElementById('arpChord').value.split(',').map(Number);
    var pattern=document.getElementById('arpPattern').value;
    var notes=intervals.map(function(s){return baseMidi+s;});
    if(pattern==='up')sequence=notes;
    else if(pattern==='down')sequence=notes.slice().reverse();
    else if(pattern==='updown')sequence=notes.concat(notes.slice(1,-1).reverse());
    else if(pattern==='downup'){var d=notes.slice().reverse();sequence=d.concat(d.slice(1,-1).reverse());}
    else if(pattern==='random')sequence=notes.slice().sort(function(){return Math.random()-.5;});
    else if(pattern==='chord'){sequence=notes;}
    else if(pattern==='up2')sequence=notes.concat(notes.map(function(n){return n+12;}));
    /* Build display */
    var disp=document.getElementById('arpDisplay');disp.innerHTML='';dispEls=[];
    sequence.forEach(function(midi){
      var el=document.createElement('div');
      el.style.cssText='padding:8px 12px;border-radius:8px;background:var(--input-bg);border:1px solid var(--border);font-size:.9rem;font-weight:600;color:var(--accent-text);transition:background .05s,transform .05s';
      el.textContent=NOTES[((midi%12)+12)%12]+(Math.floor(midi/12)-1);
      disp.appendChild(el);dispEls.push(el);
    });
  }

  function stepDur(){var bpm=parseInt(document.getElementById('arpBpm').value)||120;var div=parseInt(document.getElementById('arpLen').value)||4;return(60/bpm)*(4/div);}

  function scheduler(){
    var ctx=getCtx(),vol=parseFloat(document.getElementById('arpVol').value);
    while(nextTime<ctx.currentTime+0.3){
      var t=nextTime,dur=stepDur();
      var pattern=document.getElementById('arpPattern').value;
      if(pattern==='chord'){
        sequence.forEach(function(midi){pianoNote(ctx,freq(midi),t,dur*0.85,vol/sequence.length*1.5);});
        var idx2=0;
        (function(idx2){setTimeout(function(){
          dispEls.forEach(function(el){el.style.background='var(--accent)';el.style.transform='scale(1.1)';});
          setTimeout(function(){dispEls.forEach(function(el){el.style.background='var(--input-bg)';el.style.transform='';});},dur*800);
        },(t-ctx.currentTime)*1000);})(0);
      } else {
        var midi=sequence[arpIdx%sequence.length];
        pianoNote(ctx,freq(midi),t,dur*0.8,vol);
        (function(idx){setTimeout(function(){
          dispEls.forEach(function(el,i){
            el.style.background=i===idx?'var(--accent)':'var(--input-bg)';
            el.style.transform=i===idx?'scale(1.15)':'';
          });
        },(t-ctx.currentTime)*1000);})(arpIdx%sequence.length);
      }
      arpIdx++;nextTime+=dur;
    }
    timerId=setTimeout(scheduler,50);
  }

  document.getElementById('arpPlay').addEventListener('click',function(){
    if(isPlaying)return;buildSequence();if(!sequence.length)return;
    isPlaying=true;arpIdx=0;nextTime=getCtx().currentTime+0.05;
    scheduler();document.getElementById('arpPlay').disabled=true;
  });
  document.getElementById('arpStop').addEventListener('click',function(){
    isPlaying=false;clearTimeout(timerId);
    document.getElementById('arpPlay').disabled=false;
    dispEls.forEach(function(el){el.style.background='var(--input-bg)';el.style.transform='';});
  });
  ['arpRoot','arpChord','arpPattern','arpOct'].forEach(function(id){
    document.getElementById(id).addEventListener('change',function(){if(isPlaying){buildSequence();}else{buildSequence();}});
  });
  buildSequence();
})();
</script>
"""

# ── Music Flashcards ──────────────────────────────────────────────────────────
EXT_FLASH_CSS = """
.flash-card{perspective:600px;cursor:pointer;margin:0 auto;max-width:420px;height:200px}
.flash-inner{position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform .5s}
.flash-card.flipped .flash-inner{transform:rotateY(180deg)}
.flash-front,.flash-back{position:absolute;inset:0;border-radius:14px;border:1px solid var(--border);
  display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;
  backface-visibility:hidden;-webkit-backface-visibility:hidden}
.flash-front{background:var(--card)}
.flash-back{background:var(--accent);color:#fff;transform:rotateY(180deg)}
.flash-q{font-size:1.1rem;font-weight:700;color:var(--text);text-align:center;line-height:1.4}
.flash-a{font-size:1.2rem;font-weight:700;color:#fff;text-align:center;line-height:1.4}
.flash-hint{font-size:.78rem;color:var(--text-faint);margin-top:8px;text-align:center}
.flash-progress{height:5px;background:var(--border);border-radius:3px;margin-bottom:16px;overflow:hidden}
.flash-progress-fill{height:100%;background:var(--accent);border-radius:3px;transition:width .3s}
.fc-deck-btn{padding:6px 14px;border:1px solid var(--border);border-radius:8px;
  background:var(--input-bg);color:var(--text-muted);font-size:.83rem;cursor:pointer;
  transition:all .15s;margin:0 4px 6px 0}
.fc-deck-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
/* Staff reading */
.sr-kb{display:flex;height:60px;position:relative;background:#111;padding:3px 3px 0}
.sr-w{flex:1;background:#fff;border:1px solid #bbb;border-radius:0 0 4px 4px;cursor:pointer;
  position:relative;display:flex;align-items:flex-end;justify-content:center;
  padding-bottom:2px;transition:background .08s;min-width:0}
.sr-w:hover{background:#e0e7ff}
.sr-w.ok{background:#86efac!important}
.sr-w.bad{background:#fca5a5!important}
.sr-b{position:absolute;top:3px;left:58%;width:56%;height:55%;background:#1e2130;
  border:1px solid #475569;border-radius:0 0 3px 3px;z-index:2;cursor:pointer;
  display:flex;align-items:flex-end;justify-content:center;padding-bottom:1px;
  transition:background .08s}
.sr-b:hover{background:#4f46e5}
.sr-b.ok{background:#166534!important}
.sr-b.bad{background:#7f1d1d!important}
.sr-klbl{font-size:.48rem;color:#999;pointer-events:none;text-align:center}
.sr-blbl{font-size:.44rem;color:#94a3b8;pointer-events:none;text-align:center;line-height:1.2}
"""

EXT_FLASH_CONTENT = """
<div class="page-title">&#x1F0A1; Music Flashcards</div>
<p class="page-sub">Click a card to flip it, then mark yourself. Staff Reading shows a note on a real staff — click the correct key.</p>

<div class="card">
  <div style="margin-bottom:14px;display:flex;flex-wrap:wrap;gap:0">
    <button class="fc-deck-btn active" id="btn-all" onclick="loadDeck('all',this)">All</button>
    <button class="fc-deck-btn" id="btn-notes" onclick="loadDeck('notes',this)">Notes</button>
    <button class="fc-deck-btn" id="btn-keys" onclick="loadDeck('keys',this)">Key Sigs</button>
    <button class="fc-deck-btn" id="btn-intervals" onclick="loadDeck('intervals',this)">Intervals</button>
    <button class="fc-deck-btn" id="btn-chords" onclick="loadDeck('chords',this)">Chords</button>
    <button class="fc-deck-btn" id="btn-staff" onclick="loadDeck('staff',this)">&#x1F3BC; Staff Reading</button>
  </div>

  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:12px">
    <div style="text-align:center"><div id="fcGotN" style="font-size:1.5rem;font-weight:800;color:#22c55e">0</div><div style="font-size:.7rem;color:var(--text-faint)">GOT IT</div></div>
    <div style="text-align:center"><div id="fcLeftN" style="font-size:1.5rem;font-weight:800;color:var(--accent-text)">0</div><div style="font-size:.7rem;color:var(--text-faint)">LEFT</div></div>
    <div style="text-align:center"><div id="fcBadN" style="font-size:1.5rem;font-weight:800;color:#ef4444">0</div><div style="font-size:.7rem;color:var(--text-faint)">AGAIN</div></div>
  </div>

  <div class="flash-progress"><div class="flash-progress-fill" id="fcBar" style="width:0%"></div></div>

  <!-- Text card (hidden in staff mode) -->
  <div id="textCardWrap">
    <div class="flash-card" id="fcCard" onclick="doFlip()">
      <div class="flash-inner" id="fcInner">
        <div class="flash-front">
          <div class="flash-q" id="fcQ"></div>
          <div class="flash-hint" id="fcHint"></div>
        </div>
        <div class="flash-back">
          <div class="flash-a" id="fcA"></div>
        </div>
      </div>
    </div>
    <div id="fcTip" style="text-align:center;font-size:.76rem;color:var(--text-faint);margin-top:8px">Click card to flip</div>
    <div id="fcBtns" style="display:none;gap:10px;justify-content:center;margin-top:10px">
      <button class="btn btn-sm" onclick="markGot()" style="background:#22c55e;width:auto;padding:10px 22px">Got it</button>
      <button class="btn btn-sm" onclick="markAgain()" style="background:#ef4444;margin-top:0;width:auto;padding:10px 22px">Again</button>
    </div>
  </div>

  <!-- Staff reading (hidden in text mode) -->
  <div id="staffWrap" style="display:none">
    <div style="margin-bottom:10px;display:flex;gap:6px;flex-wrap:wrap">
      <button class="fc-deck-btn active" id="srBtnBoth" onclick="srSetClef('both',this)">Both</button>
      <button class="fc-deck-btn" id="srBtnTreble" onclick="srSetClef('treble',this)">Treble</button>
      <button class="fc-deck-btn" id="srBtnBass" onclick="srSetClef('bass',this)">Bass</button>
      <button class="fc-deck-btn" id="srBtnAcc" onclick="srToggleAcc(this)">&#x266F;&#x266D; Off</button>
    </div>
    <div style="background:#fff;border-radius:10px;padding:10px;text-align:center;margin-bottom:10px">
      <canvas id="srCv" width="460" height="200" style="max-width:100%;height:200px"></canvas>
    </div>
    <div id="srFb" style="text-align:center;font-size:.95rem;font-weight:700;min-height:28px;padding:6px;border-radius:8px;margin-bottom:8px"></div>
    <div style="font-size:.74rem;color:var(--text-faint);text-align:center;margin-bottom:4px">Click the correct note</div>
    <div style="border:1px solid var(--border);border-radius:8px;overflow:hidden">
      <div class="sr-kb" id="srKb"></div>
    </div>
    <div style="text-align:center;margin-top:12px">
      <button class="btn btn-sm" onclick="srNext()" style="width:auto;padding:10px 24px">Next Note</button>
    </div>
  </div>
</div>

<script>
/* ── CARDS DATA ── */
var FC_DATA={
  notes:[
    {q:'What note is between C and D?',a:'C# / Db',h:'One semitone above C'},
    {q:'How many semitones in an octave?',a:'12',h:'C to the next C'},
    {q:'Enharmonic of F#?',a:'Gb',h:'Same pitch, different name'},
    {q:'Which two notes have no sharp/flat between them and the next?',a:'E and B',h:'No black keys between E-F or B-C'},
    {q:'Treble clef lines bottom to top?',a:'E G B D F',h:'"Every Good Boy Does Fine"'},
    {q:'Treble clef spaces bottom to top?',a:'F A C E',h:'"FACE"'},
    {q:'Bass clef lines bottom to top?',a:'G B D F A',h:'"Good Boys Do Fine Always"'},
    {q:'Bass clef spaces bottom to top?',a:'A C E G',h:'"All Cows Eat Grass"'},
    {q:'Where is middle C on the treble staff?',a:'Ledger line below the staff',h:'C4'},
    {q:'How many cents in a semitone?',a:'100 cents',h:'Equal temperament'},
  ],
  keys:[
    {q:'How many sharps in G major?',a:'1 — F#',h:''},
    {q:'How many flats in F major?',a:'1 — Bb',h:''},
    {q:'What key has 4 sharps?',a:'E major',h:'F# C# G# D#'},
    {q:'Relative minor of C major?',a:'A minor',h:'6th degree'},
    {q:'What key has 3 flats?',a:'Eb major',h:'Bb Eb Ab'},
    {q:'How many sharps in B major?',a:'5',h:'F# C# G# D# A#'},
    {q:'Order of sharps?',a:'F C G D A E B',h:'"Fat Cats Go Down Alleys Eating Birds"'},
    {q:'Order of flats?',a:'B E A D G C F',h:'Reverse of the sharps order'},
    {q:'Relative minor of G major?',a:'E minor',h:'6th scale degree of G'},
    {q:'What key has 7 flats?',a:'Cb major',h:'All 7 notes are flat'},
  ],
  intervals:[
    {q:'C to G?',a:'Perfect 5th — 7 semitones',h:''},
    {q:'C to E?',a:'Major 3rd — 4 semitones',h:''},
    {q:'C to Eb?',a:'Minor 3rd — 3 semitones',h:''},
    {q:'C to B?',a:'Major 7th — 11 semitones',h:''},
    {q:'C to Bb?',a:'Minor 7th — 10 semitones',h:''},
    {q:'How many semitones in a tritone?',a:'6',h:'Half an octave'},
    {q:'Minor 2nd = how many semitones?',a:'1',h:'Smallest standard interval'},
    {q:'C to A?',a:'Major 6th — 9 semitones',h:''},
    {q:'C to Ab?',a:'Minor 6th — 8 semitones',h:''},
    {q:'C to F?',a:'Perfect 4th — 5 semitones',h:''},
  ],
  chords:[
    {q:'Notes in C major triad?',a:'C E G',h:'Root + M3 + P5'},
    {q:'Notes in A minor triad?',a:'A C E',h:'Root + m3 + P5'},
    {q:'Dominant 7th chord?',a:'Root, M3, P5, m7',h:'e.g. G7 = G B D F'},
    {q:'What is a diminished chord?',a:'Root + m3 + d5',h:'Two stacked minor 3rds'},
    {q:'What does V7 mean?',a:'Dominant 7th on the 5th degree',h:'In C: G7'},
    {q:'Sus4 chord?',a:'Root, P4, P5 — no 3rd',h:'Suspended 4th replaces the 3rd'},
    {q:'Augmented chord?',a:'Root + M3 + aug5',h:'Raised 5th'},
    {q:'Major 7th chord?',a:'Root, M3, P5, M7',h:'e.g. Cmaj7 = C E G B'},
  ],
};

/* ── TEXT FLASHCARDS ── */
var fcDeck=[],fcIdx=0,fcFlipped=false,fcGot=0,fcBad=0,fcMode='text';

function loadDeck(type,btn){
  document.querySelectorAll('.fc-deck-btn').forEach(function(b){b.classList.remove('active');});
  if(btn)btn.classList.add('active');

  if(type==='staff'){
    fcMode='staff';
    document.getElementById('textCardWrap').style.display='none';
    document.getElementById('staffWrap').style.display='block';
    if(!srKbBuilt){srKbBuilt=true;buildSrKb();}
    if(!srCur)srNext();
    return;
  }

  fcMode='text';
  document.getElementById('textCardWrap').style.display='block';
  document.getElementById('staffWrap').style.display='none';

  var cards=[];
  if(type==='all'){cards=FC_DATA.notes.concat(FC_DATA.keys,FC_DATA.intervals,FC_DATA.chords);}
  else cards=(FC_DATA[type]||[]).slice();
  /* Fisher-Yates shuffle */
  for(var i=cards.length-1;i>0;i--){
    var j=Math.floor(Math.random()*(i+1));
    var t=cards[i];cards[i]=cards[j];cards[j]=t;
  }
  fcDeck=cards;fcIdx=0;fcGot=0;fcBad=0;fcFlipped=false;
  document.getElementById('fcCard').classList.remove('flipped');
  document.getElementById('fcBtns').style.display='none';
  document.getElementById('fcTip').style.display='block';
  showFC();
}

function showFC(){
  if(!fcDeck||!fcDeck.length){
    document.getElementById('fcQ').textContent='No cards found.';
    return;
  }
  fcFlipped=false;
  document.getElementById('fcCard').classList.remove('flipped');
  document.getElementById('fcBtns').style.display='none';
  document.getElementById('fcTip').style.display='block';
  var c=fcDeck[fcIdx]||fcDeck[0];
  if(!c)return;
  document.getElementById('fcQ').textContent=c.q;
  document.getElementById('fcA').textContent=c.a;
  document.getElementById('fcHint').textContent=c.h||'';
  document.getElementById('fcBar').style.width=Math.round(fcIdx/fcDeck.length*100)+'%';
  document.getElementById('fcGotN').textContent=fcGot;
  document.getElementById('fcLeftN').textContent=Math.max(0,fcDeck.length-fcIdx);
  document.getElementById('fcBadN').textContent=fcBad;
}

function doFlip(){
  if(fcMode!=='text'||!fcDeck.length)return;
  fcFlipped=!fcFlipped;
  document.getElementById('fcCard').classList.toggle('flipped',fcFlipped);
  document.getElementById('fcBtns').style.display=fcFlipped?'flex':'none';
  document.getElementById('fcTip').style.display=fcFlipped?'none':'block';
}

function markGot(){
  fcGot++;fcIdx++;
  if(fcIdx>=fcDeck.length){
    document.getElementById('fcQ').textContent='Done! '+fcGot+' correct, '+fcBad+' again.';
    document.getElementById('fcBtns').style.display='none';
    return;
  }
  showFC();
}

function markAgain(){
  fcBad++;
  var c=fcDeck.splice(fcIdx,1)[0];fcDeck.push(c);
  showFC();
}

/* ── STAFF READING ── */
var srMode='both',srAcc=false,srCur=null,srDone=false,srOk=0,srBad=0,srStr=0;

var TNOTES=[
  {n:'C',a:'',o:4,p:-2},{n:'D',a:'',o:4,p:-1},
  {n:'E',a:'',o:4,p:0},{n:'F',a:'',o:4,p:1},
  {n:'G',a:'',o:4,p:2},{n:'A',a:'',o:4,p:3},
  {n:'B',a:'',o:4,p:4},{n:'C',a:'',o:5,p:5},
  {n:'D',a:'',o:5,p:6},{n:'E',a:'',o:5,p:7},
  {n:'F',a:'',o:5,p:8},{n:'G',a:'',o:5,p:9},
  {n:'A',a:'',o:5,p:10},{n:'B',a:'',o:5,p:11},
  {n:'C',a:'',o:6,p:12},
  {n:'F',a:'#',o:4,p:1},{n:'C',a:'#',o:5,p:5},
  {n:'G',a:'#',o:4,p:2},{n:'B',a:'b',o:4,p:4},
  {n:'E',a:'b',o:5,p:7},{n:'A',a:'b',o:4,p:3},
];
var BNOTES=[
  {n:'G',a:'',o:1,p:0},{n:'A',a:'',o:1,p:1},
  {n:'B',a:'',o:1,p:2},{n:'C',a:'',o:2,p:3},
  {n:'D',a:'',o:2,p:4},{n:'E',a:'',o:2,p:5},
  {n:'F',a:'',o:2,p:6},{n:'G',a:'',o:2,p:7},
  {n:'A',a:'',o:2,p:8},{n:'B',a:'',o:2,p:9},
  {n:'C',a:'',o:3,p:10},{n:'D',a:'',o:3,p:11},
  {n:'E',a:'',o:3,p:12},
  {n:'B',a:'b',o:2,p:9},{n:'E',a:'b',o:2,p:5},
  {n:'F',a:'#',o:2,p:6},{n:'G',a:'#',o:2,p:7},
];

function drawStaff(note){
  var cv=document.getElementById('srCv');
  var cx=cv.getContext('2d');
  /* Hi-DPI fix */
  var dpr=window.devicePixelRatio||1;
  var rect=cv.getBoundingClientRect();
  cv.width=rect.width*dpr||460*dpr;
  cv.height=200*dpr;
  cv.style.width=(rect.width||460)+'px';
  cv.style.height='200px';
  cx.scale(dpr,dpr);
  var W=rect.width||460,H=200;
  cx.clearRect(0,0,W,H);
  cx.fillStyle='#fff';cx.fillRect(0,0,W,H);
  var isT=(note.clef==='treble');
  var top=H*.30,gap=H*.12,step=gap/2,bot=top+gap*4;
  var sl=58,sr2=W-18;
  /* staff lines */
  cx.strokeStyle='#222';cx.lineWidth=1.5;
  for(var i=0;i<5;i++){cx.beginPath();cx.moveTo(sl,top+i*gap);cx.lineTo(sr2,top+i*gap);cx.stroke();}
  /* clef */
  cx.fillStyle='#111';cx.textBaseline='alphabetic';
  if(isT){cx.font='bold '+(H*.52)+'px serif';cx.fillText('𝄞',sl-40,bot+gap*.15);}
  else{cx.font='bold '+(H*.32)+'px serif';cx.fillText('𝄢',sl-38,top+gap*2.1);}
  /* note position */
  var nx=W*.63,ny=bot-note.p*step,r=step*.83;
  /* ledger lines */
  cx.strokeStyle='#222';cx.lineWidth=1.5;
  if(note.p<0){for(var lp=0;lp>=note.p-(note.p%2===0?0:1);lp-=2){cx.beginPath();cx.moveTo(nx-18,bot-lp*step);cx.lineTo(nx+18,bot-lp*step);cx.stroke();}}
  if(note.p>10){for(var lp=12;lp<=note.p+(note.p%2===0?0:1);lp+=2){cx.beginPath();cx.moveTo(nx-18,bot-lp*step);cx.lineTo(nx+18,bot-lp*step);cx.stroke();}}
  /* note head using scale+arc for compat */
  cx.fillStyle='#111';cx.beginPath();
  cx.save();cx.translate(nx,ny);cx.scale(1.3,.85);cx.arc(0,0,r*1.1,0,Math.PI*2);cx.restore();cx.fill();
  /* stem */
  cx.strokeStyle='#111';cx.lineWidth=2;cx.beginPath();
  if(note.p<5){cx.moveTo(nx+r*1.12,ny);cx.lineTo(nx+r*1.12,ny-gap*3.5);}
  else{cx.moveTo(nx-r*1.12,ny);cx.lineTo(nx-r*1.12,ny+gap*3.5);}
  cx.stroke();
  /* accidental */
  if(note.a){
    cx.fillStyle='#111';cx.font='bold '+(gap*2)+'px serif';cx.textBaseline='middle';
    cx.fillText(note.a==='#'?'♯':'♭',nx-r*3.2,ny+(note.a==='b'?-step*.3:0));
  }
  /* clef label */
  cx.fillStyle='#aaa';cx.font='10px sans-serif';cx.textBaseline='top';
  cx.fillText(isT?'Treble':'Bass',sl,1);
}

var ENH={'C#':'Db','Db':'C#','D#':'Eb','Eb':'D#','F#':'Gb','Gb':'F#','G#':'Ab','Ab':'G#','A#':'Bb','Bb':'A#'};
var WNAMES=['C','D','E','F','G','A','B'];
var HASBLACK=[true,true,false,true,true,true,false];
var SHARPNAMES=['C#','D#','','F#','G#','A#',''];
var FLATNAMES=['','Db','Eb','','Gb','Ab','Bb'];

function buildSrKb(){
  var kb=document.getElementById('srKb');kb.innerHTML='';
  WNAMES.forEach(function(wn,wi){
    var w=document.createElement('div');w.className='sr-w';
    w.dataset.n=wn;w.dataset.a='';
    var lbl=document.createElement('div');lbl.className='sr-klbl';
    lbl.textContent=wn;w.appendChild(lbl);
    w.onclick=function(){srAnswer(this.dataset.n,'',this);};
    kb.appendChild(w);
    if(HASBLACK[wi]){
      var sn=SHARPNAMES[wi];
      if(sn){
        var b=document.createElement('div');b.className='sr-b';
        b.dataset.n=sn[0];b.dataset.a='#';
        var fn=FLATNAMES[(wi+1)%7]||'';
        b.dataset.fn=fn[0]||'';b.dataset.fa=fn.length>1?'b':'';
        var bl=document.createElement('div');bl.className='sr-blbl';
        bl.innerHTML=sn+'<br>'+fn;b.appendChild(bl);
        b.onclick=function(e){e.stopPropagation();srAnswerB(this);};
        w.style.position='relative';w.appendChild(b);
      }
    }
  });
}

function srAnswer(name,acc,el){
  if(srDone)return;srDone=true;
  var tgt=srCur.n+(srCur.a||'');
  var ok=(name+(acc||'')===tgt||(ENH[tgt]&&name+(acc||'')===ENH[tgt]));
  el.classList.add(ok?'ok':'bad');
  if(!ok)srHighlight();
  srFeedback(ok);
}

function srAnswerB(el){
  if(srDone)return;srDone=true;
  var sharp=el.dataset.n+'#';
  var flat=(el.dataset.fn||'')+(el.dataset.fa||'');
  var tgt=srCur.n+(srCur.a||'');
  var ok=(sharp===tgt||flat===tgt||(ENH[sharp]&&ENH[sharp]===tgt));
  el.classList.add(ok?'ok':'bad');
  if(!ok)srHighlight();
  srFeedback(ok);
}

function srHighlight(){
  var tgt=srCur.n+(srCur.a||'');
  document.querySelectorAll('#srKb [data-n]').forEach(function(k){
    var kn=k.dataset.n+(k.dataset.a||'');
    if(kn===tgt||(ENH[tgt]&&kn===ENH[tgt]))k.classList.add('ok');
  });
}

function srFeedback(ok){
  if(ok){srOk++;srStr++;}else{srBad++;srStr=0;}
  document.getElementById('srOkN')||void 0;
  /* update stats in the shared stat row */
  document.getElementById('fcGotN').textContent=srOk;
  document.getElementById('fcLeftN').textContent=srStr;
  document.getElementById('fcBadN').textContent=srBad;
  var name=srCur.n+(srCur.a==='#'?'♯':srCur.a==='b'?'♭':'');
  var fb=document.getElementById('srFb');
  fb.textContent=(ok?'Correct! ':'Wrong — ')+name;
  fb.style.color=ok?'#22c55e':'#ef4444';
  fb.style.background=ok?'rgba(34,197,94,.1)':'rgba(239,68,68,.1)';
}

function srNext(){
  srDone=false;
  document.getElementById('srFb').textContent='';
  document.getElementById('srFb').style.background='transparent';
  document.querySelectorAll('#srKb .sr-w').forEach(function(k){k.classList.remove('ok','bad');k.style.background='';});
  document.querySelectorAll('#srKb .sr-b').forEach(function(k){k.classList.remove('ok','bad');k.style.background='';});
  var pool=[];
  if(srMode==='treble'||srMode==='both')pool=pool.concat(TNOTES);
  if(srMode==='bass'||srMode==='both')pool=pool.concat(BNOTES);
  if(!srAcc)pool=pool.filter(function(n){return !n.a;});
  if(!pool.length)pool=TNOTES;
  var filtered=srCur?pool.filter(function(n){return n.n!==srCur.n||n.a!==srCur.a||n.o!==srCur.o;}):pool;
  srCur=(filtered.length?filtered:pool)[Math.floor(Math.random()*(filtered.length||pool.length))];
  srCur.clef=(srMode==='bass'||(srMode==='both'&&BNOTES.indexOf(srCur)>=0))?'bass':'treble';
  drawStaff(srCur);
}

function srSetClef(c,btn){
  srMode=c;
  document.querySelectorAll('#staffWrap .fc-deck-btn').forEach(function(b){
    if(b.id==='srBtnAcc')return;b.classList.remove('active');
  });
  if(btn)btn.classList.add('active');
  srNext();
}

function srToggleAcc(btn){
  srAcc=!srAcc;
  if(btn){btn.textContent='♯♭ '+(srAcc?'On':'Off');btn.classList.toggle('active',srAcc);}
  srNext();
}

var srKbBuilt=false;
loadDeck('all',document.getElementById('btn-all'));
</script>
"""

EXT_PIANO_CSS = """
.piano-wrap{overflow-x:auto;padding:16px 0}
.piano-keys{position:relative;display:flex;height:160px;user-select:none;min-width:560px}
.key-w{width:40px;height:140px;background:#fff;border:1px solid #aaa;border-radius:0 0 6px 6px;
  cursor:pointer;position:relative;flex-shrink:0;transition:background .05s;z-index:1}
.key-w:hover,.key-w.pressed{background:#c7d2fe}
.key-b{width:26px;height:88px;background:#1e2130;border:1px solid #475569;border-radius:0 0 4px 4px;
  cursor:pointer;position:absolute;top:0;z-index:2;transition:background .05s}
.key-b:hover,.key-b.pressed{background:#4f46e5}
.key-label{position:absolute;bottom:6px;left:50%;transform:translateX(-50%);
  font-size:.65rem;color:#94a3b8;pointer-events:none}
.piano-controls{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:14px}
.piano-controls label{font-size:.82rem;color:var(--text-muted);margin-bottom:0}
.piano-controls select{width:auto;margin-bottom:0}
.chord-highlight{display:flex;flex-wrap:wrap;gap:6px;margin-top:12px}
"""

EXT_PIANO_CONTENT = """
<div class="page-title">🎹 Piano Keyboard</div>
<p class="page-sub">Click keys to play, or use your computer keyboard (A=C, W=C#, S=D, E=D#, D=E, F=F…). Hold Shift for octave up.</p>
<div class="card">
  <div class="piano-wrap"><div class="piano-keys" id="pianoKeys"></div></div>
  <div class="piano-controls">
    <label>Octave</label>
    <select id="pianoOctave"><option value="3">Octave 3</option><option value="4" selected>Octave 4</option><option value="5">Octave 5</option></select>
    <label>Sound</label>
    <select id="pianoSound"><option value="piano">Piano</option><option value="organ">Organ</option><option value="bell">Bell</option></select>
    <label style="margin-left:8px">Volume</label>
    <input type="range" id="pianoVol" min="0" max="1" step="0.05" value="0.7" style="width:80px;accent-color:var(--accent);margin-bottom:0"/>
  </div>
  <div style="margin-top:14px">
    <div class="card-title">Quick Chord</div>
    <div class="chord-highlight" id="pianoChords"></div>
  </div>
</div>
<script>
(function(){
  var audioCtx=null,octave=4,sound='piano',vol=0.7;
  /* C D E F G A B + sharps for 2 octaves */
  var WHITE=['C','D','E','F','G','A','B'];
  var SEMIS={C:0,'C#':1,D:2,'D#':3,E:4,F:5,'F#':6,G:7,'G#':8,A:9,'A#':10,B:11};
  var KEY_MAP={'a':'C','w':'C#','s':'D','e':'D#','d':'E','f':'F','t':'F#','g':'G','y':'G#','h':'A','u':'A#','j':'B','k':'C'};
  var pressedKeys={};
  var QUICK_CHORDS=[{n:'Major',i:[0,4,7]},{n:'Minor',i:[0,3,7]},{n:'Dom7',i:[0,4,7,10]},{n:'Maj7',i:[0,4,7,11]},{n:'Minor7',i:[0,3,7,10]},{n:'Dim',i:[0,3,6]},{n:'Aug',i:[0,4,8]},{n:'Sus4',i:[0,5,7]}];

  function getCtx(){if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();if(audioCtx.state==='suspended')audioCtx.resume();return audioCtx;}
  function noteFreq(note,oct){return 261.63*Math.pow(2,((oct-4)*12+SEMIS[note])/12);}

  function playFreq(freq,dur){
    var ctx=getCtx(),now=ctx.currentTime;
    var master=ctx.createGain();master.connect(ctx.destination);
    master.gain.setValueAtTime(0,now);master.gain.linearRampToValueAtTime(vol,now+0.008);
    master.gain.exponentialRampToValueAtTime(vol*0.3,now+0.15);master.gain.setValueAtTime(vol*0.3,now+dur-0.15);master.gain.exponentialRampToValueAtTime(0.0001,now+dur);
    if(sound==='piano'){
      [{m:1,a:1},{m:2,a:.55},{m:3,a:.28},{m:4,a:.14}].forEach(function(h){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=freq*h.m;g.gain.value=h.a;g.gain.setValueAtTime(h.a,now);g.gain.exponentialRampToValueAtTime(h.a*(h.m===1?.7:.04),now+0.12*h.m*.55);o.connect(g);g.connect(master);o.start(now);o.stop(now+dur+0.1);});
    } else if(sound==='organ'){
      [1,2,3,4,6].forEach(function(m,i){var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=freq*m;g.gain.value=[0.8,0.4,0.3,0.2,0.1][i];o.connect(g);g.connect(master);o.start(now);o.stop(now+dur+0.1);});
    } else {/* bell */
      var o=ctx.createOscillator(),g=ctx.createGain();o.type='sine';o.frequency.value=freq*6;g.gain.setValueAtTime(vol*0.5,now);g.gain.exponentialRampToValueAtTime(0.0001,now+2);o.connect(g);g.connect(master);o.start(now);o.stop(now+2.1);
      var o2=ctx.createOscillator(),g2=ctx.createGain();o2.type='sine';o2.frequency.value=freq;g2.gain.setValueAtTime(vol*0.8,now);g2.gain.exponentialRampToValueAtTime(0.0001,now+1.5);o2.connect(g2);g2.connect(master);o2.start(now);o2.stop(now+1.6);
    }
  }

  function playNote(note,oct){playFreq(noteFreq(note,oct||octave),sound==='organ'?0.8:1.2);}

  function buildKeyboard(){
    var container=document.getElementById('pianoKeys');container.innerHTML='';
    var whites=[];var blackPos={};
    /* Two octaves */
    for(var o=octave;o<=octave+1;o++){
      WHITE.forEach(function(n){whites.push({n:n,o:o});});
    }
    whites.forEach(function(wk,wi){
      var k=document.createElement('div');k.className='key-w';k.dataset.note=wk.n;k.dataset.oct=wk.o;
      var lbl=document.createElement('div');lbl.className='key-label';lbl.textContent=wk.n+(wk.o);
      k.appendChild(lbl);container.appendChild(k);
      k.addEventListener('mousedown',function(){playNote(wk.n,wk.o);k.classList.add('pressed');});
      k.addEventListener('mouseup',function(){k.classList.remove('pressed');});
      k.addEventListener('mouseleave',function(){k.classList.remove('pressed');});
      /* Add black key after C,D,F,G,A */
      if(['C','D','F','G','A'].includes(wk.n)){
        var bname=wk.n+'#';
        var bk=document.createElement('div');bk.className='key-b';bk.dataset.note=bname;bk.dataset.oct=wk.o;
        bk.style.left=(wi*36+22)+'px';
        container.appendChild(bk);
        bk.addEventListener('mousedown',function(e){e.stopPropagation();playNote(bname,wk.o);bk.classList.add('pressed');});
        bk.addEventListener('mouseup',function(){bk.classList.remove('pressed');});
        bk.addEventListener('mouseleave',function(){bk.classList.remove('pressed');});
      }
    });
  }

  /* Computer keyboard */
  document.addEventListener('keydown',function(e){
    if(e.repeat||e.ctrlKey||e.metaKey)return;
    var k=e.key.toLowerCase(),note=KEY_MAP[k];
    if(note&&!pressedKeys[k]){
      pressedKeys[k]=true;
      var oct=octave+(e.shiftKey?1:0)+(k==='k'?1:0);
      playNote(note,oct);
      document.querySelectorAll('#pianoKeys .key-w,.key-b').forEach(function(el){
        if(el.dataset.note===note&&parseInt(el.dataset.oct)===oct)el.classList.add('pressed');
      });
    }
  });
  document.addEventListener('keyup',function(e){
    var k=e.key.toLowerCase();pressedKeys[k]=false;
    document.querySelectorAll('#pianoKeys .key-w,.key-b').forEach(function(el){el.classList.remove('pressed');});
  });

  /* Quick chords */
  var chordsEl=document.getElementById('pianoChords');
  QUICK_CHORDS.forEach(function(c){
    var btn=document.createElement('button');
    btn.style.cssText='padding:6px 14px;border:1px solid var(--border);border-radius:8px;background:var(--input-bg);color:var(--text-muted);font-size:.83rem;cursor:pointer;transition:all .15s';
    btn.textContent=c.n;btn.title='Play '+c.n+' chord';
    btn.addEventListener('click',function(){
      var ctx=getCtx(),now=ctx.currentTime;
      c.i.forEach(function(s,i){
        var semi=(octave-4)*12+s;
        var freq=261.63*Math.pow(2,semi/12);
        playFreq(freq,1.4);
      });
    });
    chordsEl.appendChild(btn);
  });

  document.getElementById('pianoOctave').addEventListener('change',function(){octave=parseInt(this.value);buildKeyboard();});
  document.getElementById('pianoSound').addEventListener('change',function(){sound=this.value;});
  document.getElementById('pianoVol').addEventListener('input',function(){vol=parseFloat(this.value);});
  buildKeyboard();
})();
</script>
"""

# ── Music Theory Quiz ─────────────────────────────────────────────────────────
EXT_QUIZ_CSS = """
.quiz-opt{width:100%;padding:12px 16px;background:var(--input-bg);border:1px solid var(--border);
  border-radius:10px;color:var(--text);font-size:.93rem;cursor:pointer;text-align:left;
  transition:all .15s;margin-bottom:8px}
.quiz-opt:hover{background:var(--hover-bg);border-color:var(--accent)}
.quiz-opt.correct{background:#14261f;border-color:#166534;color:#86efac}
.quiz-opt.wrong{background:#2d1b1b;border-color:#7f1d1d;color:#fca5a5}
.quiz-progress{height:6px;background:var(--border);border-radius:3px;margin-bottom:20px;overflow:hidden}
.quiz-progress-bar{height:100%;background:var(--accent);border-radius:3px;transition:width .3s}
"""

EXT_QUIZ_CONTENT = """
<div class="page-title">🧠 Music Theory Quiz</div>
<p class="page-sub">Test your knowledge of music theory fundamentals.</p>
<div class="card">
  <div style="display:flex;gap:20px;justify-content:center;margin-bottom:16px">
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="qScore">0</div><div style="font-size:.74rem;color:var(--text-faint)">SCORE</div></div>
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="qNum">1</div><div style="font-size:.74rem;color:var(--text-faint)">QUESTION</div></div>
    <div style="text-align:center"><div style="font-size:1.8rem;font-weight:800;color:var(--accent-text)" id="qStreak">0</div><div style="font-size:.74rem;color:var(--text-faint)">STREAK 🔥</div></div>
  </div>
  <div class="quiz-progress"><div class="quiz-progress-bar" id="qBar" style="width:0%"></div></div>
  <div id="qCat" style="font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;color:var(--text-xfaint);margin-bottom:6px"></div>
  <div id="qText" style="font-size:1.05rem;font-weight:600;color:var(--text);margin-bottom:18px;min-height:48px"></div>
  <div id="qOpts"></div>
  <div id="qFeedback" style="font-size:.9rem;font-weight:600;min-height:24px;margin-top:4px"></div>
</div>
<script>
(function(){
  var QUESTIONS=[
    /* Note names */
    {cat:'Note Names',q:'How many semitones are in an octave?',opts:['8','10','12','7'],a:'12'},
    {cat:'Note Names',q:'What note is enharmonically equivalent to C#?',opts:['Db','D','Cb','B#'],a:'Db'},
    {cat:'Note Names',q:'What is the 5th note of the C major scale?',opts:['F','G','A','E'],a:'G'},
    {cat:'Note Names',q:'Which note is a tritone above C?',opts:['F#','G','Bb','Ab'],a:'F#'},
    /* Key Signatures */
    {cat:'Key Signatures',q:'How many sharps does G major have?',opts:['0','1','2','3'],a:'1'},
    {cat:'Key Signatures',q:'What key has 4 flats?',opts:['Eb Major','Ab Major','Bb Major','Db Major'],a:'Ab Major'},
    {cat:'Key Signatures',q:'How many sharps does D major have?',opts:['1','2','3','4'],a:'2'},
    {cat:'Key Signatures',q:'What is the relative minor of F major?',opts:['D minor','A minor','G minor','B minor'],a:'D minor'},
    {cat:'Key Signatures',q:'How many flats does Bb major have?',opts:['1','2','3','4'],a:'2'},
    /* Intervals */
    {cat:'Intervals',q:'A perfect 5th spans how many semitones?',opts:['5','6','7','8'],a:'7'},
    {cat:'Intervals',q:'What interval is C to E?',opts:['Major 3rd','Minor 3rd','Perfect 4th','Major 2nd'],a:'Major 3rd'},
    {cat:'Intervals',q:'A minor 7th spans how many semitones?',opts:['9','10','11','12'],a:'10'},
    {cat:'Intervals',q:'What do we call an interval of 6 semitones?',opts:['Tritone','Perfect 5th','Augmented 4th','Both A and C'],a:'Both A and C'},
    /* Chords */
    {cat:'Chords',q:'What notes make up a C major triad?',opts:['C-E-G','C-Eb-G','C-E-G#','C-D-G'],a:'C-E-G'},
    {cat:'Chords',q:'A diminished triad has what intervals from root?',opts:['m3 + m3','M3 + m3','m3 + M3','M3 + M3'],a:'m3 + m3'},
    {cat:'Chords',q:'The V7 chord in C major is?',opts:['G7','F7','D7','Am7'],a:'G7'},
    {cat:'Chords',q:'What type of chord is C-E-G#?',opts:['Augmented','Major','Diminished','Suspended'],a:'Augmented'},
    /* Rhythm */
    {cat:'Rhythm',q:'How many eighth notes equal one quarter note?',opts:['1','2','3','4'],a:'2'},
    {cat:'Rhythm',q:'In 6/8 time, the basic beat is?',opts:['Quarter note','Dotted quarter','Half note','Eighth note'],a:'Dotted quarter'},
    {cat:'Rhythm',q:'A dotted half note gets how many beats in 4/4?',opts:['2','2.5','3','4'],a:'3'},
    /* Terminology */
    {cat:'Terminology',q:'What does "fortissimo" mean?',opts:['Very loud','Very soft','Gradually louder','Suddenly loud'],a:'Very loud'},
    {cat:'Terminology',q:'What does "D.C. al Fine" mean?',opts:['Go to the sign','Repeat from beginning to Fine','Play twice','Skip to coda'],a:'Repeat from beginning to Fine'},
    {cat:'Terminology',q:'What does "legato" mean?',opts:['Short and detached','Smooth and connected','Getting louder','Getting softer'],a:'Smooth and connected'},
    {cat:'Terminology',q:'What does "allegro" indicate?',opts:['Slow','Medium','Fast','Very fast'],a:'Fast'},
    {cat:'Terminology',q:'What is a fermata?',opts:['Hold the note longer','Play very loudly','A type of scale','A cadence'],a:'Hold the note longer'},
  ];

  var score=0,qNum=0,streak=0,answered=false,shuffled=[];

  function shuffle(a){return a.slice().sort(function(){return Math.random()-.5;});}

  function start(){shuffled=shuffle(QUESTIONS);qNum=0;score=0;streak=0;next();}

  function next(){
    if(qNum>=shuffled.length){qNum=0;shuffled=shuffle(QUESTIONS);}
    answered=false;
    var q=shuffled[qNum];
    document.getElementById('qCat').textContent=q.cat;
    document.getElementById('qText').textContent=q.q;
    document.getElementById('qFeedback').textContent='';
    document.getElementById('qNum').textContent=qNum+1;
    document.getElementById('qBar').style.width=Math.round((qNum/shuffled.length)*100)+'%';
    var opts=shuffle(q.opts);
    var el=document.getElementById('qOpts');el.innerHTML='';
    opts.forEach(function(o){
      var btn=document.createElement('button');btn.className='quiz-opt';btn.textContent=o;
      btn.addEventListener('click',function(){if(!answered)answer(o,btn,q);});
      el.appendChild(btn);
    });
  }

  function answer(chosen,btn,q){
    if(answered)return;answered=true;
    var ok=(chosen===q.a);
    btn.classList.add(ok?'correct':'wrong');
    if(!ok){document.querySelectorAll('.quiz-opt').forEach(function(b){if(b.textContent===q.a)b.classList.add('correct');});}
    if(ok){score+=10;streak++;}else streak=0;
    document.getElementById('qScore').textContent=score;
    document.getElementById('qStreak').textContent=streak;
    document.getElementById('qFeedback').textContent=ok?'✅ Correct!':'❌ Answer: '+q.a;
    document.getElementById('qFeedback').style.color=ok?'#22c55e':'#ef4444';
    qNum++;
    setTimeout(next,1500);
  }

  start();
})();
</script>
"""

# ── Tempo Converter ───────────────────────────────────────────────────────────
EXT_TEMPO_CONTENT = """
<div class="page-title">⚡ Tempo Converter</div>
<p class="page-sub">Convert BPM to note durations and find equivalent tempos across time signatures.</p>
<div class="card">
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:20px">
    <div>
      <label>BPM</label>
      <input type="number" id="tcBpm" value="120" min="1" max="400" style="margin-bottom:0"/>
    </div>
    <div>
      <label>Beat Unit</label>
      <select id="tcBeat" style="margin-bottom:0">
        <option value="1">Whole note</option>
        <option value="2">Half note</option>
        <option value="4" selected>Quarter note</option>
        <option value="8">Eighth note</option>
        <option value="16">Sixteenth note</option>
      </select>
    </div>
  </div>
  <div id="tcResult" style="margin-top:4px"></div>
</div>
<script>
(function(){
  function calc(){
    var bpm=parseFloat(document.getElementById('tcBpm').value)||120;
    var beat=parseFloat(document.getElementById('tcBeat').value)||4;
    /* Duration of one beat in ms */
    var beatMs=60000/bpm;
    /* All note durations */
    var notes=[
      {n:'Whole note',div:1},{n:'Dotted half',div:1.5},{n:'Half note',div:2},
      {n:'Dotted quarter',div:3},{n:'Quarter note',div:4},{n:'Dotted eighth',div:6},
      {n:'Eighth note',div:8},{n:'Dotted sixteenth',div:12},{n:'Sixteenth note',div:16},
      {n:'Triplet eighth',div:12/1},{n:'Thirty-second note',div:32},
    ];
    var html='<table style="width:100%;border-collapse:collapse;font-size:.88rem">';
    html+='<tr style="border-bottom:2px solid var(--border)"><th style="padding:8px 12px;text-align:left;color:var(--text-xfaint);font-size:.75rem;text-transform:uppercase">Note</th><th style="padding:8px 12px;text-align:right;color:var(--text-xfaint);font-size:.75rem;text-transform:uppercase">Duration</th><th style="padding:8px 12px;text-align:right;color:var(--text-xfaint);font-size:.75rem;text-transform:uppercase">Hz</th></tr>';
    notes.forEach(function(n){
      var ms=(beatMs*beat/n.div);
      var hz=ms>0?(1000/ms).toFixed(3):'-';
      html+='<tr style="border-bottom:1px solid var(--border)">'
        +'<td style="padding:8px 12px;color:var(--text)">'+n.n+'</td>'
        +'<td style="padding:8px 12px;text-align:right;color:var(--accent-text);font-weight:600">'+Math.round(ms)+' ms</td>'
        +'<td style="padding:8px 12px;text-align:right;color:var(--text-muted)">'+hz+' Hz</td>'
        +'</tr>';
    });
    html+='</table>';
    /* Equivalent tempos */
    html+='<div class="card-title" style="margin-top:20px">Equivalent Tempos</div>';
    html+='<div style="display:flex;flex-wrap:wrap;gap:8px">';
    [[1,'Whole'],[2,'Half'],[4,'Quarter'],[8,'Eighth'],[16,'Sixteenth']].forEach(function(nb){
      var equiv=bpm*(nb[0]/beat);
      if(equiv>=20&&equiv<=400){
        var active=(nb[0]===beat);
        html+='<div style="background:'+(active?'var(--accent)':'var(--input-bg)')+';border:1px solid '+(active?'var(--accent)':'var(--border)')+';border-radius:8px;padding:8px 14px;text-align:center">'
          +'<div style="font-size:1rem;font-weight:700;color:'+(active?'#fff':'var(--accent-text)')+'">'+Math.round(equiv*10)/10+'</div>'
          +'<div style="font-size:.72rem;color:'+(active?'rgba(255,255,255,.7)':'var(--text-faint)')+'">♩='+nb[1]+'</div></div>';
      }
    });
    html+='</div>';
    document.getElementById('tcResult').innerHTML=html;
  }
  document.getElementById('tcBpm').addEventListener('input',calc);
  document.getElementById('tcBeat').addEventListener('change',calc);
  calc();
})();
</script>
"""
