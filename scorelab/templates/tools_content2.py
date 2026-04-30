from scorelab.templates.shell import BASE_CSS, THEME_SCRIPT, EASTER_EGG_JS, SIDEBAR_JS, NAV_HTML, SIDEBAR_HTML, make_shell

METRONOME_CSS = """
.metro-display{text-align:center;padding:28px 0 20px}
.metro-bpm-row{display:flex;align-items:center;justify-content:center;gap:10px}
.metro-pm-btn{width:44px;height:44px;border-radius:50%;border:2px solid var(--border);
  background:var(--input-bg);color:var(--text);font-size:1.4rem;font-weight:700;
  cursor:pointer;transition:background .15s,border-color .15s,transform .08s;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;line-height:1}
.metro-pm-btn:hover{background:var(--hover-bg);border-color:var(--accent)}
.metro-pm-btn:active{transform:scale(.92)}
.metro-bpm-input{font-size:4.2rem;font-weight:800;color:var(--accent-text);line-height:1;
  background:transparent;border:none;outline:none;width:5ch;text-align:center;
  -moz-appearance:textfield;font-family:inherit}
.metro-bpm-input::-webkit-inner-spin-button,.metro-bpm-input::-webkit-outer-spin-button{-webkit-appearance:none}
.metro-bpm-input:focus{border-bottom:2px solid var(--accent)}
.metro-bpm-label{font-size:.85rem;color:var(--text-faint);margin-top:4px}
.metro-slider{width:100%;margin:16px 0;accent-color:var(--accent)}
.metro-beats{display:flex;justify-content:center;gap:14px;margin:20px 0}
.beat-dot{width:28px;height:28px;border-radius:50%;background:var(--border);
  transition:background .05s,transform .05s;flex-shrink:0}
.beat-dot.active{background:var(--accent);transform:scale(1.25)}
.beat-dot.accent{background:#22c55e;transform:scale(1.35)}
.metro-controls{display:flex;gap:10px;margin-top:18px}
.metro-btn{flex:1;padding:16px;font-size:1.05rem;font-weight:700;border:none;
  border-radius:12px;cursor:pointer;transition:background .15s,transform .05s}
.metro-btn:active{transform:scale(.97)}
.metro-start{background:var(--accent);color:#fff}
.metro-start:hover{background:var(--accent-h)}
.metro-stop{background:var(--input-bg);color:var(--text-muted);border:1px solid var(--border)}
.metro-stop:hover{background:var(--hover-bg)}
.metro-settings{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:18px}
.metro-setting label{display:block;font-size:.78rem;color:var(--text-xfaint);
  text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px}
.metro-setting select,.metro-setting input{margin-bottom:0}
.vol-row{display:flex;align-items:center;gap:10px;margin-top:14px}
.vol-row label{flex-shrink:0;font-size:.82rem;color:var(--text-muted);margin-bottom:0}
.vol-row input[type=range]{flex:1;margin-bottom:0;accent-color:var(--accent)}
/* Presets */
.preset-list{display:flex;flex-direction:column;gap:8px;margin-top:4px}
.preset-item{display:flex;align-items:center;gap:10px;padding:10px 14px;
  background:var(--input-bg);border:1px solid var(--border);border-radius:10px;
  transition:border-color .15s}
.preset-item:hover{border-color:var(--accent)}
.preset-info{flex:1;min-width:0}
.preset-name{font-size:.9rem;font-weight:600;color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.preset-meta{font-size:.76rem;color:var(--text-faint);margin-top:2px}
.preset-load{padding:5px 12px;font-size:.8rem;background:var(--accent);color:#fff;
  border:none;border-radius:6px;cursor:pointer;transition:background .15s;flex-shrink:0}
.preset-load:hover{background:var(--accent-h)}
.preset-del{padding:5px 10px;font-size:.8rem;background:transparent;color:var(--text-faint);
  border:1px solid var(--border);border-radius:6px;cursor:pointer;transition:background .15s;flex-shrink:0}
.preset-del:hover{background:#2d1b1b;color:#fca5a5;border-color:#7f1d1d}
.no-presets{color:var(--text-faint);font-size:.86rem;padding:12px 0;text-align:center}
.save-preset-row{display:flex;gap:8px;margin-top:12px}
.save-preset-row input{flex:1;margin-bottom:0}
.save-preset-row button{flex-shrink:0;width:auto;padding:10px 18px;margin-top:0}
"""

