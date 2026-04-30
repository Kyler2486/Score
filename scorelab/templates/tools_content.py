from scorelab.templates.shell import BASE_CSS, THEME_SCRIPT, EASTER_EGG_JS

AUTH_CSS = """
body{align-items:center;justify-content:center;min-height:100vh;padding:20px}
.auth-card{background:var(--card);border:1px solid var(--border);border-radius:16px;
  padding:36px;width:100%;max-width:420px}
.logo{text-align:center;margin-bottom:28px}
.logo h1{font-size:1.6rem;font-weight:700;color:var(--text)}
.logo p{color:var(--text-faint);font-size:.88rem;margin-top:6px}
.footer-link{text-align:center;margin-top:20px;font-size:.88rem;color:var(--text-faint)}
"""

AUTH_TEMPLATE = """<!DOCTYPE html><html lang="en"><head>
""" + THEME_SCRIPT + """
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>{{ title }} — ScoreLab</title>
<style>""" + BASE_CSS + AUTH_CSS + """</style></head><body>
<div class="auth-card">
  <div class="logo"><h1>🎵 ScoreLab</h1><p>{{ subtitle }}</p></div>
  {% for msg,cat in messages %}<div class="flash {{cat}}">{{msg}}</div>{% endfor %}
  <form method="POST">
    {% if show_register %}
      <label>Display Name</label>
      <input type="text" name="display_name" value="{{ form.display_name }}" required/>
      <p class="hint">Visible in the app — not required to be unique.</p>
      <label>Username</label>
      <input type="text" name="username" value="{{ form.username }}" required/>
      <p class="hint">Must be unique across all accounts.</p>
    {% endif %}
    <label>Email</label>
    <input type="email" name="email" value="{{ form.email }}" required autocomplete="email"/>
    <label>Password</label>
    <input type="password" name="password" required
      autocomplete="{{ 'new-password' if show_register else 'current-password' }}"/>
    {% if show_register %}
      <p class="hint" style="margin-top:-10px;margin-bottom:14px">Minimum 6 characters.</p>
    {% endif %}
    <button class="btn" type="submit">{{ btn }}</button>
  </form>
  <div class="footer-link">{{ footer_text|safe }}</div>
</div>
""" + EASTER_EGG_JS + """</body></html>"""

# ── Tool content templates ────────────────────────────────────────────────────

CONVERTER_CSS = """
.drop-zone{border:2px dashed var(--border);border-radius:12px;padding:44px 24px;
  text-align:center;cursor:pointer;transition:border-color .2s,background .2s;position:relative}
.drop-zone.drag-over{border-color:var(--accent);background:var(--hover-bg)}
.drop-zone input[type="file"]{position:absolute;inset:0;opacity:0;cursor:pointer;width:100%;height:100%}
.drop-zone .icon{font-size:2.2rem;margin-bottom:10px}
.drop-zone p{color:var(--text-muted);font-size:.93rem}
.drop-zone p strong{color:var(--accent-text)}
.file-name{margin-top:12px;font-size:.83rem;color:var(--text-faint);min-height:18px}
.convert-btn{display:block;width:100%;margin-top:18px;padding:13px;background:var(--accent);
  color:#fff;font-size:.95rem;font-weight:600;border:none;border-radius:10px;cursor:pointer;transition:background .2s}
.convert-btn:hover{background:var(--accent-h)}
.convert-btn:disabled{background:var(--border);cursor:not-allowed;color:var(--text-faint)}
.loading{display:none;text-align:center;margin-top:18px;color:var(--text-muted)}
.spinner{width:26px;height:26px;border:3px solid var(--border);border-top-color:var(--accent);
  border-radius:50%;animation:spin .7s linear infinite;margin:0 auto 10px}
@keyframes spin{to{transform:rotate(360deg)}}
.result-section{display:none;margin-top:24px}
.result-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}
.result-header h2{font-size:.95rem;font-weight:600;color:var(--text-muted)}
.action-btns{display:flex;gap:8px}
.action-btn{padding:5px 13px;font-size:.8rem;font-weight:500;border:1px solid var(--border);
  border-radius:7px;background:transparent;color:var(--text-muted);cursor:pointer;
  transition:background .15s,color .15s}
.action-btn:hover{background:var(--hover-bg);color:var(--text)}
.stats{display:flex;gap:12px;margin-bottom:12px;flex-wrap:wrap}
.stat{background:var(--stat-bg);border:1px solid var(--border);border-radius:8px;
  padding:7px 13px;font-size:.8rem;color:var(--text-muted)}
.stat span{color:var(--accent-text);font-weight:600}
.error-msg{display:none;margin-top:14px;padding:11px 15px;background:#2d1b1b;
  border:1px solid #7f1d1d;border-radius:8px;color:#fca5a5;font-size:.86rem}
.achieve{display:none;margin-top:12px;padding:12px 16px;border-radius:10px;
  font-size:.88rem;font-weight:600;text-align:center}
.achieve.gold{background:#422006;border:1px solid #92400e;color:#fde68a}
.achieve.piano{background:#1e1b4b;border:1px solid #4338ca;color:#c7d2fe}
"""

