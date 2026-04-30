from flask import Blueprint, request, render_template_string
from flask_login import login_required
from scorelab.music_utils import analyze_form
from scorelab.templates.shell import make_shell, nav_ctx, ext_stub
from scorelab.templates.extensions_content import (
    EXT_SCALE_FINDER, EXT_CIRCLE_CSS, EXT_CIRCLE_CONTENT,
    EXT_TUNER_CONTENT, EXT_FREQ_CONTENT,
    EXT_PROGRESSION_CSS, EXT_PROGRESSION_CONTENT,
    EXT_NOTATION_CONTENT, EXT_RHYTHM_CSS, EXT_RHYTHM_CONTENT,
    EXT_EAR_CSS, EXT_EAR_CONTENT, EXT_TIMESIG_CONTENT,
    EXT_SOLFEGE_CONTENT, EXT_FORM_CONTENT,
    EXT_MIDI_CSS, EXT_MIDI_CONTENT,
    EXT_GUITAR_CONTENT, EXT_DRUM_CSS, EXT_DRUM_CONTENT,
    EXT_ARP_CONTENT, EXT_FLASH_CSS, EXT_FLASH_CONTENT,
    EXT_PIANO_CSS, EXT_PIANO_CONTENT,
    EXT_QUIZ_CSS, EXT_QUIZ_CONTENT, EXT_TEMPO_CONTENT,
)

ext_bp = Blueprint('ext', __name__)

@ext_bp.route("/ext/guitar-tuner")
@login_required
def ext_guitar_tuner():
    return make_shell(EXT_GUITAR_CONTENT, **nav_ctx())

@ext_bp.route("/ext/drum-machine")
@login_required
def ext_drum_machine():
    return make_shell(EXT_DRUM_CONTENT, extra_css=EXT_DRUM_CSS, **nav_ctx())

@ext_bp.route("/ext/arpeggiator")
@login_required
def ext_arpeggiator():
    return make_shell(EXT_ARP_CONTENT, **nav_ctx())

@ext_bp.route("/ext/music-flashcards")
@login_required
def ext_music_flashcards():
    return make_shell(EXT_FLASH_CONTENT, extra_css=EXT_FLASH_CSS, **nav_ctx())


# ── Note Reading Flashcards ───────────────────────────────────────────────────
EXT_NOTEREADING_CSS = """
.nr-card{background:var(--card);border:1px solid var(--border);border-radius:14px;
  padding:20px;margin-bottom:16px}
.nr-staff-wrap{background:#fff;border-radius:10px;padding:16px;display:flex;
  flex-direction:column;gap:20px;align-items:center}
.nr-clef-label{font-size:.72rem;font-weight:700;text-transform:uppercase;
  letter-spacing:.08em;color:var(--text-xfaint);margin-bottom:4px;text-align:center}
.nr-score{display:flex;gap:20px;justify-content:center;margin-bottom:12px}
.nr-stat .v{font-size:1.8rem;font-weight:800;color:var(--accent-text);text-align:center}
.nr-stat .l{font-size:.72rem;color:var(--text-faint);text-align:center;text-transform:uppercase}
/* Piano answer keyboard */
.nr-kb{position:relative;height:100px;display:flex;margin:0 auto;max-width:560px;
  background:#1a1a2e;border-radius:0 0 10px 10px;overflow:hidden;padding:4px 6px 0;
  border:1px solid var(--border);border-top:none}
.nr-kb-inner{position:relative;display:flex;height:92px;flex:1}
.nr-kw{flex:1 1 0;min-width:0;background:#fff;border:1px solid #ccc;border-radius:0 0 6px 6px;
  cursor:pointer;position:relative;transition:background .1s;display:flex;
  align-items:flex-end;justify-content:center;padding-bottom:4px}
.nr-kw:hover{background:#e0e7ff}
.nr-kw.correct{background:#86efac!important}
.nr-kw.wrong{background:#fca5a5!important}
.nr-kw.highlight{background:#c7d2fe}
.nr-kb-label{font-size:.55rem;color:#94a3b8;pointer-events:none;font-weight:600}
.nr-kb-label.sharp{font-size:.48rem}
.nr-kbl{position:absolute;background:#1e2130;border:1px solid #475569;border-radius:0 0 4px 4px;
  width:52%;height:56%;top:4px;left:61%;z-index:2;cursor:pointer;transition:background .1s;
  display:flex;align-items:flex-end;justify-content:center;padding-bottom:3px}
.nr-kbl:hover{background:#4f46e5}
.nr-kbl.correct{background:#166534!important}
.nr-kbl.wrong{background:#7f1d1d!important}
.nr-kbl.highlight{background:#4f46e5}
.nr-kbl-label{font-size:.5rem;color:#94a3b8;pointer-events:none;font-weight:600}
.nr-feedback{text-align:center;font-size:1rem;font-weight:700;min-height:32px;
  padding:6px;border-radius:8px;margin-top:8px;transition:all .2s}
.nr-controls{display:flex;gap:10px;justify-content:center;margin-bottom:16px;flex-wrap:wrap}
.nr-mode-btn{padding:7px 14px;border:1px solid var(--border);border-radius:8px;
  background:transparent;color:var(--text-muted);font-size:.83rem;cursor:pointer;transition:all .15s}
.nr-mode-btn.active{background:var(--accent);color:#fff;border-color:var(--accent)}
"""

