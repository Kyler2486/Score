import io, zipfile
import xml.etree.ElementTree as ET
from collections import Counter

KEY_MAP = {-7:"C♭ Major",-6:"G♭ Major",-5:"D♭ Major",-4:"A♭ Major",-3:"E♭ Major",
           -2:"B♭ Major",-1:"F Major",0:"C Major",1:"G Major",2:"D Major",
           3:"A Major",4:"E Major",5:"B Major",6:"F♯ Major",7:"C♯ Major"}
ACC_MAP = {"1":"#","-1":"b","0":"♮"}

def parse_musicxml(content):
    root = ET.fromstring(content)
    lines, tempo, time_sig, key_sig, clef = [],"Unknown","Unknown","Unknown","Unknown"
    for part in root.findall('.//part'):
        for m in part.findall('.//measure'):
            t=m.find('.//time')
            if t is not None: time_sig=f"{t.find('beats').text}/{t.find('beat-type').text}"
            s=m.find('.//sound')
            if s is not None and 'tempo' in s.attrib: tempo=s.attrib['tempo']
            k=m.find('.//key')
            if k is not None: key_sig=KEY_MAP.get(int(k.find('fifths').text),"Unknown")
            c=m.find('.//clef')
            if c is not None: clef=f"{c.find('sign').text} Clef"
            notes=[]
            for n in m.findall('.//note'):
                p=n.find('pitch'); dur=n.find('duration'); nt=n.find('type')
                if p is not None:
                    acc=ACC_MAP.get(p.find('alter').text,'') if p.find('alter') is not None else ''
                    nr=f"{p.find('step').text}{acc}{p.find('octave').text} ({nt.text if nt is not None else '?'},{dur.text if dur is not None else '?'})"
                else: nr="Rest"
                if n.find('chord') is not None: nr=f"[Chord] {nr}"
                lyr=n.find('lyric/text')
                if lyr is not None: nr+=f" - Lyric: {lyr.text}"
                notes.append(nr)
            lines.append(f"Measure {m.attrib['number']}: "+", ".join(notes))
    return f"Tempo: {tempo} BPM\nTime Signature: {time_sig}\nKey Signature: {key_sig}\nClef: {clef}\n\n"+"\n".join(lines)

def mxl_to_xml(mxl_bytes):
    with zipfile.ZipFile(io.BytesIO(mxl_bytes)) as z:
        try:
            container = z.read('META-INF/container.xml')
            cr = ET.fromstring(container)
            rf = cr.find('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile') or cr.find('.//rootfile')
            if rf is not None:
                return z.read(rf.get('full-path')).decode('utf-8')
        except Exception:
            pass
        for name in z.namelist():
            if name.endswith('.xml') and 'META-INF' not in name:
                return z.read(name).decode('utf-8')
    raise ValueError('No MusicXML file found inside the .mxl archive.')

def extract_metadata(content):
    root = ET.fromstring(content)
    info = {'title':None,'composer':None,'arranger':None,'lyricist':None,
            'tempo':None,'time_sig':None,'key':None,'parts':[],'measures':0,'copyright':None}
    work = root.find('.//work')
    if work is not None:
        t=work.find('work-title')
        if t is not None and t.text: info['title']=t.text.strip()
    mv=root.find('.//movement-title')
    if mv is not None and mv.text: info['title']=info['title'] or mv.text.strip()
    ident=root.find('.//identification')
    if ident is not None:
        for cr in ident.findall('creator'):
            tp=cr.get('type','')
            if tp=='composer' and cr.text: info['composer']=cr.text.strip()
            elif tp=='arranger' and cr.text: info['arranger']=cr.text.strip()
            elif tp=='lyricist' and cr.text: info['lyricist']=cr.text.strip()
        rights=ident.find('rights')
        if rights is not None and rights.text: info['copyright']=rights.text.strip()
    for pn in root.findall('.//part-name'):
        if pn.text and pn.text.strip(): info['parts'].append(pn.text.strip())
    for pi in root.findall('.//instrument-name'):
        if pi.text and pi.text.strip() and pi.text.strip() not in info['parts']:
            info['parts'].append(pi.text.strip())
    first_m=root.find('.//measure')
    if first_m is not None:
        s=first_m.find('.//sound')
        if s is not None and 'tempo' in s.attrib: info['tempo']=s.attrib['tempo']
        t=first_m.find('.//time')
        if t is not None:
            beats=t.find('beats'); bt=t.find('beat-type')
            if beats is not None and bt is not None: info['time_sig']=f"{beats.text}/{bt.text}"
        k=first_m.find('.//key')
        if k is not None:
            f5=k.find('fifths')
            if f5 is not None: info['key']=KEY_MAP.get(int(f5.text),"Unknown")
    all_m=root.findall('.//measure')
    if all_m:
        try: info['measures']=max(int(m.get('number',0)) for m in all_m)
        except: info['measures']=len(all_m)
    return info