CONVERTER_CONTENT = """
<div class="page-title">MusicXML → Text</div>
<p class="page-sub">Upload a MusicXML file and get plain text to paste into any AI.</p>
<div class="card">
  <form id="uploadForm">
    <div class="drop-zone" id="dropZone">
      <input type="file" id="fileInput" accept=".xml,.musicxml"/>
      <div class="icon">📄</div>
      <p><strong>Click to upload</strong> or drag and drop</p>
      <p style="margin-top:4px;font-size:.8rem">Supports .xml and .musicxml</p>
    </div>
    <div class="file-name" id="fileName">No file selected</div>
    <button class="convert-btn" type="submit" id="convertBtn" disabled>Convert to Text</button>
  </form>
  <div class="loading" id="loading"><div class="spinner"></div><p>Parsing…</p></div>
  <div class="error-msg" id="errorMsg"></div>
  <div class="result-section" id="resultSection">
    <div class="result-header">
      <h2>Output</h2>
      <div class="action-btns">
        <button class="action-btn" id="copyBtn">Copy</button>
        <button class="action-btn" id="dlBtn">Download .txt</button>
      </div>
    </div>
    <div class="stats" id="stats"></div>
    <div class="achieve gold" id="achPachelbel">🎻 Pachelbel's Canon detected! A timeless classic.</div>
    <div class="achieve piano" id="achPiano">🎹 Exactly 88 notes — a full piano keyboard's worth!</div>
    <textarea id="outputText" readonly></textarea>
  </div>
</div>
<script>
const fi=document.getElementById('fileInput'),fn=document.getElementById('fileName'),
  cb=document.getElementById('convertBtn'),form=document.getElementById('uploadForm'),
  ld=document.getElementById('loading'),rs=document.getElementById('resultSection'),
  ot=document.getElementById('outputText'),em=document.getElementById('errorMsg'),
  st=document.getElementById('stats'),dz=document.getElementById('dropZone');
fi.addEventListener('change',()=>{const f=fi.files[0];if(f){fn.textContent=f.name;cb.disabled=false;}});
dz.addEventListener('dragover',e=>{e.preventDefault();dz.classList.add('drag-over');});
dz.addEventListener('dragleave',()=>dz.classList.remove('drag-over'));
dz.addEventListener('drop',e=>{e.preventDefault();dz.classList.remove('drag-over');
  const f=e.dataTransfer.files[0];if(f){fi.files=e.dataTransfer.files;fn.textContent=f.name;cb.disabled=false;}});
form.addEventListener('submit',async e=>{
  e.preventDefault();const f=fi.files[0];if(!f)return;
  ld.style.display='block';rs.style.display='none';em.style.display='none';cb.disabled=true;
  document.getElementById('achPachelbel').style.display='none';
  document.getElementById('achPiano').style.display='none';
  try{
    const fd=new FormData();fd.append('file',f);
    const res=await fetch('/convert',{method:'POST',body:fd}),
          data=await res.json();
    if(!res.ok||data.error){em.textContent=data.error||'Failed.';em.style.display='block';}
    else{
      ot.value=data.text;
      const lines=data.text.split('\\n'),m=lines.filter(l=>l.startsWith('Measure')).length,
            n=(data.text.match(/\\b[A-G][#b♮]?\\d/g)||[]).length;
      st.innerHTML=`<div class="stat">Measures:<span>${m}</span></div><div class="stat">Notes:<span>${n}</span></div><div class="stat">Lines:<span>${lines.length}</span></div>`;
      rs.style.display='block';document.getElementById('dlBtn').dataset.fn=f.name.replace(/\\.xml.*$/,'')+'.txt';
      if(f.name.toLowerCase().includes('pachelbel'))document.getElementById('achPachelbel').style.display='block';
      if(n===88)document.getElementById('achPiano').style.display='block';
    }
  }catch{em.textContent='Network error.';em.style.display='block';}
  ld.style.display='none';cb.disabled=false;
});
document.getElementById('copyBtn').addEventListener('click',()=>{
  navigator.clipboard.writeText(ot.value);
  const t=document.getElementById('toast');t.textContent='Copied!';t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),2000);});
document.getElementById('dlBtn').addEventListener('click',()=>{
  const blob=new Blob([ot.value],{type:'text/plain;charset=utf-8'}),url=URL.createObjectURL(blob),a=document.createElement('a');
  a.href=url;a.download=document.getElementById('dlBtn').dataset.fn||'output.txt';a.click();URL.revokeObjectURL(url);});
</script>"""