EXT_NOTEREADING_CONTENT = """
<div class="page-title">🎼 Note Reading</div>
<p class="page-sub">A random note appears on the staff — click the correct key on the keyboard below. Includes ledger lines, sharps, and flats.</p>

<div class="nr-card">
  <div class="nr-controls">
    <button class="nr-mode-btn active" id="mBoth" onclick="setClef('both')">🎼 Both Clefs</button>
    <button class="nr-mode-btn" id="mTreble" onclick="setClef('treble')">𝄞 Treble Only</button>
    <button class="nr-mode-btn" id="mBass" onclick="setClef('bass')">𝄢 Bass Only</button>
    <button class="nr-mode-btn" id="mAccidentals" onclick="toggleAccidentals()">♯♭ Accidentals: OFF</button>
  </div>
  <div class="nr-score">
    <div class="nr-stat"><div class="v" id="nrCorrect">0</div><div class="l">Correct</div></div>
    <div class="nr-stat"><div class="v" id="nrStreak">0</div><div class="l">Streak 🔥</div></div>
    <div class="nr-stat"><div class="v" id="nrWrong">0</div><div class="l">Wrong</div></div>
  </div>

  <!-- Staff SVG rendered here -->
  <div class="nr-staff-wrap" id="nrStaffWrap">
    <canvas id="nrCanvas" width="480" height="160" style="max-width:100%;border-radius:6px"></canvas>
  </div>

  <div class="nr-feedback" id="nrFeedback"></div>

  <!-- Piano keyboard answer selector -->
  <div style="margin-top:10px">
    <div style="font-size:.78rem;color:var(--text-faint);text-align:center;margin-bottom:6px">Click the correct note on the keyboard</div>
    <div style="position:relative">
      <div style="background:var(--input-bg);border:1px solid var(--border);border-radius:10px 10px 0 0;
        padding:6px 12px;display:flex;justify-content:space-between;font-size:.72rem;color:var(--text-xfaint)">
        <span>C3</span><span>C4 (middle C)</span><span>C5</span>
      </div>
      <div class="nr-kb"><div class="nr-kb-inner" id="nrKbInner"></div></div>
    </div>
  </div>

  <div style="text-align:center;margin-top:14px">
    <button class="btn btn-sm" id="nrNext" style="width:auto;padding:10px 28px" onclick="nextNote()">Next Note →</button>
  </div>
</div>

<script>
(function(){
  /* ── Note data ──
     Each note has: name, octave, clef, staffPos (0=first ledger below, 1=space below staff,
     2=line 1, 3=space 1 ... 10=line 5, 11=space above, 12=first ledger above)
     staffPos for treble: 0=C4 ledger, 2=E4, 3=F4, 4=G4, 5=A4, 6=B4, 7=C5, 8=D5, 9=E5, 10=F5
  */
  var TREBLE_NOTES = [
    /* Ledger lines below */
    {name:'C',acc:'',oct:4,clef:'treble',pos:-2,ledger:[-1]},/* middle C */
    {name:'D',acc:'',oct:4,clef:'treble',pos:-1,ledger:[]},
    /* Staff */
    {name:'E',acc:'',oct:4,clef:'treble',pos:0,ledger:[]},
    {name:'F',acc:'',oct:4,clef:'treble',pos:1,ledger:[]},
    {name:'G',acc:'',oct:4,clef:'treble',pos:2,ledger:[]},
    {name:'A',acc:'',oct:4,clef:'treble',pos:3,ledger:[]},
    {name:'B',acc:'',oct:4,clef:'treble',pos:4,ledger:[]},
    {name:'C',acc:'',oct:5,clef:'treble',pos:5,ledger:[]},
    {name:'D',acc:'',oct:5,clef:'treble',pos:6,ledger:[]},
    {name:'E',acc:'',oct:5,clef:'treble',pos:7,ledger:[]},
    {name:'F',acc:'',oct:5,clef:'treble',pos:8,ledger:[]},
    {name:'G',acc:'',oct:5,clef:'treble',pos:9,ledger:[]},
    {name:'A',acc:'',oct:5,clef:'treble',pos:10,ledger:[]},
    {name:'B',acc:'',oct:5,clef:'treble',pos:11,ledger:[]},
    /* Ledger lines above */
    {name:'C',acc:'',oct:6,clef:'treble',pos:12,ledger:[12]},
    {name:'D',acc:'',oct:6,clef:'treble',pos:13,ledger:[12]},
    {name:'E',acc:'',oct:6,clef:'treble',pos:14,ledger:[12,14]},
    /* Accidentals */
    {name:'F',acc:'#',oct:4,clef:'treble',pos:1,ledger:[]},
    {name:'C',acc:'#',oct:5,clef:'treble',pos:5,ledger:[]},
    {name:'G',acc:'#',oct:4,clef:'treble',pos:2,ledger:[]},
    {name:'B',acc:'b',oct:4,clef:'treble',pos:4,ledger:[]},
    {name:'E',acc:'b',oct:5,clef:'treble',pos:7,ledger:[]},
    {name:'A',acc:'b',oct:4,clef:'treble',pos:3,ledger:[]},
    {name:'D',acc:'#',oct:5,clef:'treble',pos:6,ledger:[]},
  ];
  var BASS_NOTES = [
    /* Ledger lines above */
    {name:'E',acc:'',oct:3,clef:'bass',pos:12,ledger:[12]},
    {name:'D',acc:'',oct:3,clef:'bass',pos:11,ledger:[]},
    /* Staff */
    {name:'C',acc:'',oct:3,clef:'bass',pos:10,ledger:[]},
    {name:'B',acc:'',oct:2,clef:'bass',pos:9,ledger:[]},
    {name:'A',acc:'',oct:2,clef:'bass',pos:8,ledger:[]},
    {name:'G',acc:'',oct:2,clef:'bass',pos:7,ledger:[]},
    {name:'F',acc:'',oct:2,clef:'bass',pos:6,ledger:[]},
    {name:'E',acc:'',oct:2,clef:'bass',pos:5,ledger:[]},
    {name:'D',acc:'',oct:2,clef:'bass',pos:4,ledger:[]},
    {name:'C',acc:'',oct:2,clef:'bass',pos:3,ledger:[]},
    {name:'B',acc:'',oct:1,clef:'bass',pos:2,ledger:[]},
    {name:'A',acc:'',oct:1,clef:'bass',pos:1,ledger:[]},
    {name:'G',acc:'',oct:1,clef:'bass',pos:0,ledger:[]},
    /* Ledger lines below */
    {name:'F',acc:'',oct:1,clef:'bass',pos:-1,ledger:[]},
    {name:'E',acc:'',oct:1,clef:'bass',pos:-2,ledger:[-1]},
    /* Accidentals */
    {name:'B',acc:'b',oct:2,clef:'bass',pos:9,ledger:[]},
    {name:'E',acc:'b',oct:2,clef:'bass',pos:5,ledger:[]},
    {name:'F',acc:'#',oct:2,clef:'bass',pos:6,ledger:[]},
    {name:'A',acc:'b',oct:2,clef:'bass',pos:8,ledger:[]},
    {name:'C',acc:'#',oct:2,clef:'bass',pos:3,ledger:[]},
  ];

  var clefMode='both', useAccidentals=false;
  var current=null, answered=false, correct=0, wrong=0, streak=0;
  var canvas=document.getElementById('nrCanvas');
  var ctx2=canvas.getContext('2d');

  window.setClef=function(m){
    clefMode=m;
    ['mBoth','mTreble','mBass','mAccidentals'].forEach(function(id){
      document.getElementById(id).classList.remove('active');
    });
    document.getElementById(m==='both'?'mBoth':m==='treble'?'mTreble':'mBass').classList.add('active');
    if(useAccidentals) document.getElementById('mAccidentals').classList.add('active');
    nextNote();
  };
  window.toggleAccidentals=function(){
    useAccidentals=!useAccidentals;
    var btn=document.getElementById('mAccidentals');
    btn.textContent='♯♭ Accidentals: '+(useAccidentals?'ON':'OFF');
    btn.classList.toggle('active',useAccidentals);
    nextNote();
  };

  /* ── Draw staff ── */
  function drawStaff(note){
    var W=canvas.width,H=canvas.height;
    ctx2.clearRect(0,0,W,H);
    ctx2.fillStyle='#fff'; ctx2.fillRect(0,0,W,H);

    var isT=(note.clef==='treble');
    var staffTop=H*0.18, lineGap=H*0.13;
    var staffLeft=80,staffRight=W-40;

    /* Staff lines */
    ctx2.strokeStyle='#333';ctx2.lineWidth=1.5;
    for(var i=0;i<5;i++){
      var y=staffTop+i*lineGap;
      ctx2.beginPath();ctx2.moveTo(staffLeft,y);ctx2.lineTo(staffRight,y);ctx2.stroke();
    }

    /* Clef symbol */
    ctx2.fillStyle='#222';ctx2.font='bold '+(H*0.8)+'px serif';
    ctx2.textBaseline='alphabetic';
    if(isT){
      ctx2.font='bold '+(H*0.95)+'px serif';
      ctx2.fillText('𝄞',staffLeft-60,staffTop+lineGap*4.2);
    } else {
      ctx2.font='bold '+(H*0.55)+'px serif';
      ctx2.fillText('𝄢',staffLeft-58,staffTop+lineGap*2.1);
    }

    /* Note position: pos 0=line1(bottom), 1=space1, 2=line2... */
    /* Bottom line = pos 0, each step = lineGap/2 */
    var bottomLine=staffTop+lineGap*4;
    var step=lineGap/2;
    var noteX=W*0.62;
    var noteY=bottomLine - note.pos*step;

    /* Ledger lines */
    ctx2.strokeStyle='#333';ctx2.lineWidth=1.5;
    (note.ledger||[]).forEach(function(lpos){
      var ly=bottomLine-lpos*step;
      ctx2.beginPath();ctx2.moveTo(noteX-18,ly);ctx2.lineTo(noteX+18,ly);ctx2.stroke();
    });
    /* Auto ledger for pos < 0 or > 10 */
    if(note.pos<0){
      for(var p=0;p>=note.pos;p-=2){
        var ly=bottomLine-p*step;
        ctx2.beginPath();ctx2.moveTo(noteX-18,ly);ctx2.lineTo(noteX+18,ly);ctx2.stroke();
      }
    }
    if(note.pos>10){
      for(var p=12;p<=note.pos;p+=2){
        var ly=bottomLine-p*step;
        ctx2.beginPath();ctx2.moveTo(noteX-18,ly);ctx2.lineTo(noteX+18,ly);ctx2.stroke();
      }
    }

    /* Note head */
    var r=step*0.82;
    ctx2.fillStyle='#111';
    ctx2.beginPath();
    ctx2.ellipse(noteX,noteY,r*1.18,r*0.82,-0.3,0,Math.PI*2);
    ctx2.fill();

    /* Stem */
    var stemDir=note.pos>=5?-1:1;
    ctx2.strokeStyle='#111';ctx2.lineWidth=1.8;
    ctx2.beginPath();
    if(stemDir===1){ctx2.moveTo(noteX+r*1.1,noteY);ctx2.lineTo(noteX+r*1.1,noteY-lineGap*3.5);}
    else{ctx2.moveTo(noteX-r*1.1,noteY);ctx2.lineTo(noteX-r*1.1,noteY+lineGap*3.5);}
    ctx2.stroke();

    /* Accidental */
    if(note.acc){
      ctx2.fillStyle='#111';
      ctx2.font='bold '+(lineGap*2.2)+'px serif';
      ctx2.textBaseline='middle';
      var sym=note.acc==='#'?'♯':'♭';
      ctx2.fillText(sym,noteX-r*3.2,noteY+(note.acc==='b'?-step*0.3:0));
    }

    /* Clef label */
    ctx2.fillStyle='#666';ctx2.font='bold 11px sans-serif';ctx2.textBaseline='top';
    ctx2.fillText(isT?'Treble Clef':'Bass Clef',staffLeft,2);
  }

  /* ── Keyboard ── */
  var WHITE_NAMES=['C','D','E','F','G','A','B'];
  var HAS_BLACK=[0,1,3,4,5];/* white indices with a black key after */
  /* Build keyboard covering C3–C5 */
  var KB_NOTES=[];/* {name, acc, oct, isBlack} */
  for(var oct=3;oct<=5;oct++){
    WHITE_NAMES.forEach(function(n,wi){
      KB_NOTES.push({name:n,acc:'',oct:oct,isBlack:false,wi:wi});
      if(HAS_BLACK.includes(wi)){
        var sName=['C#','D#','','F#','G#','A#'][wi];
        if(sName)KB_NOTES.push({name:sName[0],acc:'#',oct:oct,isBlack:true,wi:wi});
      }
    });
  }

  function buildKb(){
    var inner=document.getElementById('nrKbInner');inner.innerHTML='';
    var whites=KB_NOTES.filter(function(n){return !n.isBlack;});
    whites.forEach(function(n,wi){
      var k=document.createElement('div');k.className='nr-kw';
      var noteId=n.name+(n.acc||'')+n.oct;
      k.dataset.note=n.name;k.dataset.acc=n.acc;k.dataset.oct=n.oct;k.dataset.id=noteId;
      var lbl=document.createElement('div');lbl.className='nr-kb-label';
      lbl.textContent=n.name+(n.oct===4&&n.name==='C'?' (mid)':'');k.appendChild(lbl);
      k.addEventListener('click',function(){checkAnswer(n.name,n.acc,n.oct,k);});
      inner.appendChild(k);
      /* Black key */
      if(HAS_BLACK.includes(n.wi)&&wi<whites.length-1){
        var bn=KB_NOTES.find(function(x){return x.isBlack&&x.wi===n.wi&&x.oct===n.oct;});
        if(bn){
          var bk=document.createElement('div');bk.className='nr-kbl';
          bk.dataset.note=bn.name;bk.dataset.acc='#';bk.dataset.oct=bn.oct;
          var bl=document.createElement('div');bl.className='nr-kbl-label';
          bl.textContent=bn.name+'#/'+(['Db','Eb','','Gb','Ab','Bb'][bn.wi]||'');bk.appendChild(bl);
          bk.addEventListener('click',function(e){e.stopPropagation();checkAnswer(bn.name,'#',bn.oct,bk);});
          k.style.position='relative';k.appendChild(bk);
        }
      }
    });

    /* Also add flat keys as clickable on existing black keys */
    /* Map sharps to flat equivalents so clicking a black key works for both */
  }

  function checkAnswer(name,acc,oct,el){
    if(answered||!current)return;
    answered=true;
    /* Check match — allow enharmonic equivalents */
    var ok=isMatch(name,acc,oct,current);
    if(ok){correct++;streak++;}else{wrong++;streak=0;}
    el.classList.add(ok?'correct':'wrong');
    /* Highlight correct key if wrong */
    if(!ok){
      document.querySelectorAll('[data-note]').forEach(function(k){
        if(k.dataset.note===current.name&&k.dataset.acc===(current.acc||'')&&parseInt(k.dataset.oct)===current.oct){
          k.classList.add('correct');
        }
      });
    }
    var fb=document.getElementById('nrFeedback');
    var fullName=current.name+(current.acc==='#'?'♯':current.acc==='b'?'♭':'')+(current.oct||'');
    if(ok){
      fb.textContent='✅ Correct! '+fullName;fb.style.color='#22c55e';fb.style.background='rgba(34,197,94,.1)';
    } else {
      fb.textContent='❌ It was '+fullName;fb.style.color='#ef4444';fb.style.background='rgba(239,68,68,.1)';
    }
    document.getElementById('nrCorrect').textContent=correct;
    document.getElementById('nrStreak').textContent=streak;
    document.getElementById('nrWrong').textContent=wrong;
  }

  var ENHARMONIC={
    'C#':'Db','Db':'C#','D#':'Eb','Eb':'D#','F#':'Gb','Gb':'F#',
    'G#':'Ab','Ab':'G#','A#':'Bb','Bb':'A#','B#':'C','Cb':'B'
  };
  function isMatch(name,acc,oct,note){
    var guess=(name+(acc||'')).trim();
    var target=(note.name+(note.acc||'')).trim();
    if(guess===target&&oct===note.oct)return true;
    /* Enharmonic */
    var enh=ENHARMONIC[target];
    if(enh&&enh===guess&&oct===note.oct)return true;
    return false;
  }

  window.nextNote=function(){
    answered=false;
    document.getElementById('nrFeedback').textContent='';
    document.getElementById('nrFeedback').style.background='transparent';
    document.querySelectorAll('.nr-kw,.nr-kbl').forEach(function(k){
      k.classList.remove('correct','wrong','highlight');
    });
    var pool=[];
    if(clefMode==='treble'||clefMode==='both') pool=pool.concat(TREBLE_NOTES);
    if(clefMode==='bass'||clefMode==='both') pool=pool.concat(BASS_NOTES);
    if(!useAccidentals) pool=pool.filter(function(n){return !n.acc;});
    /* Don't repeat same note twice */
    var filtered=pool.filter(function(n){return !current||n.name!==current.name||n.acc!==current.acc||n.oct!==current.oct||n.clef!==current.clef;});
    if(!filtered.length)filtered=pool;
    current=filtered[Math.floor(Math.random()*filtered.length)];
    drawStaff(current);
    /* Hint: highlight the octave range on keyboard */
    document.querySelectorAll('[data-oct="'+current.oct+'"]').forEach(function(k){
      if(!k.classList.contains('correct')&&!k.classList.contains('wrong'))
        k.classList.add('highlight');
    });
    setTimeout(function(){
      document.querySelectorAll('.highlight').forEach(function(k){k.classList.remove('highlight');});
    },600);
  };

  buildKb();
  nextNote();
})();
</script>
"""