METRONOME_CONTENT = """
<div class="page-title">Metronome</div>
<p class="page-sub">A precise, audio-based metronome. Press T to tap tempo. The accent beat plays a higher tone.</p>
<div class="card">
  <div class="metro-display">
    <div class="metro-bpm-row">
      <button class="metro-pm-btn" id="bpmMinus" title="Decrease BPM">−</button>
      <input type="number" class="metro-bpm-input" id="bpmInput" value="120" min="20" max="300"/>
      <button class="metro-pm-btn" id="bpmPlus" title="Increase BPM">+</button>
    </div>
    <div class="metro-bpm-label">BPM</div>
  </div>
  <input type="range" class="metro-slider" id="bpmSlider" min="20" max="300" value="120"/>
  <div class="metro-beats" id="beatDots"></div>
  <div class="metro-controls">
    <button class="metro-btn metro-start" id="startBtn">▶ Start</button>
    <button class="metro-btn metro-stop" id="stopBtn" disabled>■ Stop</button>
    <button class="metro-btn" id="flashBtn" title="Flash on every beat — useful when playing piano" style="background:var(--input-bg);color:var(--text-muted);border:1px solid var(--border);font-size:.8rem;padding:10px 16px">⚡ Flash</button>
  </div>
  <!-- Full-screen flash overlay -->
  <div id="metroFlash" style="display:none;position:fixed;inset:0;z-index:9999;pointer-events:none;opacity:0;transition:opacity .05s"></div>
  <div class="metro-settings">
    <div class="metro-setting">
      <label>Time Signature</label>
      <select id="timeSig">
        <option value="2">2/4</option>
        <option value="3">3/4</option>
        <option value="4" selected>4/4</option>
        <option value="5">5/4</option>
        <option value="6">6/8</option>
        <option value="7">7/8</option>
      </select>
    </div>
    <div class="metro-setting">
      <label>Sound</label>
      <select id="soundType">
        <option value="click">Click</option>
        <option value="beep">Beep</option>
        <option value="wood">Wood block</option>
        <option value="rim">Rim shot</option>
        <option value="clave">Clave</option>
        <option value="cowbell">Cowbell 🐄</option>
        <option value="hihat">Hi-hat</option>
        <option value="soft">Soft mallet</option>
      </select>
    </div>
  </div>
  <div class="vol-row">
    <label>Volume</label>
    <input type="range" id="volSlider" min="0" max="1" step="0.05" value="1.0"/>
  </div>
</div>

<div class="card">
  <div class="card-title">Presets</div>
  <div class="preset-list" id="presetList"><div class="no-presets">No presets saved yet.</div></div>
  <div class="save-preset-row">
    <input type="text" id="presetNameInput" placeholder="Preset name (e.g. Allegro 4/4)" style="margin-bottom:0"/>
    <button class="btn btn-sm" id="savePresetBtn" style="white-space:nowrap">Save Current</button>
  </div>
</div>

<script>
(function(){
  var bpm=120, beats=4, currentBeat=0, isRunning=false;
  var audioCtx=null, nextNoteTime=0, timerID=null;
  var lookahead=25, scheduleAhead=0.12;
  var noteQueue=[], rafID=null;
  var vol=1.0, sound='click';

  var bpmInput=document.getElementById('bpmInput'),
      bpmSlider=document.getElementById('bpmSlider'),
      bpmMinus=document.getElementById('bpmMinus'),
      bpmPlus=document.getElementById('bpmPlus'),
      beatDots=document.getElementById('beatDots'),
      startBtn=document.getElementById('startBtn'),
      stopBtn=document.getElementById('stopBtn'),
      timeSigSel=document.getElementById('timeSig'),
      soundSel=document.getElementById('soundType'),
      volSlider=document.getElementById('volSlider'),
      presetList=document.getElementById('presetList'),
      presetNameInput=document.getElementById('presetNameInput'),
      savePresetBtn=document.getElementById('savePresetBtn');

  function buildDots(){
    beatDots.innerHTML='';
    for(var i=0;i<beats;i++){
      var d=document.createElement('div');d.className='beat-dot';beatDots.appendChild(d);
    }
  }
  buildDots();

  function clampBpm(v){return Math.min(300,Math.max(20,parseInt(v)||120));}

  function setBpm(v){
    bpm=clampBpm(v);
    bpmInput.value=bpm;
    bpmSlider.value=bpm;
  }

  /* Slider syncs instantly */
  bpmSlider.addEventListener('input',function(){setBpm(this.value);});

  /* Number input: only commit on blur or Enter, avoids glitch while typing */
  bpmInput.addEventListener('keydown',function(e){
    if(e.key==='Enter'){e.preventDefault();setBpm(this.value);this.blur();}
    if(e.key==='ArrowUp'){e.preventDefault();setBpm(bpm+1);}
    if(e.key==='ArrowDown'){e.preventDefault();setBpm(bpm-1);}
  });
  bpmInput.addEventListener('blur',function(){setBpm(this.value);});
  /* Prevent non-numeric besides backspace/arrows */
  bpmInput.addEventListener('keypress',function(e){
    if(!/[0-9]/.test(e.key))e.preventDefault();
  });

  /* +/- buttons with hold-to-repeat */
  function makePmBtn(el, delta){
    var iv=null,tv=null;
    function tick(){setBpm(bpm+delta);}
    el.addEventListener('mousedown',function(e){e.preventDefault();tick();tv=setTimeout(function(){iv=setInterval(tick,80);},400);});
    el.addEventListener('mouseup',function(){clearTimeout(tv);clearInterval(iv);});
    el.addEventListener('mouseleave',function(){clearTimeout(tv);clearInterval(iv);});
    el.addEventListener('touchstart',function(e){e.preventDefault();tick();tv=setTimeout(function(){iv=setInterval(tick,80);},400);},{passive:false});
    el.addEventListener('touchend',function(){clearTimeout(tv);clearInterval(iv);});
  }
  makePmBtn(bpmMinus,-1);
  makePmBtn(bpmPlus,1);

  timeSigSel.addEventListener('change',function(){beats=parseInt(this.value);buildDots();if(isRunning){stopMetro();startMetro();}});
  soundSel.addEventListener('change',function(){sound=this.value;});
  volSlider.addEventListener('input',function(){vol=parseFloat(this.value);});

  function scheduleNote(beatNum, time){
    var ctx=audioCtx;
    if(ctx.state==='suspended') ctx.resume();
    /* Compressor for loudness without clipping */
    var comp=ctx.createDynamicsCompressor();
    comp.threshold.value=-6;comp.knee.value=3;comp.ratio.value=4;
    comp.attack.value=0.001;comp.release.value=0.05;
    comp.connect(ctx.destination);
    var osc=ctx.createOscillator(), gain=ctx.createGain();
    osc.connect(gain); gain.connect(comp);
    var isAccent=(beatNum===0);

    switch(sound){
      case 'click':
        osc.type='square';
        osc.frequency.value=isAccent?1200:800;
        gain.gain.setValueAtTime(vol*1.4,time);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.04);
        break;
      case 'beep':
        osc.type='sine';
        osc.frequency.value=isAccent?880:440;
        gain.gain.setValueAtTime(vol*1.6,time);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.08);
        break;
      case 'wood':
        osc.type='triangle';
        osc.frequency.value=isAccent?300:220;
        gain.gain.setValueAtTime(vol*1.8,time);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.06);
        break;
      case 'rim':
        osc.type='sawtooth';
        osc.frequency.value=isAccent?900:600;
        gain.gain.setValueAtTime(vol*1.2,time);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.025);
        break;
      case 'clave':
        osc.type='sine';
        osc.frequency.value=isAccent?2400:1800;
        gain.gain.setValueAtTime(vol*1.5,time);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.03);
        break;
      case 'cowbell':
        osc.type='square';
        osc.frequency.value=isAccent?562:440;
        gain.gain.setValueAtTime(vol*1.4,time);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.18);
        break;
      case 'hihat':
        /* White noise via buffer */
        osc.disconnect();
        var buf=ctx.createBuffer(1,ctx.sampleRate*0.05,ctx.sampleRate);
        var d=buf.getChannelData(0);
        for(var i=0;i<d.length;i++)d[i]=(Math.random()*2-1);
        var src=ctx.createBufferSource();
        src.buffer=buf;
        var hgain=ctx.createGain();
        hgain.gain.setValueAtTime(vol*(isAccent?1.8:1.1),time);
        hgain.gain.exponentialRampToValueAtTime(0.0001,time+0.05);
        src.connect(hgain);hgain.connect(comp);
        src.start(time);src.stop(time+0.06);
        noteQueue.push({beat:beatNum,time:time});
        return;
      case 'soft':
        osc.type='sine';
        osc.frequency.value=isAccent?523:392;
        gain.gain.setValueAtTime(0,time);
        gain.gain.linearRampToValueAtTime(vol*1.5,time+0.01);
        gain.gain.exponentialRampToValueAtTime(0.0001,time+0.12);
        break;
    }
    osc.start(time); osc.stop(time+0.2);
    noteQueue.push({beat:beatNum,time:time});
  }

  function scheduler(){
    while(nextNoteTime < audioCtx.currentTime+scheduleAhead){
      scheduleNote(currentBeat,nextNoteTime);
      nextNoteTime += 60/bpm;
      currentBeat=(currentBeat+1)%beats;
    }
    timerID=setTimeout(scheduler,lookahead);
  }

  var flashEnabled=false;
  var flashEl=document.getElementById('metroFlash');
  var flashBtn=document.getElementById('flashBtn');
  flashBtn.addEventListener('click',function(){
    flashEnabled=!flashEnabled;
    flashBtn.style.background=flashEnabled?'var(--accent)':'var(--input-bg)';
    flashBtn.style.color=flashEnabled?'#fff':'var(--text-muted)';
    flashBtn.style.borderColor=flashEnabled?'var(--accent)':'var(--border)';
    flashEl.style.display=flashEnabled?'block':'none';
    if(!flashEnabled){flashEl.style.opacity='0';}
  });

  function doFlash(isAccent){
    if(!flashEnabled)return;
    flashEl.style.background=isAccent?'rgba(99,102,241,0.55)':'rgba(255,255,255,0.18)';
    flashEl.style.opacity='1';
    clearTimeout(flashEl._t);
    flashEl._t=setTimeout(function(){flashEl.style.opacity='0';},isAccent?120:80);
  }

  function visualizer(){
    var now=audioCtx?audioCtx.currentTime:0;
    while(noteQueue.length && noteQueue[0].time < now+0.02){
      var n=noteQueue.shift();
      var dots=beatDots.querySelectorAll('.beat-dot');
      dots.forEach(function(d,i){
        d.classList.remove('active','accent');
        if(i===n.beat){d.classList.add(n.beat===0?'accent':'active');}
      });
      doFlash(n.beat===0);
      setTimeout(function(idx){
        var d=beatDots.querySelectorAll('.beat-dot')[idx];
        if(d) d.classList.remove('active','accent');
      }.bind(null,n.beat), 200);
    }
    if(isRunning) rafID=requestAnimationFrame(visualizer);
  }

  function startMetro(){
    /* Resume existing ctx if suspended (handles browser autoplay policy) */
    if(!audioCtx) audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    if(audioCtx.state==='suspended') audioCtx.resume();
    /* Also resume any other audio contexts that may exist on the page */
    isRunning=true; currentBeat=0;
    nextNoteTime=audioCtx.currentTime+0.05;
    scheduler(); rafID=requestAnimationFrame(visualizer);
    startBtn.disabled=true; stopBtn.disabled=false;
    startBtn.textContent='▶ Running…';
  }

  function stopMetro(){
    isRunning=false;
    clearTimeout(timerID); cancelAnimationFrame(rafID);
    noteQueue=[];
    beatDots.querySelectorAll('.beat-dot').forEach(function(d){d.classList.remove('active','accent');});
    startBtn.disabled=false; stopBtn.disabled=true;
    startBtn.textContent='▶ Start';
  }

  startBtn.addEventListener('click',startMetro);
  stopBtn.addEventListener('click',stopMetro);

  /* T key tap tempo */
  var tapTimes=[];
  document.addEventListener('keydown',function(e){
    if((e.key==='t'||e.key==='T')&&!e.ctrlKey&&!e.metaKey&&document.activeElement!==bpmInput){
      var now=Date.now();
      tapTimes.push(now); if(tapTimes.length>8)tapTimes.shift();
      if(tapTimes.length>1){
        var diffs=[]; for(var i=1;i<tapTimes.length;i++) diffs.push(tapTimes[i]-tapTimes[i-1]);
        var avg=diffs.reduce(function(a,b){return a+b;},0)/diffs.length;
        setBpm(Math.round(60000/avg));
      }
    }
  });

  /* ── Presets ── */
  function loadPresets(){
    return JSON.parse(localStorage.getItem('metroPresets')||'[]');
  }
  function savePresets(arr){
    localStorage.setItem('metroPresets',JSON.stringify(arr));
  }
  function renderPresets(){
    var arr=loadPresets();
    if(!arr.length){presetList.innerHTML='<div class="no-presets">No presets saved yet.</div>';return;}
    presetList.innerHTML='';
    arr.forEach(function(p,idx){
      var item=document.createElement('div');item.className='preset-item';
      item.innerHTML='<div class="preset-info"><div class="preset-name">'+escHtml(p.name)+'</div>'
        +'<div class="preset-meta">'+p.bpm+' BPM · '+p.timeSig+'/4 · '+p.sound+'</div></div>'
        +'<button class="preset-load" data-idx="'+idx+'">Load</button>'
        +'<button class="preset-del" data-idx="'+idx+'">✕</button>';
      presetList.appendChild(item);
    });
    presetList.querySelectorAll('.preset-load').forEach(function(btn){
      btn.addEventListener('click',function(){
        var p=loadPresets()[parseInt(this.dataset.idx)];
        if(!p)return;
        setBpm(p.bpm);
        timeSigSel.value=String(p.timeSig);beats=p.timeSig;buildDots();
        soundSel.value=p.sound;sound=p.sound;
        if(isRunning){stopMetro();startMetro();}
      });
    });
    presetList.querySelectorAll('.preset-del').forEach(function(btn){
      btn.addEventListener('click',function(){
        var arr=loadPresets();arr.splice(parseInt(this.dataset.idx),1);
        savePresets(arr);renderPresets();
      });
    });
  }
  function escHtml(s){var d=document.createElement('div');d.textContent=s;return d.innerHTML;}

  savePresetBtn.addEventListener('click',function(){
    var name=presetNameInput.value.trim();
    if(!name){presetNameInput.focus();return;}
    var arr=loadPresets();
    arr.push({name:name,bpm:bpm,timeSig:beats,sound:sound});
    savePresets(arr);renderPresets();
    presetNameInput.value='';
  });

  renderPresets();
})();
</script>
"""

# ── Sheet Music Viewer (with audio playback + lazy render) ────────────────────
VIEWER_CSS = """
.viewer-drop{border:2px dashed var(--border);border-radius:12px;padding:38px 24px;
  text-align:center;cursor:pointer;position:relative;transition:border-color .2s,background .2s}
.viewer-drop.drag-over{border-color:var(--accent);background:var(--hover-bg)}
.viewer-drop input[type="file"]{position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%}
.viewer-drop .icon{font-size:2.2rem;margin-bottom:10px}
.osmd-wrap{background:var(--card);border:1px solid var(--border);border-radius:12px;
  padding:20px;margin-top:20px;min-height:300px;overflow:auto}
.osmd-container{background:#fff;border-radius:8px;padding:16px;min-height:200px;width:100%;
  box-sizing:border-box;position:relative}
.viewer-toolbar{display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap}
.viewer-toolbar label{font-size:.83rem;color:var(--text-muted)}
.viewer-toolbar input[type=range]{width:120px;accent-color:var(--accent);margin:0}
.viewer-toolbar span{font-size:.83rem;color:var(--text-faint);min-width:36px}
.viewer-filename{font-size:.88rem;color:var(--accent-text);font-weight:600}
.loading-sheet{text-align:center;padding:40px;color:var(--text-faint);font-size:.9rem}
.loading-sheet .spinner{width:30px;height:30px;border:3px solid var(--border);
  border-top-color:var(--accent);border-radius:50%;animation:spin .7s linear infinite;margin:0 auto 12px}
@keyframes spin{to{transform:rotate(360deg)}}
.playback-cursor{position:absolute;top:0;width:2px;background:rgba(99,102,241,.85);
  pointer-events:none;z-index:10;display:none;border-radius:1px;
  box-shadow:0 0 6px rgba(99,102,241,.5)}
.transport{display:flex;align-items:center;gap:10px;padding:12px 16px;
  background:var(--input-bg);border:1px solid var(--border);border-radius:10px;
  margin-top:14px;flex-wrap:wrap}
.t-btn{width:36px;height:36px;border-radius:50%;border:none;font-size:.9rem;
  cursor:pointer;transition:background .15s;flex-shrink:0;display:flex;align-items:center;justify-content:center}
.t-btn.play{background:var(--accent);color:#fff}
.t-btn.play:hover{background:var(--accent-h)}
.t-btn.play:disabled{background:var(--border);cursor:not-allowed;color:var(--text-faint)}
.t-btn.ctrl{background:var(--input-bg);color:var(--text-muted);border:1px solid var(--border)}
.t-btn.ctrl:hover{background:var(--hover-bg);color:var(--text)}
.t-progress{flex:1;min-width:80px;accent-color:var(--accent)}
.t-time{font-size:.78rem;color:var(--text-faint);white-space:nowrap;font-family:monospace;min-width:90px;text-align:center}
.t-vol{width:60px;accent-color:var(--accent)}
.t-label{font-size:.75rem;color:var(--text-faint);flex-shrink:0}
.t-status{font-size:.75rem;color:var(--text-faint);width:100%;padding-top:2px}
.mini-kb{display:flex;height:56px;margin-top:10px;background:var(--card);
  border:1px solid var(--border);border-radius:8px;overflow:hidden;align-items:flex-end;padding:0 4px}
.mk-inner{position:relative;display:flex;height:48px;flex:1}
.mk-w{flex:1;min-width:0;background:#fff;border:1px solid #ccc;border-radius:0 0 4px 4px;
  position:relative;transition:background .04s}
.mk-w.lit{background:#818cf8}
.mk-b{position:absolute;background:#1e2130;border:1px solid #475569;border-radius:0 0 3px 3px;
  width:55%;height:60%;top:0;left:55%;z-index:2;transition:background .04s}
.mk-b.lit{background:#6366f1}
"""