MXL_CONTENT = """
<div class="page-title">MXL → XML</div>
<p class="page-sub">Compressed .mxl files are ZIP archives containing MusicXML. This tool extracts the XML inside so you can open or edit it directly.</p>
<div class="card">
  <div class="card-title">Upload .mxl file</div>
  <form method="POST" enctype="multipart/form-data">
    <label>MXL File</label>
    <input type="file" name="file" accept=".mxl" required/>
    <button class="btn" type="submit">Extract XML</button>
  </form>
</div>
{% if error %}<div class="flash error">{{ error }}</div>{% endif %}
"""

META_CONTENT = """
<div class="page-title">Metadata Viewer</div>
<p class="page-sub">Extract the key information from a MusicXML file — title, composer, tempo, key, and more — without wading through all the notes.</p>
<div class="card">
  <form method="POST" enctype="multipart/form-data">
    <label>MusicXML File (.xml or .musicxml)</label>
    <input type="file" name="file" accept=".xml,.musicxml" required/>
    <button class="btn" type="submit">View Metadata</button>
  </form>
</div>
{% if error %}<div class="flash error">{{ error }}</div>{% endif %}
{% if meta %}
<div class="card">
  <div class="card-title">Score Information</div>
  <table style="width:100%;border-collapse:collapse;font-size:.9rem">
    {% set rows = [
      ('Title', meta.title),('Composer', meta.composer),
      ('Arranger', meta.arranger),('Lyricist', meta.lyricist),
      ('Copyright', meta.copyright),('Tempo', (meta.tempo ~ ' BPM') if meta.tempo else None),
      ('Time Signature', meta.time_sig),('Key', meta.key),('Total Measures', meta.measures),
    ] %}
    {% for label, val in rows %}{% if val %}
    <tr style="border-bottom:1px solid var(--border)">
      <td style="padding:10px 12px;color:var(--text-muted);width:140px;font-weight:600">{{ label }}</td>
      <td style="padding:10px 12px;color:var(--text)">{{ val }}</td>
    </tr>
    {% endif %}{% endfor %}
  </table>
</div>
{% if meta.parts %}
<div class="card">
  <div class="card-title">Parts / Instruments</div>
  <div style="display:flex;flex-wrap:wrap;gap:8px">
    {% for p in meta.parts %}
    <span style="background:var(--input-bg);border:1px solid var(--border);border-radius:6px;
      padding:5px 12px;font-size:.84rem;color:var(--text-muted)">{{ p }}</span>
    {% endfor %}
  </div>
</div>
{% endif %}
{% endif %}
"""