def note_stats(content):
    root = ET.fromstring(content)
    note_counts = Counter()
    dur_counts = Counter()
    total_notes = 0; total_rests = 0; total_chords = 0
    for note in root.findall('.//note'):
        p=note.find('pitch')
        if p is not None:
            step=p.find('step').text
            alter_el=p.find('alter')
            alter=int(float(alter_el.text)) if alter_el is not None else 0
            acc='#' if alter>0 else ('b' if alter<0 else '')
            note_counts[f"{step}{acc}"]+=1
            total_notes+=1
            if note.find('chord') is not None: total_chords+=1
        else: total_rests+=1
        nt=note.find('type')
        if nt is not None: dur_counts[nt.text]+=1
    return {'note_counts':dict(note_counts.most_common(12)),
            'dur_counts':dict(dur_counts.most_common()),
            'total_notes':total_notes,'total_rests':total_rests,'total_chords':total_chords}

NOTE_TO_SEMI = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
SEMI_TO_SHARP = {0:('C',0),1:('C',1),2:('D',0),3:('D',1),4:('E',0),
                 5:('F',0),6:('F',1),7:('G',0),8:('G',1),9:('A',0),10:('A',1),11:('B',0)}
SEMI_TO_FLAT  = {0:('C',0),1:('D',-1),2:('D',0),3:('E',-1),4:('E',0),
                 5:('F',0),6:('G',-1),7:('G',0),8:('A',-1),9:('A',0),10:('B',-1),11:('B',0)}
SEMI_TO_FIFTH = {0:0,1:7,2:2,3:9,4:4,5:11,6:6,7:1,8:8,9:3,10:10,11:5}

def transpose_xml(content, semitones):
    if semitones == 0: return content
    lut = SEMI_TO_SHARP if semitones > 0 else SEMI_TO_FLAT
    tree = ET.parse(io.BytesIO(content if isinstance(content,bytes) else content.encode()))
    root = tree.getroot()
    for pitch in root.findall('.//pitch'):
        step_el=pitch.find('step'); oct_el=pitch.find('octave'); alt_el=pitch.find('alter')
        if step_el is None or oct_el is None: continue
        step=step_el.text; octave=int(oct_el.text)
        alter=int(float(alt_el.text)) if alt_el is not None else 0
        total=(NOTE_TO_SEMI[step]+alter+octave*12+semitones)
        new_oct=total//12; new_semi=total%12
        new_step,new_alter=lut[new_semi]
        step_el.text=new_step; oct_el.text=str(new_oct)
        if new_alter!=0:
            if alt_el is None:
                alt_el=ET.SubElement(pitch,'alter')
                children=list(pitch)
                if len(children)>1: pitch.remove(alt_el); pitch.insert(children.index(oct_el)+1,alt_el)
            alt_el.text=str(float(new_alter))
        else:
            if alt_el is not None: pitch.remove(alt_el)
    for key in root.findall('.//key'):
        f5=key.find('fifths')
        if f5 is not None:
            old=int(f5.text); delta=SEMI_TO_FIFTH[semitones%12]
            new_f=old+delta
            while new_f>7: new_f-=12
            while new_f<-7: new_f+=12
            f5.text=str(new_f)
    out=io.BytesIO(); tree.write(out,encoding='unicode',xml_declaration=True)
    return out.getvalue().encode('utf-8')

def analyze_form(xml_bytes):
    """Analyze musical form from MusicXML."""
    import xml.etree.ElementTree as ET2
    root = ET2.fromstring(xml_bytes)
    key_map = {-7:"Cb Major",-6:"Gb Major",-5:"Db Major",-4:"Ab Major",-3:"Eb Major",
               -2:"Bb Major",-1:"F Major",0:"C Major",1:"G Major",2:"D Major",
               3:"A Major",4:"E Major",5:"B Major",6:"F# Major",7:"C# Major"}
    measures = root.findall('.//measure')
    total = len(measures)
    tempo = None; key = None
    first = measures[0] if measures else None
    if first is not None:
        s=first.find('.//sound'); k=first.find('.//key')
        if s is not None and 'tempo' in s.attrib: tempo=s.attrib['tempo']
        if k is not None:
            f5=k.find('fifths')
            if f5 is not None: key=key_map.get(int(f5.text),'Unknown')
    # Simple sectional analysis based on measure groupings
    section_size = max(4, total//4) if total > 8 else total
    labels = ['A','B','C','D','E','F','G','H']
    sections = []
    i = 0; li = 0
    while i < total:
        end = min(i+section_size, total)
        sections.append({'label':labels[li%len(labels)], 'start':i+1, 'end':end})
        i = end; li += 1
    # Guess form name
    n = len(sections)
    if n == 1: form = 'Through-composed (A)'
    elif n == 2: form = 'Binary Form (AB)'
    elif n == 3:
        if sections[0]['label'] == sections[2]['label']: form = 'Ternary Form (ABA)'
        else: form = 'Three-part Form (ABC)'
    elif n == 4: form = 'ABAB or Verse-Chorus Form'
    else: form = f'Extended Form ({"-".join([s["label"] for s in sections])})'
    return {'form_label':form,'measures':total,'sections':sections,'key':key,'tempo':tempo}