VIEWER_CONTENT = """
<div class="page-title">Sheet Music Viewer</div>
<p class="page-sub">Upload a MusicXML or .mxl file — see the score, hear it with a live cursor, and watch notes light up on the keyboard.</p>

<script src="https://cdn.jsdelivr.net/npm/opensheetmusicdisplay@1.8.8/build/opensheetmusicdisplay.min.js"></script>

<div class="card">
  <div class="viewer-drop" id="viewerDrop">
    <input type="file" id="viewerFile" accept=".xml,.musicxml,.mxl"/>
    <div class="icon">🎶</div>
    <p><strong>Click to upload</strong> or drag and drop</p>
    <p style="margin-top:4px;font-size:.8rem">Supports .xml, .musicxml, .mxl</p>
  </div>
</div>

<div id="viewerOutput" style="display:none">
  <div class="osmd-wrap">
    <div class="viewer-toolbar">
      <span class="viewer-filename" id="viewerFilename"></span>
      <div style="display:flex;align-items:center;gap:8px;margin-left:auto">
        <label>Zoom</label>
        <input type="range" id="zoomSlider" min="0.3" max="2.5" step="0.1" value="1.0"/>
        <span id="zoomVal">100%</span>
      </div>
      <button class="btn btn-sm" style="width:auto;padding:6px 14px;margin-top:0" id="dlSvgBtn">Download SVG</button>
    </div>
    <div class="osmd-container" id="osmdContainer">
      <div class="playback-cursor" id="pbCursor"></div>
    </div>
  </div>

  <!-- Transport -->
  <div class="transport">
    <button class="t-btn play" id="tPlay" disabled>▶</button>
    <button class="t-btn ctrl" id="tStop" disabled>■</button>
    <button class="t-btn ctrl" id="tRewind" title="Rewind">⏮</button>
    <input type="range" class="t-progress" id="tProgress" value="0" min="0" max="100" step="0.1"/>
    <span class="t-time" id="tTime">0:00 / 0:00</span>
    <span class="t-label">Vol</span>
    <input type="range" class="t-vol" id="tVol" min="0" max="1" step="0.05" value="0.7"/>
    <div class="t-status" id="tStatus">Load a score above, then press ▶ to play.</div>
  </div>

  <!-- Mini piano keyboard -->
  <div class="mini-kb" id="miniKb" style="display:none">
    <div class="mk-inner" id="mkInner"></div>
  </div>
</div>

<div id="viewerLoading" style="display:none" class="osmd-wrap">
  <div class="loading-sheet"><div class="spinner"></div>Rendering…</div>
</div>
<div id="viewerError" style="display:none" class="flash error"></div>

<script>
(function(){
  var fileInput=document.getElementById('viewerFile'),
      drop=document.getElementById('viewerDrop'),
      output=document.getElementById('viewerOutput'),
      loading=document.getElementById('viewerLoading'),
      errDiv=document.getElementById('viewerError'),
      container=document.getElementById('osmdContainer'),
      filenameEl=document.getElementById('viewerFilename'),
      zoomSlider=document.getElementById('zoomSlider'),
      zoomVal=document.getElementById('zoomVal'),
      dlBtn=document.getElementById('dlSvgBtn'),
      tPlay=document.getElementById('tPlay'),
      tStop=document.getElementById('tStop'),
      tRewind=document.getElementById('tRewind'),
      tProgress=document.getElementById('tProgress'),
      tTime=document.getElementById('tTime'),
      tVol=document.getElementById('tVol'),
      tStatus=document.getElementById('tStatus'),
      pbCursor=document.getElementById('pbCursor'),
      mkInner=document.getElementById('mkInner'),
      miniKb=document.getElementById('miniKb');

  var osmd=null,audioCtx=null;
  var isPlaying=false,playOffset=0,playStartTime=0;
  var noteEvents=[],totalDuration=0;
  var rafId=null,schedTimer=null,schedIdx=0;
  var masterGain=null;
  var LOOKAHEAD=0.3,SCHED_MS=80;

  /* ─ Zoom ─ */
  var zoomT=null;
  zoomSlider.addEventListener('input',function(){
    zoomVal.textContent=Math.round(this.value*100)+'%';
    clearTimeout(zoomT);zoomT=setTimeout(function(){
      if(osmd){osmd.zoom=parseFloat(zoomSlider.value);osmd.render();}
    },300);
  });

  /* ─ SVG Download ─ */
  dlBtn.addEventListener('click',function(){
    var svgs=container.querySelectorAll('svg');if(!svgs.length)return;
    var out='<svg xmlns="http://www.w3.org/2000/svg" style="background:#fff">',h=0;
    svgs.forEach(function(s){var sh=parseFloat(s.getAttribute('height')||0);out+='<g transform="translate(0,'+h+')">'+s.innerHTML+'</g>';h+=sh+10;});
    var a=document.createElement('a');a.href=URL.createObjectURL(new Blob([out+'</svg>'],{type:'image/svg+xml'}));
    a.download=(filenameEl.textContent||'sheet')+'.svg';a.click();
  });

  /* ─ File loading ─ */
  drop.addEventListener('dragover',function(e){e.preventDefault();drop.classList.add('drag-over');});
  drop.addEventListener('dragleave',function(){drop.classList.remove('drag-over');});
  drop.addEventListener('drop',function(e){e.preventDefault();drop.classList.remove('drag-over');var f=e.dataTransfer.files[0];if(f)loadFile(f);});
  fileInput.addEventListener('change',function(){if(this.files[0])loadFile(this.files[0]);});

  function loadFile(file){
    stopAudio();output.style.display='none';errDiv.style.display='none';loading.style.display='block';
    tPlay.disabled=true;tStop.disabled=true;
    filenameEl.textContent=file.name;
    var isMxl=file.name.toLowerCase().endsWith('.mxl');
    var r=new FileReader();
    r.onload=function(e){renderScore(e.target.result,isMxl);};
    r.onerror=function(){showError('Could not read file.');};
    if(isMxl)r.readAsArrayBuffer(file);else r.readAsText(file);
  }

  function renderScore(data,isMxl){
    container.innerHTML='';container.appendChild(pbCursor);
    noteEvents=[];
    if(typeof opensheetmusicdisplay==='undefined'){showError('OSMD failed to load — check internet connection.');return;}
    try{
      osmd=new opensheetmusicdisplay.OpenSheetMusicDisplay(container,{
        autoResize:false,drawTitle:true,drawSubtitle:true,
        drawComposer:true,drawLyricist:true,drawPartNames:true});
      osmd.load(data).then(function(){
        osmd.zoom=parseFloat(zoomSlider.value);
        osmd.render();
        loading.style.display='none';
        output.style.display='block';
        if(!isMxl){buildNoteEvents(data);}
        else{tStatus.textContent='.mxl playback not supported — use .xml for audio.';}
        buildMiniKb();
        tPlay.disabled=false;tStop.disabled=false;
      }).catch(function(e){showError('Parse error: '+(e.message||e));});
    }catch(e){showError('Render error: '+(e.message||e));}
  }

  /* ─ Parse MusicXML into note events ─ */
  function buildNoteEvents(xmlStr){
    try{
      var doc=new DOMParser().parseFromString(xmlStr,'application/xml');
      var SEMI={C:0,D:2,E:4,F:5,G:7,A:9,B:11};
      function midi(step,alter,oct){return(oct+1)*12+SEMI[step]+(Math.round(alter||0));}
      function freq(m){return 440*Math.pow(2,(m-69)/12);}
      var parts=doc.querySelectorAll('part');
      if(!parts.length){tStatus.textContent='No parts found.';return;}
      var part=parts[0],divisions=1,tempo=120,t=0;
      part.querySelectorAll('measure').forEach(function(m){
        var de=m.querySelector('divisions');if(de)divisions=parseInt(de.textContent)||1;
        var se=m.querySelector('sound[tempo]');if(se)tempo=parseFloat(se.getAttribute('tempo'))||tempo;
        var divSec=(60/tempo)/divisions;
        var chordBack=0;
        m.querySelectorAll('note').forEach(function(n){
          var isRest=!!n.querySelector('rest'),isChord=!!n.querySelector('chord');
          var durEl=n.querySelector('duration');
          var dur=durEl?parseInt(durEl.textContent)||divisions:divisions;
          var durSec=dur*divSec;
          var st=isChord?t-chordBack:t;
          if(!isRest){
            var stepEl=n.querySelector('pitch step'),octEl=n.querySelector('pitch octave'),altEl=n.querySelector('pitch alter');
            if(stepEl&&octEl){
              var mid=midi(stepEl.textContent,altEl?parseFloat(altEl.textContent):0,parseInt(octEl.textContent));
              noteEvents.push({time:Math.round(st*10000)/10000,dur:Math.max(0.06,durSec*0.9),freq:freq(mid),midi:mid});
            }
          }
          if(isChord)chordBack=durSec;else{t+=durSec;chordBack=0;}
        });
      });
      noteEvents.sort(function(a,b){return a.time-b.time;});
      totalDuration=t;
      tProgress.max=totalDuration||100;
      tStatus.textContent='Ready · '+noteEvents.length+' notes · '+fmtTime(totalDuration);
      miniKb.style.display='flex';
    }catch(e){tStatus.textContent='Audio parse error: '+e.message;}
  }

  /* ─ Audio ─ */
  function getCtx(){
    if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    if(audioCtx.state==='suspended')audioCtx.resume();
    return audioCtx;
  }
  function getMaster(){
    var ctx=getCtx();
    if(!masterGain||masterGain.context.state==='closed'){
      masterGain=ctx.createGain();masterGain.connect(ctx.destination);}
    masterGain.gain.value=parseFloat(tVol.value);return masterGain;
  }

  function playNote(ctx,freq,midi,startAt,durSec){
    var g=ctx.createGain(),end=startAt+durSec;
    g.connect(getMaster());
    g.gain.setValueAtTime(0,startAt);
    g.gain.linearRampToValueAtTime(0.5,startAt+0.006);
    g.gain.exponentialRampToValueAtTime(0.16,startAt+0.1);
    g.gain.setValueAtTime(0.16,Math.max(startAt+0.11,end-0.08));
    g.gain.exponentialRampToValueAtTime(0.0001,end);
    /* Harmonics */
    [[1,1],[2,.5],[3,.25],[4,.12],[5,.06]].forEach(function(h){
      var o=ctx.createOscillator(),hg=ctx.createGain();
      o.type='sine';o.frequency.value=freq*h[0];hg.gain.value=h[1];
      hg.gain.setValueAtTime(h[1],startAt);
      hg.gain.exponentialRampToValueAtTime(Math.max(0.0001,h[1]*(h[0]===1?.6:.025)),startAt+0.08*h[0]*.5);
      o.connect(hg);hg.connect(g);o.start(startAt);o.stop(end+0.05);
    });
    /* Key light */
    var delay=(startAt-ctx.currentTime)*1000;
    setTimeout(function(){
      litKey(midi,true);
      setTimeout(function(){litKey(midi,false);},Math.min(durSec*1000,600));
    },Math.max(0,delay));
  }

  /* Lookahead scheduler */
  function schedLoop(){
    if(!isPlaying)return;
    var ctx=getCtx(),now=ctx.currentTime,until=now+LOOKAHEAD;
    while(schedIdx<noteEvents.length&&playStartTime+noteEvents[schedIdx].time<=until){
      var ev=noteEvents[schedIdx];
      var at=playStartTime+ev.time;
      if(at>=now-0.01)playNote(ctx,ev.freq,ev.midi,Math.max(at,now+0.001),ev.dur);
      schedIdx++;
    }
    schedTimer=setTimeout(schedLoop,SCHED_MS);
  }

  function rafTick(){
    if(!isPlaying)return;
    var ctx=getCtx(),el=ctx.currentTime-playStartTime;
    if(el>=totalDuration){stopAudio();tProgress.value=0;tTime.textContent='0:00 / '+fmtTime(totalDuration);return;}
    tProgress.value=el;tTime.textContent=fmtTime(el)+' / '+fmtTime(totalDuration);
    updateCursor(el);
    rafId=requestAnimationFrame(rafTick);
  }

  function startAudio(offset){
    stopAudio();
    if(!noteEvents.length){tStatus.textContent='No audio data. Use .xml/.musicxml file.';return;}
    var ctx=getCtx();playOffset=offset||0;
    playStartTime=ctx.currentTime-playOffset;
    schedIdx=0;
    while(schedIdx<noteEvents.length&&noteEvents[schedIdx].time<playOffset-0.02)schedIdx++;
    isPlaying=true;tPlay.textContent='⏸';
    schedLoop();rafTick();
  }

  function stopAudio(){
    isPlaying=false;clearTimeout(schedTimer);cancelAnimationFrame(rafId);
    masterGain=null;tPlay.textContent='▶';
    pbCursor.style.display='none';
    document.querySelectorAll('.mk-w,.mk-b').forEach(function(k){k.classList.remove('lit');});
  }

  tPlay.addEventListener('click',function(){
    if(isPlaying){var ctx=getCtx();playOffset=ctx.currentTime-playStartTime;stopAudio();}
    else startAudio(playOffset);
  });
  tStop.addEventListener('click',function(){stopAudio();playOffset=0;tProgress.value=0;tTime.textContent='0:00 / '+fmtTime(totalDuration);});
  tRewind.addEventListener('click',function(){var was=isPlaying;stopAudio();playOffset=0;tProgress.value=0;tTime.textContent='0:00 / '+fmtTime(totalDuration);if(was)startAudio(0);});
  tProgress.addEventListener('input',function(){
    var was=isPlaying;if(was)stopAudio();
    playOffset=parseFloat(this.value);tTime.textContent=fmtTime(playOffset)+' / '+fmtTime(totalDuration);
    if(was)startAudio(playOffset);
  });
  tVol.addEventListener('input',function(){if(masterGain)masterGain.gain.value=parseFloat(this.value);});

  /* ─ Playback cursor ─ */
  /* Build a time→x map by sampling the score SVG */
  var cursorMap=[];
  function buildCursorMapFromSVG(){
    cursorMap=[];
    var svgs=container.querySelectorAll('svg');if(!svgs.length)return;
    /* Use note events + SVG width to estimate cursor position linearly */
    var svgEl=svgs[0];
    var svgW=svgEl.getBoundingClientRect().width||svgEl.viewBox.baseVal.width||800;
    var cRect=container.getBoundingClientRect();
    var svgLeft=svgEl.getBoundingClientRect().left-cRect.left;
    cursorMap={left:svgLeft,width:svgW,totalDuration:totalDuration};
  }
  function updateCursor(elapsed){
    if(!cursorMap.width||!cursorMap.totalDuration)return;
    var pct=Math.min(1,elapsed/cursorMap.totalDuration);
    var x=cursorMap.left+pct*cursorMap.width;
    pbCursor.style.left=x+'px';
    pbCursor.style.top='16px';
    pbCursor.style.height=(container.offsetHeight-32)+'px';
    pbCursor.style.display='block';
  }

  /* ─ Mini keyboard ─ */
  function buildMiniKb(){
    mkInner.innerHTML='';
    var WHITE=[0,2,4,5,7,9,11];var HAS_BLACK=[0,1,3,4,5];
    for(var oct=3;oct<=6;oct++){
      WHITE.forEach(function(s,wi){
        var midi=(oct+1)*12+s;
        var w=document.createElement('div');w.className='mk-w';w.dataset.midi=midi;
        mkInner.appendChild(w);
        if(HAS_BLACK.includes(wi)){
          var bk=document.createElement('div');bk.className='mk-b';bk.dataset.midi=midi+1;
          w.style.position='relative';w.appendChild(bk);
        }
      });
    }
  }
  function litKey(midi,on){
    document.querySelectorAll('[data-midi="'+midi+'"]').forEach(function(k){k.classList.toggle('lit',on);});
  }

  function fmtTime(s){if(!s||isNaN(s))return'0:00';return Math.floor(s/60)+':'+(Math.floor(s%60)<10?'0':'')+Math.floor(s%60);}
  function showError(msg){loading.style.display='none';output.style.display='none';errDiv.textContent=msg;errDiv.style.display='block';}

  /* Auto-build cursor map after render */
  var origRender=null;
})();
</script>
"""