TRANSPOSE_CONTENT = """
<div class="page-title">Transpose</div>
<p class="page-sub">Shift all notes in a MusicXML file up or down by any number of semitones and download the result.</p>
<div class="card">
  <form method="POST" enctype="multipart/form-data">
    <label>MusicXML File (.xml or .musicxml)</label>
    <input type="file" name="file" accept=".xml,.musicxml" required/>
    <label>Semitones to transpose</label>
    <select name="semitones">
      {% for i in range(-12, 13) %}
        <option value="{{ i }}" {% if i==0 %}selected{% endif %}>
          {% if i > 0 %}+{{ i }} (up {{ i }} semitone{{ 's' if i!=1 }})
          {% elif i < 0 %}{{ i }} (down {{ -i }} semitone{{ 's' if i!=-1 }})
          {% else %}0 (no change){% endif %}
        </option>
      {% endfor %}
    </select>
    <button class="btn" type="submit">Transpose &amp; Download</button>
  </form>
</div>
{% if error %}<div class="flash error">{{ error }}</div>{% endif %}
<div class="card" style="font-size:.84rem;color:var(--text-faint)">
  <div class="card-title">How it works</div>
  Each note's pitch, octave, and accidental are recalculated. Key signatures are
  automatically updated. Positive values transpose up; negative values transpose down.
  Up uses sharps (C#, D#…), down uses flats (Db, Eb…).
</div>
"""

STATS_CSS = """
.bar-chart{margin-top:4px}
.bar-row{display:flex;align-items:center;gap:10px;margin-bottom:6px;font-size:.84rem}
.bar-label{width:36px;text-align:right;color:var(--text-muted);font-weight:600;flex-shrink:0}
.bar-track{flex:1;background:var(--input-bg);border-radius:4px;height:18px;overflow:hidden}
.bar-fill{height:100%;background:var(--accent);border-radius:4px;transition:width .4s}
.bar-count{width:36px;color:var(--text-faint);font-size:.78rem;flex-shrink:0}
.stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:4px}
.stat-box{background:var(--input-bg);border:1px solid var(--border);border-radius:10px;
  padding:14px 16px;text-align:center}
.stat-box .val{font-size:1.5rem;font-weight:700;color:var(--accent-text)}
.stat-box .lbl{font-size:.78rem;color:var(--text-faint);margin-top:3px}
"""