@ext_bp.route('/ext/note-reading')
@login_required
def ext_note_reading():
    return make_shell(EXT_NOTEREADING_CONTENT, extra_css=EXT_NOTEREADING_CSS, **nav_ctx())


@ext_bp.route("/ext/scale-finder")
@login_required
def ext_scale_finder():
    return make_shell(EXT_SCALE_FINDER, **nav_ctx())

@ext_bp.route("/ext/circle-of-fifths")
@login_required
def ext_circle_of_fifths():
    return make_shell(EXT_CIRCLE_CONTENT, extra_css=EXT_CIRCLE_CSS, **nav_ctx())

@ext_bp.route("/ext/tuner")
@login_required
def ext_tuner():
    return make_shell(EXT_TUNER_CONTENT, **nav_ctx())

@ext_bp.route("/ext/pitch-detector")
@login_required
def ext_pitch_detector():
    return make_shell(EXT_TUNER_CONTENT, **nav_ctx())

@ext_bp.route("/ext/freq-calculator")
@login_required
def ext_freq_calc():
    return make_shell(EXT_FREQ_CONTENT, **nav_ctx())

@ext_bp.route("/ext/chord-progression")
@login_required
def ext_chord_progression():
    return make_shell(EXT_PROGRESSION_CONTENT, extra_css=EXT_PROGRESSION_CSS, **nav_ctx())