INTERVAL_CSS = """
.int-question{text-align:center;padding:32px 20px}
.int-interval{font-size:3rem;font-weight:800;color:var(--accent-text);margin-bottom:8px}
.int-desc{font-size:1rem;color:var(--text-muted)}
.int-choices{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:24px}
.int-btn{padding:14px;background:var(--input-bg);border:1px solid var(--border);
  border-radius:10px;color:var(--text);font-size:.93rem;font-weight:500;cursor:pointer;
  transition:background .15s,border-color .15s,transform .08s}
.int-btn:hover{background:var(--hover-bg);border-color:var(--accent)}
.int-btn:active{transform:scale(.97)}
.int-btn.correct{background:#14261f;border-color:#166534;color:#86efac}
.int-btn.wrong{background:#2d1b1b;border-color:#7f1d1d;color:#fca5a5}
.int-score{display:flex;gap:20px;justify-content:center;margin-bottom:20px}
.int-stat{text-align:center}
.int-stat .val{font-size:1.8rem;font-weight:800;color:var(--accent-text)}
.int-stat .lbl{font-size:.75rem;color:var(--text-faint);text-transform:uppercase;letter-spacing:.06em}
.int-feedback{min-height:28px;text-align:center;font-size:.93rem;font-weight:600;margin-top:14px}
.int-piano{display:flex;justify-content:center;gap:2px;margin:20px 0;user-select:none}
.key-w{width:36px;height:100px;background:#fff;border:1px solid #ccc;border-radius:0 0 4px 4px;
  cursor:pointer;transition:background .1s;position:relative}
.key-w:hover{background:#e8e0ff}
.key-w.hl{background:#818cf8}
.key-b{width:24px;height:62px;background:#1e2130;border-radius:0 0 3px 3px;
  position:absolute;top:0;z-index:2;cursor:pointer;transition:background .1s;border:1px solid #475569}
.key-b:hover{background:#4f46e5}
.key-b.hl{background:#6366f1}
.piano-wrap{position:relative;display:flex}
"""

INTERVAL_CONTENT = """
<div class="page-title">Interval Trainer</div>
<p class="page-sub">Hear an interval played on a piano, then choose what it is. Click <strong>New Interval</strong> to start.</p>
<div class="card">
  <div class="int-score">
    <div class="int-stat"><div class="val" id="scoreCorrect">0</div><div class="lbl">Correct</div></div>
    <div class="int-stat"><div class="val" id="scoreWrong">0</div><div class="lbl">Wrong</div></div>
    <div class="int-stat"><div class="val" id="scoreStreak">0</div><div class="lbl">Streak 🔥</div></div>
  </div>
  <div class="int-question">
    <div class="int-interval" id="intDisplay">🎹</div>
    <div class="int-desc" id="intDescDisplay">Click "New Interval" to begin</div>
  </div>
  <div style="text-align:center;margin-bottom:16px;display:flex;gap:10px;justify-content:center">
    <button class="btn btn-sm" id="intNewBtn" style="width:auto;padding:10px 22px;display:inline-block;background:var(--accent)">New Interval</button>
    <button class="btn btn-sm" id="intPlayBtn" style="width:auto;padding:10px 22px;display:inline-block;background:var(--input-bg);border:1px solid var(--border);color:var(--text-muted)" disabled>▶ Replay</button>
  </div>
  <div class="int-choices" id="intChoices"></div>
  <div class="int-feedback" id="intFeedback"></div>
</div>
<script>
(function(){
  var INTERVALS=[
    {name:'Unison',semis:0,desc:'Same note played twice'},
    {name:'Minor 2nd',semis:1,desc:'Half step — very tense and dissonant'},
    {name:'Major 2nd',semis:2,desc:'Whole step — start of "Happy Birthday"'},
    {name:'Minor 3rd',semis:3,desc:'Minor sound — "Smoke on the Water" riff'},
    {name:'Major 3rd',semis:4,desc:'Bright and happy — "When the Saints Go Marching"'},
    {name:'Perfect 4th',semis:5,desc:'Strong and pure — "Here Comes the Bride"'},
    {name:'Tritone',semis:6,desc:'The devil\'s interval — most dissonant of all'},
    {name:'Perfect 5th',semis:7,desc:'Power chord — the "Star Wars" opening'},
    {name:'Minor 6th',semis:8,desc:'Bittersweet — "The Entertainer"'},
    {name:'Major 6th',semis:9,desc:'Warm and open — the NBC chime'},
    {name:'Minor 7th',semis:10,desc:'Bluesy dominant tension'},
    {name:'Major 7th',semis:11,desc:'Jazzy — just one half step from the octave'},
    {name:'Octave',semis:12,desc:'Same note, one octave higher — "Somewhere Over the Rainbow"'},
  ];

  var audioCtx=null;
  var correct=0,wrong=0,streak=0;
  var currentInterval=null,answered=false,hasQuestion=false;

  function getCtx(){
    if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    if(audioCtx.state==='suspended')audioCtx.resume();
    return audioCtx;
  }

  /* Piano-like note using additive synthesis */
  function pianoPianoNote(ctx,freq,startAt,durSec,vol){
    var harmonics=[
      {mult:1,amp:1.0},{mult:2,amp:0.6},{mult:3,amp:0.3},
      {mult:4,amp:0.15},{mult:5,amp:0.08},{mult:6,amp:0.04}];
    var master=ctx.createGain();
    master.connect(ctx.destination);
    var attack=0.005,decay=0.1,sus=0.3,rel=Math.min(durSec*0.35,0.7);
    var end=startAt+durSec;
    master.gain.setValueAtTime(0,startAt);
    master.gain.linearRampToValueAtTime(vol,startAt+attack);
    master.gain.exponentialRampToValueAtTime(vol*sus,startAt+attack+decay);
    master.gain.setValueAtTime(vol*sus,end-rel);
    master.gain.exponentialRampToValueAtTime(0.0001,end);
    harmonics.forEach(function(h){
      var osc=ctx.createOscillator(),g=ctx.createGain();
      osc.type='sine';osc.frequency.value=freq*h.mult;
      g.gain.value=h.amp;
      g.gain.setValueAtTime(h.amp,startAt);
      g.gain.exponentialRampToValueAtTime(h.amp*(h.mult===1?0.7:0.05),startAt+decay*h.mult*0.6);
      osc.connect(g);g.connect(master);
      osc.start(startAt);osc.stop(end+0.1);
    });
  }

  function playIntervalSound(semis){
    var ctx=getCtx();
    var baseFreq=261.63; /* C4 */
    var topFreq=baseFreq*Math.pow(2,semis/12);
    var now=ctx.currentTime;
    /* Play melodically (ascending) then harmonically */
    pianoPianoNote(ctx,baseFreq,now,0.8,0.45);
    pianoPianoNote(ctx,topFreq,now+0.65,0.8,0.45);
    /* Then together */
    pianoPianoNote(ctx,baseFreq,now+1.5,1.2,0.35);
    pianoPianoNote(ctx,topFreq,now+1.5,1.2,0.35);
  }

  function shuffle(arr){return arr.slice().sort(function(){return Math.random()-.5;});}

  function buildChoices(correctInterval){
    /* Pick 3 wrong answers — include nearby semitones to make it challenging */
    var pool=INTERVALS.filter(function(x){return x.name!==correctInterval.name;});
    var nearby=pool.filter(function(x){return Math.abs(x.semis-correctInterval.semis)<=3;});
    var far=pool.filter(function(x){return Math.abs(x.semis-correctInterval.semis)>3;});
    nearby=shuffle(nearby);far=shuffle(far);
    var wrong=(nearby.length>=2)?nearby.slice(0,2).concat(far.slice(0,1)):nearby.concat(far).slice(0,3);
    return shuffle([correctInterval].concat(wrong.slice(0,3)));
  }

  function newQuestion(){
    currentInterval=INTERVALS[Math.floor(Math.random()*INTERVALS.length)];
    answered=false;hasQuestion=true;
    document.getElementById('intDisplay').textContent='?';
    document.getElementById('intDescDisplay').textContent='Listen, then choose below…';
    document.getElementById('intFeedback').textContent='';
    document.getElementById('intPlayBtn').disabled=false;

    var choices=buildChoices(currentInterval);
    var el=document.getElementById('intChoices');
    el.innerHTML='';
    choices.forEach(function(c){
      var btn=document.createElement('button');
      btn.className='int-btn';btn.textContent=c.name;
      btn.addEventListener('click',function(){if(!answered)answer(c,btn);});
      el.appendChild(btn);
    });

    playIntervalSound(currentInterval.semis);
  }

  function answer(chosen,btn){
    if(answered||!hasQuestion)return;
    answered=true;
    var isCorrect=(chosen.name===currentInterval.name);
    if(isCorrect){
      correct++;streak++;
      document.getElementById('intFeedback').textContent='✅ Correct! '+currentInterval.desc;
    } else {
      wrong++;streak=0;
      document.getElementById('intFeedback').textContent='❌ It was: '+currentInterval.name+' — '+currentInterval.desc;
      document.getElementById('intChoices').querySelectorAll('.int-btn').forEach(function(b){
        if(b.textContent===currentInterval.name)b.classList.add('correct');
      });
    }
    btn.classList.add(isCorrect?'correct':'wrong');
    document.getElementById('scoreCorrect').textContent=correct;
    document.getElementById('scoreWrong').textContent=wrong;
    document.getElementById('scoreStreak').textContent=streak;
    document.getElementById('intDisplay').textContent=currentInterval.name;
    document.getElementById('intDescDisplay').textContent=currentInterval.desc;
  }

  document.getElementById('intNewBtn').addEventListener('click',function(){newQuestion();});
  document.getElementById('intPlayBtn').addEventListener('click',function(){
    if(currentInterval)playIntervalSound(currentInterval.semis);
  });
})();
</script>
"""