STATS_CONTENT = """
<div class="page-title">Note Statistics</div>
<p class="page-sub">Analyze note frequency, duration breakdown, and overall counts from any MusicXML file.</p>
<div class="card">
  <form method="POST" enctype="multipart/form-data">
    <label>MusicXML File (.xml or .musicxml)</label>
    <input type="file" name="file" accept=".xml,.musicxml" required/>
    <button class="btn" type="submit">Analyze</button>
  </form>
</div>
{% if error %}<div class="flash error">{{ error }}</div>{% endif %}
{% if stats %}
<div class="card">
  <div class="card-title">Summary</div>
  <div class="stat-grid">
    <div class="stat-box"><div class="val">{{ stats.total_notes }}</div><div class="lbl">Total Notes</div></div>
    <div class="stat-box"><div class="val">{{ stats.total_rests }}</div><div class="lbl">Rests</div></div>
    <div class="stat-box"><div class="val">{{ stats.total_chords }}</div><div class="lbl">Chord Notes</div></div>
    <div class="stat-box"><div class="val">{{ stats.note_counts.keys()|list|first if stats.note_counts else '—' }}</div><div class="lbl">Most Common</div></div>
  </div>
</div>
{% if stats.note_counts %}
<div class="card">
  <div class="card-title">Note Frequency</div>
  <div class="bar-chart">
    {% set max_count = stats.note_counts.values()|list|max %}
    {% for note, count in stats.note_counts.items() %}
    <div class="bar-row">
      <div class="bar-label">{{ note }}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{{ (count/max_count*100)|round|int }}%"></div></div>
      <div class="bar-count">{{ count }}</div>
    </div>
    {% endfor %}
  </div>
</div>
{% endif %}
{% if stats.dur_counts %}
<div class="card">
  <div class="card-title">Duration Breakdown</div>
  <div class="bar-chart">
    {% set max_d = stats.dur_counts.values()|list|max %}
    {% for dur, count in stats.dur_counts.items() %}
    <div class="bar-row">
      <div class="bar-label" style="width:64px;text-align:right">{{ dur }}</div>
      <div class="bar-track"><div class="bar-fill" style="width:{{ (count/max_d*100)|round|int }}%;background:#06b6d4"></div></div>
      <div class="bar-count">{{ count }}</div>
    </div>
    {% endfor %}
  </div>
</div>
{% endif %}
{% endif %}
"""

BPM_CSS = """
.tap-btn{width:100%;padding:60px 0;font-size:2rem;font-weight:800;background:var(--accent);
  color:#fff;border:none;border-radius:16px;cursor:pointer;transition:background .1s,transform .05s;
  letter-spacing:-.5px;user-select:none}
.tap-btn:active{background:var(--accent-h);transform:scale(.98)}
.bpm-display{text-align:center;margin:24px 0}
.bpm-num{font-size:4.5rem;font-weight:800;color:var(--accent-text);line-height:1}
.bpm-label{font-size:.9rem;color:var(--text-faint);margin-top:6px}
.tap-meta{display:flex;justify-content:center;gap:28px;margin-top:4px;font-size:.85rem;color:var(--text-faint)}
.tap-meta span span{color:var(--text-muted);font-weight:600}
"""

BPM_CONTENT = """
<div class="page-title">BPM Tapper</div>
<p class="page-sub">Tap the button (or press any key) to the beat. Your BPM will be calculated from the average interval between taps.</p>
<div class="card">
  <div class="bpm-display">
    <div class="bpm-num" id="bpmNum">—</div>
    <div class="bpm-label">Beats Per Minute</div>
  </div>
  <button class="tap-btn" id="tapBtn">TAP</button>
  <div class="tap-meta" style="margin-top:16px">
    <span>Taps: <span id="tapCount">0</span></span>
    <span>Interval: <span id="tapInterval">—</span> ms</span>
  </div>
  <button class="btn secondary btn-sm" id="resetBtn" style="margin-top:18px;max-width:160px;margin-left:auto;margin-right:auto;display:block">Reset</button>
</div>
<script>
var taps=[],last=null;
function tap(){
  var now=Date.now();
  if(last){taps.push(now-last);if(taps.length>8)taps.shift();}
  last=now;
  document.getElementById('tapCount').textContent=taps.length+1;
  if(taps.length){
    var avg=taps.reduce((a,b)=>a+b,0)/taps.length;
    var bpm=Math.round(60000/avg);
    document.getElementById('bpmNum').textContent=bpm;
    document.getElementById('tapInterval').textContent=Math.round(avg);
  }
}
document.getElementById('tapBtn').addEventListener('click',tap);
document.addEventListener('keydown',function(e){if(e.code==='Space'||e.code==='Enter'){e.preventDefault();tap();}});
document.getElementById('resetBtn').addEventListener('click',function(){
  taps=[];last=null;
  document.getElementById('bpmNum').textContent='—';
  document.getElementById('tapCount').textContent='0';
  document.getElementById('tapInterval').textContent='—';
});
</script>
"""

# ── Metronome (fixed BPM input + plus/minus + more sounds + presets) ──────────