@ext_bp.route("/ext/notation-guide")
@login_required
def ext_notation_guide():
    return make_shell(EXT_NOTATION_CONTENT, **nav_ctx())

@ext_bp.route("/ext/rhythm-trainer")
@login_required
def ext_rhythm_trainer():
    return make_shell(EXT_RHYTHM_CONTENT, extra_css=EXT_RHYTHM_CSS, **nav_ctx())

@ext_bp.route("/ext/ear-training")
@login_required
def ext_ear_training():
    return make_shell(EXT_EAR_CONTENT, extra_css=EXT_EAR_CSS, **nav_ctx())

@ext_bp.route("/ext/time-sig-trainer")
@login_required
def ext_time_sig_trainer():
    return make_shell(EXT_TIMESIG_CONTENT, **nav_ctx())

@ext_bp.route("/ext/solfege")
@login_required
def ext_solfege():
    return make_shell(EXT_SOLFEGE_CONTENT, **nav_ctx())

@ext_bp.route("/ext/form-analyzer", methods=["GET","POST"])
@login_required
def ext_form_analyzer():
    result=None;error=None
    if request.method=="POST":
        f=request.files.get("file")
        if not f or not f.filename: error="No file selected."
        else:
            try:
                result=analyze_form(f.read())
            except Exception as e: error=str(e)
    content=render_template_string(EXT_FORM_CONTENT, result=result, error=error)
    return make_shell(content, **nav_ctx())


# Add routes for new extensions
@ext_bp.route("/ext/piano-keyboard")
@login_required
def ext_piano_keyboard():
    return make_shell(EXT_PIANO_CONTENT, extra_css=EXT_PIANO_CSS, **nav_ctx())

@ext_bp.route("/ext/music-quiz")
@login_required
def ext_music_quiz():
    return make_shell(EXT_QUIZ_CONTENT, extra_css=EXT_QUIZ_CSS, **nav_ctx())

@ext_bp.route("/ext/tempo-converter")
@login_required
def ext_tempo_converter():
    return make_shell(EXT_TEMPO_CONTENT, **nav_ctx())

@ext_bp.route("/ext/metronome-visual")
@login_required
def ext_metronome_visual():
    return make_shell(ext_stub("📊","Visual Metronome","Pendulum-style visual metronome — coming soon!"), **nav_ctx())