# ── Chord Reference (new tool) ────────────────────────────────────────────────
CHORD_CSS = """
.chord-search{display:flex;gap:10px;margin-bottom:20px}
.chord-search input{flex:1;margin-bottom:0}
.chord-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px}
.chord-card{background:var(--input-bg);border:1px solid var(--border);border-radius:12px;
  padding:16px;cursor:pointer;transition:border-color .15s,background .15s}
.chord-card:hover{border-color:var(--accent);background:var(--hover-bg)}
.chord-name{font-size:1.05rem;font-weight:700;color:var(--accent-text);margin-bottom:4px}
.chord-type{font-size:.78rem;color:var(--text-faint);text-transform:uppercase;letter-spacing:.06em;margin-bottom:8px}
.chord-notes{display:flex;flex-wrap:wrap;gap:5px}
.chord-note{background:var(--stat-bg);border:1px solid var(--border);border-radius:5px;
  padding:3px 8px;font-size:.8rem;color:var(--text-muted);font-family:monospace}
.chord-root-btns{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:18px}
.root-btn{padding:6px 12px;border:1px solid var(--border);border-radius:7px;
  background:transparent;color:var(--text-muted);font-size:.85rem;cursor:pointer;transition:all .15s}
.root-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.root-btn:hover:not(.active){background:var(--hover-bg);color:var(--text)}
.play-chord-btn{margin-top:10px;padding:5px 12px;font-size:.78rem;background:var(--accent);
  color:#fff;border:none;border-radius:6px;cursor:pointer;transition:background .15s;width:100%}
.play-chord-btn:hover{background:var(--accent-h)}
"""

CHORD_CONTENT = """
<div class="page-title">Chord Reference</div>
<p class="page-sub">Browse common chord types for any root note. Click a card to hear it.</p>
<div class="card">
  <div class="card-title">Root Note</div>
  <div class="chord-root-btns" id="rootBtns"></div>
  <div class="card-title" style="margin-top:4px">Filter</div>
  <input type="text" id="chordFilter" placeholder="Search chords (e.g. minor, 7th, dim…)" style="margin-bottom:18px"/>
  <div class="chord-grid" id="chordGrid"></div>
</div>
<script>
(function(){
  var ROOTS=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var CHORD_TYPES=[
    {name:'Major',type:'Major',intervals:[0,4,7]},
    {name:'Minor',type:'Minor',intervals:[0,3,7]},
    {name:'Dominant 7th',type:'7th',intervals:[0,4,7,10]},
    {name:'Major 7th',type:'Maj7',intervals:[0,4,7,11]},
    {name:'Minor 7th',type:'Min7',intervals:[0,3,7,10]},
    {name:'Diminished',type:'Dim',intervals:[0,3,6]},
    {name:'Augmented',type:'Aug',intervals:[0,4,8]},
    {name:'Sus2',type:'Sus',intervals:[0,2,7]},
    {name:'Sus4',type:'Sus',intervals:[0,5,7]},
    {name:'Add9',type:'Add',intervals:[0,4,7,14]},
    {name:'Minor Add9',type:'Add',intervals:[0,3,7,14]},
    {name:'Diminished 7th',type:'Dim7',intervals:[0,3,6,9]},
    {name:'Half-Dim 7th',type:'Dim7',intervals:[0,3,6,10]},
    {name:'Minor Major 7th',type:'Exotic',intervals:[0,3,7,11]},
    {name:'Dominant 9th',type:'9th',intervals:[0,4,7,10,14]},
    {name:'Major 9th',type:'9th',intervals:[0,4,7,11,14]},
    {name:'Minor 9th',type:'9th',intervals:[0,3,7,10,14]},
    {name:'Power Chord',type:'Power',intervals:[0,7]},
    {name:'6th',type:'6th',intervals:[0,4,7,9]},
    {name:'Minor 6th',type:'6th',intervals:[0,3,7,9]},
  ];
  var NOTE_NAMES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null;
  var selectedRoot='C',filterText='';

  function getCtx(){
    if(!audioCtx)audioCtx=new(window.AudioContext||window.webkitAudioContext)();
    if(audioCtx.state==='suspended')audioCtx.resume();
    return audioCtx;
  }
  function noteFreq(semitone){return 261.63*Math.pow(2,semitone/12);}

  /* Piano-like note using additive harmonics */
  function pianoNote(ctx,freq,startAt,durSec,vol){
    var harmonics=[
      {mult:1,amp:1.0},{mult:2,amp:0.55},{mult:3,amp:0.28},
      {mult:4,amp:0.14},{mult:5,amp:0.07},{mult:6,amp:0.035}];
    var master=ctx.createGain();
    master.connect(ctx.destination);
    var attack=0.004,decay=0.1,sus=0.32,rel=Math.min(durSec*0.35,0.6);
    var end=startAt+durSec;
    master.gain.setValueAtTime(0,startAt);
    master.gain.linearRampToValueAtTime(vol,startAt+attack);
    master.gain.exponentialRampToValueAtTime(vol*sus,startAt+attack+decay);
    master.gain.setValueAtTime(vol*sus,end-rel);
    master.gain.exponentialRampToValueAtTime(0.0001,end);
    harmonics.forEach(function(h){
      var osc=ctx.createOscillator(),g=ctx.createGain();
      osc.type='sine';osc.frequency.value=freq*h.mult;
      g.gain.value=h.amp;
      g.gain.setValueAtTime(h.amp,startAt);
      g.gain.exponentialRampToValueAtTime(h.amp*(h.mult===1?0.7:0.04),startAt+decay*h.mult*0.55);
      osc.connect(g);g.connect(master);
      osc.start(startAt);osc.stop(end+0.1);
    });
  }

  function playChordNotes(rootIdx,intervals){
    var ctx=getCtx();var now=ctx.currentTime;
    /* Slight arpeggiation (strum) for realism */
    intervals.forEach(function(semi,i){
      var freq=noteFreq(rootIdx+semi);
      pianoNote(ctx,freq,now+i*0.03,1.6,0.3);
    });
  }

  function getChordNotes(rootIdx,intervals){
    return intervals.map(function(semi){
      return NOTE_NAMES[(rootIdx+semi)%12];
    });
  }

  function buildRootBtns(){
    var el=document.getElementById('rootBtns');el.innerHTML='';
    ROOTS.forEach(function(r){
      var btn=document.createElement('button');
      btn.className='root-btn'+(r===selectedRoot?' active':'');
      btn.textContent=r;
      btn.addEventListener('click',function(){selectedRoot=r;buildRootBtns();renderChords();});
      el.appendChild(btn);
    });
  }

  function renderChords(){
    var rootIdx=ROOTS.indexOf(selectedRoot);
    var grid=document.getElementById('chordGrid');grid.innerHTML='';
    var filtered=CHORD_TYPES.filter(function(c){
      if(!filterText)return true;
      return c.name.toLowerCase().includes(filterText)||c.type.toLowerCase().includes(filterText);
    });
    filtered.forEach(function(c){
      var notes=getChordNotes(rootIdx,c.intervals);
      var card=document.createElement('div');card.className='chord-card';
      card.innerHTML='<div class="chord-name">'+selectedRoot+' '+c.name+'</div>'
        +'<div class="chord-type">'+c.type+'</div>'
        +'<div class="chord-notes">'+notes.map(function(n){return'<span class="chord-note">'+n+'</span>';}).join('')+'</div>'
        +'<button class="play-chord-btn">▶ Play</button>';
      card.querySelector('.play-chord-btn').addEventListener('click',function(e){
        e.stopPropagation();playChordNotes(rootIdx,c.intervals);});
      card.addEventListener('click',function(){playChordNotes(rootIdx,c.intervals);});
      grid.appendChild(card);
    });
    if(!filtered.length)grid.innerHTML='<div style="color:var(--text-faint);font-size:.9rem;padding:12px">No chords match your filter.</div>';
  }

  document.getElementById('chordFilter').addEventListener('input',function(){
    filterText=this.value.toLowerCase().trim();renderChords();});

  buildRootBtns();renderChords();
})();
</script>
"""

# ── Settings page ─────────────────────────────────────────────────────────────
SETTINGS_CSS = """
.theme-row{display:flex;align-items:center;justify-content:space-between;padding:4px 0}
.toggle-wrap{display:flex;gap:6px}
.theme-btn{padding:7px 16px;border-radius:8px;font-size:.86rem;font-weight:500;
  border:1px solid var(--border);cursor:pointer;transition:all .15s;
  background:transparent;color:var(--text-muted)}
.theme-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
.theme-btn:hover:not(.active){background:var(--hover-bg);color:var(--text)}
.setting-row{display:flex;align-items:center;justify-content:space-between;
  padding:14px 0;border-bottom:1px solid var(--border)}
.setting-row:last-child{border-bottom:none}
.setting-info .lbl{font-size:.93rem;color:var(--text);font-weight:500}
.setting-info .desc{font-size:.8rem;color:var(--text-faint);margin-top:3px}
.toggle-switch{position:relative;width:44px;height:24px;flex-shrink:0}
.toggle-switch input{opacity:0;width:0;height:0}
.toggle-slider{position:absolute;inset:0;background:var(--border);border-radius:24px;cursor:pointer;transition:background .2s}
.toggle-slider:before{content:'';position:absolute;height:18px;width:18px;left:3px;bottom:3px;
  background:#fff;border-radius:50%;transition:transform .2s}
.toggle-switch input:checked+.toggle-slider{background:var(--accent)}
.toggle-switch input:checked+.toggle-slider:before{transform:translateX(20px)}
"""

SETTINGS_CONTENT = """
<div class="page-title">Settings</div>
<p class="page-sub">Customize your experience.</p>

<div class="card">
  <div class="card-title">Appearance</div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Theme</div>
      <div class="desc">Choose how the app looks to you.</div>
    </div>
    <div class="toggle-wrap">
      <button class="theme-btn" id="btnLight" onclick="setTheme('light')">☀️ Light</button>
      <button class="theme-btn" id="btnDark"  onclick="setTheme('dark')">🌙 Dark</button>
    </div>
  </div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Animations</div>
      <div class="desc">Easter egg animations and transitions.</div>
    </div>
    <label class="toggle-switch">
      <input type="checkbox" id="toggleAnimations" checked/>
      <span class="toggle-slider"></span>
    </label>
  </div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Idle hints</div>
      <div class="desc">Show easter egg hints after 45 seconds of inactivity.</div>
    </div>
    <label class="toggle-switch">
      <input type="checkbox" id="toggleHints" checked/>
      <span class="toggle-slider"></span>
    </label>
  </div>
</div>

<div class="card">
  <div class="card-title">Sheet Music Viewer</div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Default zoom</div>
      <div class="desc">Starting zoom level for the sheet music viewer.</div>
    </div>
    <select id="defaultZoom" style="width:auto;margin-bottom:0;min-width:110px">
      <option value="0.6">60%</option>
      <option value="0.8">80%</option>
      <option value="1.0" selected>100%</option>
      <option value="1.2">120%</option>
      <option value="1.5">150%</option>
    </select>
  </div>
</div>

<div class="card">
  <div class="card-title">Metronome</div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Default BPM</div>
      <div class="desc">Starting BPM when you open the metronome.</div>
    </div>
    <input type="number" id="defaultBpm" min="20" max="300" value="120" style="width:90px;margin-bottom:0"/>
  </div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Default sound</div>
      <div class="desc">Which click sound to use by default.</div>
    </div>
    <select id="defaultSound" style="width:auto;margin-bottom:0;min-width:130px">
      <option value="click">Click</option>
      <option value="beep">Beep</option>
      <option value="wood">Wood block</option>
      <option value="rim">Rim shot</option>
      <option value="clave">Clave</option>
      <option value="cowbell">Cowbell 🐄</option>
      <option value="hihat">Hi-hat</option>
      <option value="soft">Soft mallet</option>
    </select>
  </div>
</div>

<div class="card" id="wakeLockCard">
  <div class="card-title">📱 Mobile</div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Keep screen awake</div>
      <div class="desc">Prevent your screen from turning off while using ScoreLab. Useful when reading sheet music or using the metronome.</div>
    </div>
    <label class="toggle-switch">
      <input type="checkbox" id="toggleWakeLock"/>
      <span class="toggle-slider"></span>
    </label>
  </div>
  <div id="wakeLockStatus" style="font-size:.78rem;color:var(--text-faint);margin-top:4px;display:none"></div>
</div>

<div class="card">
  <div class="card-title">About</div>
  <div style="font-size:.86rem;color:var(--text-faint);line-height:1.7">
    ScoreLab — a suite of browser-based music utilities.<br>
    There are <strong style="color:var(--accent-text)">7 easter eggs</strong> hidden in this app. How many can you find?<br>
    <br>
    <a href="/secret" style="color:var(--accent-text)">🔍 /secret</a> — You probably already know about this one.
  </div>
</div>

<div class="card">
  <div class="card-title" style="color:#ef4444">Danger Zone</div>
  <div class="setting-row">
    <div class="setting-info">
      <div class="lbl">Clear all local data</div>
      <div class="desc">Removes metronome presets and all local settings.</div>
    </div>
    <button class="btn secondary btn-sm" id="clearDataBtn" style="margin-top:0;color:#fca5a5;border-color:#7f1d1d">Clear</button>
  </div>
</div>

<script>
function setTheme(t){localStorage.setItem('theme',t);document.documentElement.setAttribute('data-theme',t);
  document.getElementById('btnLight').classList.toggle('active',t==='light');
  document.getElementById('btnDark').classList.toggle('active',t==='dark');}
(function(){
  var t=localStorage.getItem('theme')||'dark';
  document.getElementById('btnLight').classList.toggle('active',t==='light');
  document.getElementById('btnDark').classList.toggle('active',t==='dark');

  /* Load saved settings */
  var anim=localStorage.getItem('animationsEnabled');
  document.getElementById('toggleAnimations').checked=(anim!=='0');
  var hints=localStorage.getItem('hintsEnabled');
  document.getElementById('toggleHints').checked=(hints!=='0');
  var zoom=localStorage.getItem('defaultZoom')||'1.0';
  document.getElementById('defaultZoom').value=zoom;
  var bpm=localStorage.getItem('defaultMetroBpm')||'120';
  document.getElementById('defaultBpm').value=bpm;
  var snd=localStorage.getItem('defaultMetroSound')||'click';
  document.getElementById('defaultSound').value=snd;

  document.getElementById('toggleAnimations').addEventListener('change',function(){
    localStorage.setItem('animationsEnabled',this.checked?'1':'0');});
  document.getElementById('toggleHints').addEventListener('change',function(){
    localStorage.setItem('hintsEnabled',this.checked?'1':'0');});
  document.getElementById('defaultZoom').addEventListener('change',function(){
    localStorage.setItem('defaultZoom',this.value);});
  document.getElementById('defaultBpm').addEventListener('change',function(){
    localStorage.setItem('defaultMetroBpm',this.value);});
  document.getElementById('defaultSound').addEventListener('change',function(){
    localStorage.setItem('defaultMetroSound',this.value);});
  document.getElementById('clearDataBtn').addEventListener('click',function(){
    if(confirm('Clear all local settings and presets?')){
      ['theme','sidebar','metroPresets','animationsEnabled','hintsEnabled',
       'defaultZoom','defaultMetroBpm','defaultMetroSound','wakeLock'].forEach(function(k){
        localStorage.removeItem(k);});
      location.reload();}
  });

  /* Wake Lock */
  var wakeLockSentinel=null;
  var wakeLockEnabled=localStorage.getItem('wakeLock')==='1';
  var wlToggle=document.getElementById('toggleWakeLock');
  var wlStatus=document.getElementById('wakeLockStatus');

  if('wakeLock' in navigator){
    wlToggle.checked=wakeLockEnabled;
    wlStatus.style.display='block';
    if(wakeLockEnabled) requestWakeLock();
  } else {
    document.getElementById('wakeLockCard').style.display='none';
  }

  async function requestWakeLock(){
    try{
      wakeLockSentinel=await navigator.wakeLock.request('screen');
      wlStatus.textContent='✅ Screen will stay on';wlStatus.style.color='#22c55e';
      wakeLockSentinel.addEventListener('release',function(){
        wlStatus.textContent='Screen lock released (tab hidden)';wlStatus.style.color='var(--text-faint)';
      });
    } catch(e){
      wlStatus.textContent='Could not acquire wake lock: '+e.message;wlStatus.style.color='#ef4444';
    }
  }

  function releaseWakeLock(){
    if(wakeLockSentinel){wakeLockSentinel.release();wakeLockSentinel=null;}
    wlStatus.textContent='Screen can turn off normally';wlStatus.style.color='var(--text-faint)';
  }

  wlToggle.addEventListener('change',function(){
    localStorage.setItem('wakeLock',this.checked?'1':'0');
    if(this.checked)requestWakeLock();else releaseWakeLock();
  });

  /* Re-acquire wake lock when tab becomes visible again */
  document.addEventListener('visibilitychange',function(){
    if(document.visibilityState==='visible'&&localStorage.getItem('wakeLock')==='1'&&!wakeLockSentinel){
      requestWakeLock();
    }
  });
})();
</script>
"""

# ── Profile (without settings / theme) ───────────────────────────────────────
PROFILE_CSS = """
.banner-preview{width:100%;height:130px;border-radius:10px;overflow:hidden;margin-bottom:18px;
  position:relative;background:linear-gradient(135deg,#6366f1,#a855f7,#06b6d4)}
.banner-preview img{width:100%;height:100%;object-fit:cover;display:block}
.banner-placeholder{position:absolute;inset:0;display:flex;align-items:center;
  justify-content:center;color:rgba(255,255,255,.5);font-size:.83rem}
.avatar-row{display:flex;align-items:center;gap:18px;margin-bottom:18px}
.big-avatar{width:76px;height:76px;border-radius:50%;border:3px solid var(--border);
  display:flex;align-items:center;justify-content:center;background:var(--hover-bg);
  font-size:1.9rem;color:var(--accent-text);font-weight:700;flex-shrink:0;overflow:hidden}
.big-avatar img{width:100%;height:100%;object-fit:cover;display:block}
.back-link{display:inline-flex;align-items:center;gap:5px;color:var(--text-faint);
  font-size:.86rem;margin-bottom:22px}
.back-link:hover{color:var(--text-muted);text-decoration:none}
"""

PROFILE_CONTENT = """
<a class="back-link" href="/">← Back to tools</a>
<div class="page-title">Your Profile</div>
{% for msg,cat in messages %}<div class="flash {{cat}}">{{msg}}</div>{% endfor %}
<div class="card">
  <div class="card-title">Profile Banner</div>
  <div class="banner-preview">
    {% if banner_url %}<img src="{{ banner_url }}" alt="banner"/>
    {% else %}<div class="banner-placeholder">No banner — upload one below</div>{% endif %}
  </div>
  <form method="POST" action="/profile/banner" enctype="multipart/form-data">
    <label>Upload banner image</label>
    <input type="file" name="banner" accept="image/png,image/jpeg,image/gif,image/webp" required/>
    <button class="btn" type="submit">Save Banner</button>
  </form>
  {% if banner_url %}
  <form method="POST" action="/profile/banner/remove" style="margin-top:8px">
    <button class="btn secondary" type="submit">Remove Banner</button>
  </form>{% endif %}
</div>
<div class="card">
  <div class="card-title">Profile Picture</div>
  <div class="avatar-row">
    <div class="big-avatar">
      {% if avatar_url %}<img src="{{ avatar_url }}" alt="avatar"/>
      {% else %}{{ display_name[0].upper() }}{% endif %}
    </div>
    <div style="font-size:.84rem;color:var(--text-faint)">JPG, PNG, GIF or WebP · Max 5 MB</div>
  </div>
  <form method="POST" action="/profile/avatar" enctype="multipart/form-data">
    <label>Upload new picture</label>
    <input type="file" name="avatar" accept="image/png,image/jpeg,image/gif,image/webp" required/>
    <button class="btn" type="submit">Save Picture</button>
  </form>
</div>
<div class="card">
  <div class="card-title">Display Name</div>
  <form method="POST" action="/profile/display-name">
    <label>Display Name</label>
    <input type="text" name="display_name" value="{{ display_name }}" required/>
    <p class="hint">Not required to be unique.</p>
    <button class="btn" type="submit">Save</button>
  </form>
</div>
<div class="card">
  <div class="card-title">Username</div>
  <form method="POST" action="/profile/username">
    <label>Username</label>
    <input type="text" name="username" value="{{ username }}" required/>
    <p class="hint">Must be unique.</p>
    <button class="btn" type="submit">Save</button>
  </form>
</div>
<div class="card">
  <div class="card-title">Change Password</div>
  <form method="POST" action="/profile/password">
    <label>Current Password</label>
    <input type="password" name="current_password" required autocomplete="current-password"/>
    <label>New Password</label>
    <input type="password" name="new_password" required autocomplete="new-password"/>
    <p class="hint">Minimum 6 characters.</p>
    <label>Confirm New Password</label>
    <input type="password" name="confirm_password" required autocomplete="new-password"/>
    <button class="btn" type="submit">Change Password</button>
  </form>
</div>
<p style="font-size:.83rem;color:var(--text-faint);margin-top:8px">
  Looking for theme and app settings? <a href="/settings">Go to Settings →</a>
</p>
"""

SECRET_TEMPLATE = """<!DOCTYPE html><html lang="en"><head>
""" + THEME_SCRIPT + """
<meta charset="UTF-8"/><title>🤫 You found it</title>
<style>""" + BASE_CSS + """
body{align-items:center;justify-content:center;min-height:100vh;padding:20px}
.sc{background:var(--card);border:1px solid var(--border);border-radius:20px;
  padding:48px 40px;max-width:540px;width:100%;text-align:center;position:relative;overflow:hidden}
.sc::before{content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse at 50% 0%,rgba(99,102,241,.15),transparent 70%);pointer-events:none}
.badge{display:inline-block;background:#1e1b4b;border:1px solid #4338ca;color:#a5b4fc;
  border-radius:999px;padding:5px 16px;font-size:.78rem;font-weight:700;
  text-transform:uppercase;letter-spacing:.08em;margin-bottom:22px}
pre{font-family:"Courier New",monospace;font-size:.82rem;color:var(--accent-text);
  line-height:1.5;margin:20px 0;text-align:left;display:inline-block}
h1{font-size:1.75rem;font-weight:800;color:var(--text);margin-bottom:10px}
.fact{background:var(--input-bg);border:1px solid var(--border);border-radius:10px;
  padding:15px;font-size:.86rem;color:var(--text-muted);margin-top:18px;text-align:left;line-height:1.7}
.fact strong{color:var(--accent-text)}
.float{animation:fl 3s ease-in-out infinite}
@keyframes fl{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
</style></head><body>
<div class="sc">
  <div class="badge">🔍 Secret Found</div>
  <div class="float" style="font-size:3rem;margin-bottom:6px">𝄞</div>
  <h1>You found the secret page!</h1>
  <p style="color:var(--text-muted);margin-bottom:16px;line-height:1.7">
    Not many people make it here. Curiosity is how all great music is made.</p>
  <pre>
  𝄞 ── ── ── ──
  │  ♩  ♪  ♫  ♬
  │  G  E  D  C
  ────────────</pre>
  <div class="fact">
    <strong>🎵</strong> The treble clef 𝄞 is Unicode U+1D11E, added in 2001 — same year as Wikipedia.<br><br>
    <strong>🎹</strong> Pachelbel's Canon uses only 8 chords repeated 28 times. World's most recognised progression.<br><br>
    <strong>🕹️</strong> There are <em>7</em> Easter eggs in this app. You've found at least one. Can you find them all?<br><br>
    <strong>💡</strong> Hints: Konami Code, logo clicks, logo double-click, avatar clicks, typing "clef", typing "music", and… this page.
  </div>
  <a href="/" style="display:inline-block;margin-top:24px;padding:11px 26px;background:var(--accent);
    color:#fff;border-radius:10px;font-weight:600">← Back to the tools</a>
</div>
""" + EASTER_EGG_JS + """</body></html>"""

ERROR_404 = """<!DOCTYPE html><html lang="en"><head>
""" + THEME_SCRIPT + """
<meta charset="UTF-8"/><title>404 — Wrong Note</title>
<style>""" + BASE_CSS + """
body{align-items:center;justify-content:center;min-height:100vh;padding:20px}
.err{text-align:center;max-width:400px}
.big{font-size:5rem;animation:wob 2s ease-in-out infinite}
@keyframes wob{0%,100%{transform:rotate(-5deg)}50%{transform:rotate(5deg)}}
h1{font-size:1.9rem;font-weight:800;color:var(--text);margin-bottom:10px}
p{color:var(--text-muted);margin-bottom:22px;line-height:1.6}
</style></head><body>
<div class="err">
  <div class="big">𝄪</div>
  <h1>Wrong Note — 404</h1>
  <p>This page hit a rest. Every great composer makes mistakes.</p>
  <a href="/" style="display:inline-block;padding:11px 26px;background:var(--accent);
    color:#fff;border-radius:10px;font-weight:600">← Back to the score</a>
</div></body></html>"""

# ── Helpers ───────────────────────────────────────────────────────────────────



# ── Chromatic Tuner (built-in tool) ──────────────────────────────────────────
TUNER_CSS = """
.tuner-display{text-align:center;padding:24px 0 16px}
.tuner-note{font-size:5rem;font-weight:800;color:var(--accent-text);line-height:1;
  transition:color .1s}
.tuner-note.in-tune{color:#22c55e}
.tuner-note.close{color:#eab308}
.tuner-cents-wrap{position:relative;height:32px;background:var(--input-bg);
  border:1px solid var(--border);border-radius:16px;overflow:hidden;
  max-width:420px;margin:12px auto 4px}
.tuner-cents-center{position:absolute;left:50%;top:0;bottom:0;width:2px;
  background:var(--border);transform:translateX(-50%)}
.tuner-needle{position:absolute;top:4px;bottom:4px;width:4px;border-radius:2px;
  background:var(--accent);transform:translateX(-50%);transition:left .08s,background .1s;left:50%}
.tuner-needle.in-tune{background:#22c55e}
.tuner-needle.close{background:#eab308}
.tuner-needle.sharp{background:#ef4444}
.tuner-labels{display:flex;justify-content:space-between;max-width:420px;
  margin:0 auto 16px;font-size:.72rem;color:var(--text-xfaint)}
.tuner-octave{font-size:.95rem;color:var(--text-muted);margin-top:4px;min-height:24px}
.tuner-hz{font-size:.82rem;color:var(--text-faint);margin-top:2px;min-height:20px}
.tuner-cents-label{font-size:1.1rem;font-weight:700;min-height:28px;margin-top:8px}
.tuner-status{text-align:center;color:var(--text-faint);font-size:.88rem;margin-bottom:16px}
.tuner-controls{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin-bottom:16px}
.ref-row{display:flex;align-items:center;gap:10px;justify-content:center;margin-top:8px}
.ref-row label{font-size:.82rem;color:var(--text-muted);margin-bottom:0}
.ref-row input{width:90px;margin-bottom:0;text-align:center}
"""

TUNER_CONTENT = """
<div class="page-title">🎸 Chromatic Tuner</div>
<p class="page-sub">Play or sing any note — the tuner detects pitch in real time using your microphone.</p>
<div class="card">
  <div class="tuner-display">
    <div class="tuner-note" id="tNote">—</div>
    <div class="tuner-octave" id="tOctave"></div>
    <div class="tuner-hz" id="tHz"></div>
  </div>
  <div class="tuner-cents-wrap">
    <div class="tuner-cents-center"></div>
    <div class="tuner-needle" id="tNeedle"></div>
  </div>
  <div class="tuner-labels"><span>-50¢</span><span>-25¢</span><span>0</span><span>+25¢</span><span>+50¢</span></div>
  <div class="tuner-cents-label" id="tCents" style="text-align:center;min-height:28px"></div>
  <div class="tuner-status" id="tStatus">Click Start to begin listening</div>
  <div class="tuner-controls">
    <button class="btn btn-sm" id="tunerStartBtn" style="width:auto;padding:10px 28px">🎤 Start</button>
    <button class="btn btn-sm secondary" id="tunerStopBtn" style="width:auto;padding:10px 28px;margin-top:0" disabled>Stop</button>
  </div>
  <div class="ref-row">
    <label>Reference A4 (Hz)</label>
    <input type="number" id="tunerRef" value="440" min="400" max="480" step="0.5"/>
  </div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var audioCtx=null,analyser=null,stream=null,rafId=null,buf=null,running=false;

  function noteFromFreq(freq,a4){
    var n=12*Math.log2(freq/a4)+69;
    var midi=Math.round(n);var cents=Math.round((n-midi)*100);
    return{name:NOTES[((midi%12)+12)%12],octave:Math.floor(midi/12)-1,cents:cents,midi:midi};
  }

  function autoCorrelate(buf,sr){
    var N=buf.length,M=Math.floor(N/2),rms=0;
    for(var i=0;i<N;i++)rms+=buf[i]*buf[i];rms=Math.sqrt(rms/N);
    if(rms<0.008)return -1;
    var best=-1,bestC=-1,lastC=1,found=false;
    for(var o=2;o<M;o++){
      var c=0;for(var i=0;i<M;i++)c+=Math.abs(buf[i]-buf[i+o]);
      c=1-(c/M);
      if(c>0.9&&c>lastC){found=true;if(c>bestC){bestC=c;best=o;}}
      else if(found)break;lastC=c;
    }
    if(best<0||bestC<0.9)return -1;
    /* Interpolate */
    var y0=best>0?1-(function(o){var c=0;for(var i=0;i<M;i++)c+=Math.abs(buf[i]-buf[i+o]);return 1-c/M;})(best-1):0;
    var y1=bestC;
    var y2=best+1<M?1-(function(o){var c=0;for(var i=0;i<M;i++)c+=Math.abs(buf[i]-buf[i+o]);return 1-c/M;})(best+1):0;
    var shift=(y2-y0)/(2*(2*y1-y2-y0))||0;
    return sr/(best+shift);
  }

  function tick(){
    if(!running)return;
    analyser.getFloatTimeDomainData(buf);
    var a4=parseFloat(document.getElementById('tunerRef').value)||440;
    var freq=autoCorrelate(buf,audioCtx.sampleRate);
    var note=document.getElementById('tNote');
    var needle=document.getElementById('tNeedle');
    if(freq>50&&freq<4200){
      var n=noteFromFreq(freq,a4);
      note.textContent=n.name;
      document.getElementById('tOctave').textContent='Octave '+n.octave;
      document.getElementById('tHz').textContent=freq.toFixed(2)+' Hz';
      var pct=50+Math.max(-50,Math.min(50,n.cents));
      needle.style.left=pct+'%';
      var abs=Math.abs(n.cents);
      var cls=abs<=4?'in-tune':abs<=15?'close':'sharp';
      needle.className='tuner-needle '+cls;
      note.className='tuner-note '+(abs<=4?'in-tune':abs<=15?'close':'');
      var cl=document.getElementById('tCents');
      if(abs<=4){cl.textContent='✅ In tune!';cl.style.color='#22c55e';}
      else if(n.cents<0){cl.textContent='▲ Tune up '+abs+'¢';cl.style.color='#eab308';}
      else{cl.textContent='▼ Tune down '+abs+'¢';cl.style.color='#eab308';}
      document.getElementById('tStatus').textContent='Listening…';
    } else {
      note.textContent='—';note.className='tuner-note';
      document.getElementById('tOctave').textContent='';
      document.getElementById('tHz').textContent='';
      document.getElementById('tCents').textContent='';
    }
    rafId=requestAnimationFrame(tick);
  }

  document.getElementById('tunerStartBtn').addEventListener('click',function(){
    navigator.mediaDevices.getUserMedia({audio:{echoCancellation:false,noiseSuppression:false},video:false})
    .then(function(s){
      stream=s;audioCtx=new(window.AudioContext||window.webkitAudioContext)();
      analyser=audioCtx.createAnalyser();analyser.fftSize=4096;buf=new Float32Array(analyser.fftSize);
      audioCtx.createMediaStreamSource(s).connect(analyser);
      running=true;
      document.getElementById('tunerStartBtn').disabled=true;
      document.getElementById('tunerStopBtn').disabled=false;
      document.getElementById('tStatus').textContent='Listening…';
      tick();
    }).catch(function(e){document.getElementById('tStatus').textContent='Mic denied: '+e.message;});
  });
  document.getElementById('tunerStopBtn').addEventListener('click',function(){
    running=false;cancelAnimationFrame(rafId);
    if(stream)stream.getTracks().forEach(function(t){t.stop();});
    if(audioCtx)audioCtx.close();
    document.getElementById('tunerStartBtn').disabled=false;
    document.getElementById('tunerStopBtn').disabled=true;
    document.getElementById('tNote').textContent='—';
    document.getElementById('tNote').className='tuner-note';
    document.getElementById('tOctave').textContent='';
    document.getElementById('tHz').textContent='';
    document.getElementById('tCents').textContent='';
    document.getElementById('tStatus').textContent='Stopped';
  });
})();
</script>
"""

# ── Oscilloscope / Spectrum Analyzer ─────────────────────────────────────────
OSCOPE_CSS = """
.oscope-canvas{width:100%;border-radius:10px;background:#000;display:block}
.oscope-controls{display:flex;gap:12px;flex-wrap:wrap;margin-top:14px;align-items:center}
.oscope-controls label{font-size:.82rem;color:var(--text-muted);margin-bottom:0}
.oscope-controls select,.oscope-controls input[type=range]{width:auto;margin-bottom:0}
.oscope-stat{background:var(--input-bg);border:1px solid var(--border);border-radius:8px;
  padding:8px 14px;font-size:.82rem;color:var(--text-muted);text-align:center}
.oscope-stat span{display:block;font-size:1rem;font-weight:700;color:var(--accent-text)}
.oscope-stats{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}
"""

OSCOPE_CONTENT = """
<div class="page-title">📡 Oscilloscope</div>
<p class="page-sub">Real-time audio visualizer using your microphone. Switch between waveform, spectrum, and spectrogram views.</p>
<div class="card">
  <canvas class="oscope-canvas" id="oscopeCanvas" height="220"></canvas>
  <div class="oscope-stats">
    <div class="oscope-stat"><span id="osFreq">—</span>Frequency</div>
    <div class="oscope-stat"><span id="osRms">—</span>RMS Level</div>
    <div class="oscope-stat"><span id="osNote">—</span>Nearest Note</div>
  </div>
  <div class="oscope-controls">
    <label>Mode</label>
    <select id="osMode" style="min-width:140px">
      <option value="waveform">Waveform</option>
      <option value="spectrum">Spectrum</option>
      <option value="spectrogram">Spectrogram</option>
      <option value="lissajous">Lissajous</option>
    </select>
    <label>Color</label>
    <select id="osColor">
      <option value="indigo">Indigo</option>
      <option value="green">Green</option>
      <option value="amber">Amber</option>
      <option value="cyan">Cyan</option>
      <option value="white">White</option>
    </select>
    <label>Gain</label>
    <input type="range" id="osGain" min="1" max="20" value="4" style="width:90px"/>
    <button class="btn btn-sm" id="osStart" style="width:auto;padding:8px 20px">🎤 Start</button>
    <button class="btn btn-sm secondary" id="osStop" style="width:auto;padding:8px 20px;margin-top:0" disabled>Stop</button>
  </div>
</div>
<script>
(function(){
  var NOTES=['C','C#','D','D#','E','F','F#','G','G#','A','A#','B'];
  var COLORS={indigo:'#818cf8',green:'#22c55e',amber:'#f59e0b',cyan:'#06b6d4',white:'#ffffff'};
  var audioCtx=null,analyser=null,stream=null,rafId=null,running=false;
  var canvas=document.getElementById('oscopeCanvas'),ctx2=canvas.getContext('2d');
  var spectroData=[];/* for spectrogram */

  function resize(){canvas.width=canvas.parentElement.clientWidth||600;}
  resize();window.addEventListener('resize',function(){resize();spectroData=[];});

  function getColor(){return COLORS[document.getElementById('osColor').value]||'#818cf8';}
  function getGain(){return parseFloat(document.getElementById('osGain').value)||4;}

  function drawWaveform(buf){
    var W=canvas.width,H=canvas.height,col=getColor(),gain=getGain();
    ctx2.fillStyle='rgba(0,0,0,0.85)';ctx2.fillRect(0,0,W,H);
    ctx2.strokeStyle=col;ctx2.lineWidth=2;ctx2.shadowColor=col;ctx2.shadowBlur=4;
    ctx2.beginPath();
    for(var i=0;i<W;i++){
      var idx=Math.floor(i/W*buf.length);
      var v=buf[idx]*gain;
      var y=H/2-v*H/2;
      if(i===0)ctx2.moveTo(i,y);else ctx2.lineTo(i,y);
    }
    ctx2.stroke();ctx2.shadowBlur=0;
    /* Center line */
    ctx2.strokeStyle='rgba(255,255,255,0.08)';ctx2.lineWidth=1;
    ctx2.beginPath();ctx2.moveTo(0,H/2);ctx2.lineTo(W,H/2);ctx2.stroke();
  }

  function drawSpectrum(freq){
    var W=canvas.width,H=canvas.height,col=getColor(),gain=getGain();
    ctx2.fillStyle='rgba(0,0,0,0.85)';ctx2.fillRect(0,0,W,H);
    var bars=Math.min(freq.length,W/2);
    for(var i=0;i<bars;i++){
      var v=Math.max(0,(freq[i]+140)/140)*gain;
      var bh=Math.min(H,v*(H/2));
      var x=i/bars*W,bw=W/bars-0.5;
      var hue=i/bars*240;
      ctx2.fillStyle='hsl('+hue+',80%,60%)';
      ctx2.fillRect(x,H-bh,Math.max(1,bw),bh);
    }
    /* Grid */
    ctx2.strokeStyle='rgba(255,255,255,0.06)';ctx2.lineWidth=1;
    for(var db=-60;db<0;db+=20){
      var y=H+(db/140)*H*gain;
      ctx2.beginPath();ctx2.moveTo(0,y);ctx2.lineTo(W,y);ctx2.stroke();
    }
  }

  function drawSpectrogram(freq){
    var W=canvas.width,H=canvas.height;
    var col=new Uint8ClampedArray(W*4);
    var bars=Math.min(freq.length,W);
    for(var i=0;i<W;i++){
      var idx=Math.floor(i/W*bars);
      var v=Math.max(0,(freq[idx]+140)/140);
      var r=Math.round(v*255),g=Math.round(v*v*180),b=Math.round((1-v)*255);
      col[i*4]=r;col[i*4+1]=g;col[i*4+2]=b;col[i*4+3]=255;
    }
    spectroData.push(col);
    if(spectroData.length>H)spectroData.shift();
    var img=ctx2.createImageData(W,H);
    for(var row=0;row<spectroData.length;row++){
      var destRow=H-spectroData.length+row;
      img.data.set(spectroData[row],destRow*W*4);
    }
    ctx2.putImageData(img,0,0);
  }

  function drawLissajous(buf){
    var W=canvas.width,H=canvas.height,col=getColor(),gain=getGain();
    ctx2.fillStyle='rgba(0,0,0,0.6)';ctx2.fillRect(0,0,W,H);
    ctx2.strokeStyle=col;ctx2.lineWidth=1.5;ctx2.globalAlpha=0.7;
    ctx2.beginPath();
    var half=Math.floor(buf.length/2);
    for(var i=0;i<half;i++){
      var x=W/2+buf[i]*gain*W/2;
      var y=H/2+buf[i+half]*gain*H/2;
      if(i===0)ctx2.moveTo(x,y);else ctx2.lineTo(x,y);
    }
    ctx2.stroke();ctx2.globalAlpha=1;
  }

  function tick(){
    if(!running)return;
    var mode=document.getElementById('osMode').value;
    var W=canvas.width;
    if(mode==='waveform'||mode==='lissajous'){
      var tbuf=new Float32Array(analyser.fftSize);
      analyser.getFloatTimeDomainData(tbuf);
      var rms=0;for(var i=0;i<tbuf.length;i++)rms+=tbuf[i]*tbuf[i];rms=Math.sqrt(rms/tbuf.length);
      document.getElementById('osRms').textContent=(rms*100).toFixed(1)+'%';
      if(mode==='waveform')drawWaveform(tbuf);else drawLissajous(tbuf);
    }
    if(mode==='spectrum'||mode==='spectrogram'){
      var fbuf=new Float32Array(analyser.frequencyBinCount);
      analyser.getFloatFrequencyData(fbuf);
      /* Find peak */
      var peakIdx=0,peakVal=-Infinity;
      for(var i=1;i<fbuf.length;i++){if(fbuf[i]>peakVal){peakVal=fbuf[i];peakIdx=i;}}
      var freq=peakIdx*audioCtx.sampleRate/analyser.fftSize;
      if(freq>50&&freq<4000&&peakVal>-80){
        document.getElementById('osFreq').textContent=Math.round(freq)+' Hz';
        var midi=Math.round(69+12*Math.log2(freq/440));
        document.getElementById('osNote').textContent=NOTES[((midi%12)+12)%12]+(Math.floor(midi/12)-1);
      }
      if(mode==='spectrum')drawSpectrum(fbuf);else drawSpectrogram(fbuf);
    }
    rafId=requestAnimationFrame(tick);
  }

  document.getElementById('osStart').addEventListener('click',function(){
    navigator.mediaDevices.getUserMedia({audio:{echoCancellation:false,noiseSuppression:false},video:false})
    .then(function(s){
      stream=s;audioCtx=new(window.AudioContext||window.webkitAudioContext)();
      analyser=audioCtx.createAnalyser();analyser.fftSize=2048;
      audioCtx.createMediaStreamSource(s).connect(analyser);
      running=true;
      document.getElementById('osStart').disabled=true;
      document.getElementById('osStop').disabled=false;
      tick();
    }).catch(function(e){alert('Mic denied: '+e.message);});
  });
  document.getElementById('osStop').addEventListener('click',function(){
    running=false;cancelAnimationFrame(rafId);
    if(stream)stream.getTracks().forEach(function(t){t.stop();});
    if(audioCtx)audioCtx.close();
    document.getElementById('osStart').disabled=false;
    document.getElementById('osStop').disabled=true;
    ctx2.fillStyle='#000';ctx2.fillRect(0,0,canvas.width,canvas.height);
    spectroData=[];
  });
})();
</script>
"""

