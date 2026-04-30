import io, sqlite3
import xml.etree.ElementTree as ET
from flask import Blueprint, request, jsonify, send_file, render_template_string, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from scorelab.models import get_db, load_user, reload_current_user, push_msg, pop_msgs
from scorelab.music_utils import parse_musicxml, mxl_to_xml, extract_metadata, note_stats, transpose_xml, analyze_form
from scorelab.templates.shell import make_shell, nav_ctx, save_upload, delete_file
from scorelab.templates.tools_content import (
    CONVERTER_CSS, CONVERTER_CONTENT, MXL_CONTENT, META_CONTENT,
    TRANSPOSE_CONTENT, STATS_CSS, STATS_CONTENT, BPM_CSS, BPM_CONTENT,
)
from scorelab.templates.tools_content2 import (
    METRONOME_CSS, METRONOME_CONTENT, VIEWER_CSS, VIEWER_CONTENT,
    INTERVAL_CSS, INTERVAL_CONTENT, CHORD_CSS, CHORD_CONTENT,
    SETTINGS_CSS, SETTINGS_CONTENT, PROFILE_CSS, PROFILE_CONTENT,
    SECRET_TEMPLATE, TUNER_CSS, TUNER_CONTENT, OSCOPE_CSS, OSCOPE_CONTENT, ERROR_404,
)
from scorelab.templates.admin_content import ADMIN_CSS, ADMIN_CONTENT, BANNED_TEMPLATE
from scorelab.app import AVATAR_DIR, BANNER_DIR

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return make_shell(CONVERTER_CONTENT, extra_css=CONVERTER_CSS, **nav_ctx())

@main_bp.route('/convert', methods=['POST'])
@login_required
def convert():
    if 'file' not in request.files: return jsonify({'error':'No file uploaded.'}),400
    f=request.files['file']
    if not f.filename: return jsonify({'error':'No file selected.'}),400
    if not (f.filename.endswith('.xml') or f.filename.endswith('.musicxml')):
        return jsonify({'error':'Please upload a .xml or .musicxml file.'}),400
    try: return jsonify({'text':parse_musicxml(f.read())})
    except ET.ParseError as e: return jsonify({'error':f'Invalid XML: {e}'}),400
    except Exception as e: return jsonify({'error':f'Error: {e}'}),500

@main_bp.route('/tools/mxl', methods=['GET','POST'])
@login_required
def tool_mxl():
    error = None
    if request.method == 'POST':
        f = request.files.get('file')
        if not f or not f.filename: error = 'No file selected.'
        else:
            try:
                xml_str = mxl_to_xml(f.read())
                out_name = f.filename.rsplit('.',1)[0] + '.xml'
                return send_file(io.BytesIO(xml_str.encode('utf-8')),
                                 mimetype='application/xml',
                                 as_attachment=True, download_name=out_name)
            except Exception as e: error = str(e)
    content = render_template_string(MXL_CONTENT, error=error)
    return make_shell(content, **nav_ctx())

@main_bp.route('/tools/metadata', methods=['GET','POST'])
@login_required
def tool_metadata():
    meta=None; error=None
    if request.method=='POST':
        f=request.files.get('file')
        if not f or not f.filename: error='No file selected.'
        else:
            try: meta=extract_metadata(f.read())
            except Exception as e: error=str(e)
    content = render_template_string(META_CONTENT, meta=meta, error=error)
    return make_shell(content, **nav_ctx())

@main_bp.route('/tools/transpose', methods=['GET','POST'])
@login_required
def tool_transpose():
    error=None
    if request.method=='POST':
        f=request.files.get('file'); semi=int(request.form.get('semitones',0))
        if not f or not f.filename: error='No file selected.'
        else:
            try:
                result=transpose_xml(f.read(), semi)
                sign='+' if semi>0 else ''
                out_name=f.filename.rsplit('.',1)[0]+f'_transposed_{sign}{semi}st.xml'
                return send_file(io.BytesIO(result),mimetype='application/xml',
                                 as_attachment=True,download_name=out_name)
            except Exception as e: error=str(e)
    content = render_template_string(TRANSPOSE_CONTENT, error=error)
    return make_shell(content, **nav_ctx())

@main_bp.route('/tools/stats', methods=['GET','POST'])
@login_required
def tool_stats():
    stats=None; error=None
    if request.method=='POST':
        f=request.files.get('file')
        if not f or not f.filename: error='No file selected.'
        else:
            try: stats=note_stats(f.read())
            except Exception as e: error=str(e)
    content = render_template_string(STATS_CONTENT, stats=stats, error=error)
    return make_shell(content, extra_css=STATS_CSS, **nav_ctx())


@main_bp.route('/tools/tuner')
@login_required
def tool_tuner():
    return make_shell(TUNER_CONTENT, extra_css=TUNER_CSS, **nav_ctx())

@main_bp.route('/tools/oscilloscope')
@login_required
def tool_oscilloscope():
    return make_shell(OSCOPE_CONTENT, extra_css=OSCOPE_CSS, **nav_ctx())

@main_bp.route('/tools/bpm')
@login_required
def tool_bpm():
    return make_shell(BPM_CONTENT, extra_css=BPM_CSS, **nav_ctx())

@main_bp.route('/tools/metronome')
@login_required
def tool_metronome():
    return make_shell(METRONOME_CONTENT, extra_css=METRONOME_CSS, **nav_ctx())

@main_bp.route('/tools/viewer')
@login_required
def tool_viewer():
    return make_shell(VIEWER_CONTENT, extra_css=VIEWER_CSS, **nav_ctx())

@main_bp.route('/tools/interval')
@login_required
def tool_interval():
    return make_shell(INTERVAL_CONTENT, extra_css=INTERVAL_CSS, **nav_ctx())

@main_bp.route('/tools/chord')
@login_required
def tool_chord():
    return make_shell(CHORD_CONTENT, extra_css=CHORD_CSS, **nav_ctx())

# Metronome preset API
@main_bp.route('/api/presets', methods=['GET'])
@login_required
def api_presets_get():
    with get_db() as conn:
        rows = conn.execute('SELECT * FROM metronome_presets WHERE user_id=? ORDER BY created_at DESC',
                           (current_user.id,)).fetchall()
    return jsonify([dict(r) for r in rows])

@main_bp.route('/api/presets', methods=['POST'])
@login_required
def api_presets_post():
    data = request.get_json()
    if not data or not data.get('name'): return jsonify({'error':'Name required'}),400
    with get_db() as conn:
        conn.execute('INSERT INTO metronome_presets (user_id,name,bpm,time_sig,sound) VALUES(?,?,?,?,?)',
            (current_user.id, data['name'], int(data.get('bpm',120)),
             int(data.get('time_sig',4)), data.get('sound','click')))
        conn.commit()
    return jsonify({'ok':True})

@main_bp.route('/api/presets/<int:pid>', methods=['DELETE'])
@login_required
def api_presets_delete(pid):
    with get_db() as conn:
        conn.execute('DELETE FROM metronome_presets WHERE id=? AND user_id=?',(pid,current_user.id))
        conn.commit()
    return jsonify({'ok':True})


@main_bp.route('/secret')
@login_required
def secret():
    return render_template_string(SECRET_TEMPLATE, **nav_ctx())

@main_bp.route('/settings')
@login_required
def settings():
    return make_shell(SETTINGS_CONTENT, extra_css=SETTINGS_CSS, **nav_ctx())

@main_bp.route('/profile')
@login_required
def profile():
    u=reload_current_user()
    content=render_template_string(PROFILE_CONTENT, messages=pop_msgs(),
        banner_url=u.banner_url, **nav_ctx(u))
    return make_shell(content, extra_css=PROFILE_CSS, **nav_ctx(u))

@main_bp.route('/profile/banner', methods=['POST'])
@login_required
def profile_banner():
    f=request.files.get('banner')
    if not f or not f.filename: push_msg('error','No file selected.'); return redirect(url_for('main.profile'))
    with get_db() as conn:
        old=conn.execute('SELECT banner FROM users WHERE id=?',(current_user.id,)).fetchone()
        delete_file(BANNER_DIR, old['banner'] if old else None)
    fn,err=save_upload(f,BANNER_DIR,current_user.id)
    if err: push_msg('error',err); return redirect(url_for('main.profile'))
    with get_db() as conn:
        conn.execute('UPDATE users SET banner=? WHERE id=?',(fn,current_user.id)); conn.commit()
    push_msg('success','Banner updated.'); return redirect(url_for('main.profile'))

@main_bp.route('/profile/banner/remove', methods=['POST'])
@login_required
def profile_banner_remove():
    with get_db() as conn:
        old=conn.execute('SELECT banner FROM users WHERE id=?',(current_user.id,)).fetchone()
        delete_file(BANNER_DIR, old['banner'] if old else None)
        conn.execute('UPDATE users SET banner=NULL WHERE id=?',(current_user.id,)); conn.commit()
    push_msg('success','Banner removed.'); return redirect(url_for('main.profile'))

@main_bp.route('/profile/avatar', methods=['POST'])
@login_required
def profile_avatar():
    f=request.files.get('avatar')
    if not f or not f.filename: push_msg('error','No file selected.'); return redirect(url_for('main.profile'))
    with get_db() as conn:
        old=conn.execute('SELECT avatar FROM users WHERE id=?',(current_user.id,)).fetchone()
        delete_file(AVATAR_DIR, old['avatar'] if old else None)
    fn,err=save_upload(f,AVATAR_DIR,current_user.id)
    if err: push_msg('error',err); return redirect(url_for('main.profile'))
    with get_db() as conn:
        conn.execute('UPDATE users SET avatar=? WHERE id=?',(fn,current_user.id)); conn.commit()
    push_msg('success','Profile picture updated.'); return redirect(url_for('main.profile'))

@main_bp.route('/profile/display-name', methods=['POST'])
@login_required
def profile_display_name():
    dn=request.form.get('display_name','').strip()
    if not dn: push_msg('error','Cannot be empty.'); return redirect(url_for('main.profile'))
    with get_db() as conn:
        conn.execute('UPDATE users SET display_name=? WHERE id=?',(dn,current_user.id)); conn.commit()
    push_msg('success','Display name updated.'); return redirect(url_for('main.profile'))

@main_bp.route('/profile/username', methods=['POST'])
@login_required
def profile_username():
    un=request.form.get('username','').strip()
    if not un: push_msg('error','Cannot be empty.'); return redirect(url_for('main.profile'))
    try:
        with get_db() as conn:
            conn.execute('UPDATE users SET username=? WHERE id=?',(un,current_user.id)); conn.commit()
        push_msg('success','Username updated.')
    except sqlite3.IntegrityError: push_msg('error','That username is already taken.')
    return redirect(url_for('main.profile'))

@main_bp.route('/profile/password', methods=['POST'])
@login_required
def profile_password():
    cur=request.form.get('current_password','')
    new=request.form.get('new_password','')
    conf=request.form.get('confirm_password','')
    with get_db() as conn:
        row=conn.execute('SELECT password FROM users WHERE id=?',(current_user.id,)).fetchone()
    if not check_password_hash(row['password'],cur): push_msg('error','Current password is incorrect.')
    elif len(new)<6: push_msg('error','New password must be at least 6 characters.')
    elif new!=conf: push_msg('error','Passwords do not match.')
    else:
        with get_db() as conn:
            conn.execute('UPDATE users SET password=? WHERE id=?',(generate_password_hash(new),current_user.id)); conn.commit()
        push_msg('success','Password changed.')
    return redirect(url_for('main.profile'))


@main_bp.route('/banned')
def banned():
    reason = current_user.ban_reason if current_user.is_authenticated else None
    return render_template_string(BANNED_TEMPLATE, reason=reason)

# ── Admin panel ───────────────────────────────────────────────────────────────
@main_bp.route('/admin')
@login_required
def admin_panel():
    if not current_user.is_admin:
        return redirect(url_for('main.index'))
    with get_db() as conn:
        users = conn.execute('SELECT * FROM users ORDER BY id').fetchall()
        stats = {
            'total': len(users),
            'admins': sum(1 for u in users if u['is_admin']),
            'banned': sum(1 for u in users if u['is_banned']),
        }
    return make_shell(ADMIN_CONTENT, extra_css=ADMIN_CSS,
                      users=users, stats=stats, **nav_ctx())

@main_bp.route('/admin/action', methods=['POST'])
@login_required
def admin_action():
    if not current_user.is_admin:
        return redirect(url_for('main.index'))
    uid = request.form.get('user_id', type=int)
    action = request.form.get('action','')
    extra = request.form.get('extra','')
    if not uid: return redirect(url_for('main.admin_panel'))
    with get_db() as conn:
        user = conn.execute('SELECT * FROM users WHERE id=?',(uid,)).fetchone()
        if not user: return redirect(url_for('main.admin_panel'))
        # Prevent acting on yourself
        if uid == current_user.id: return redirect(url_for('main.admin_panel'))
        if action == 'ban':
            conn.execute('UPDATE users SET is_banned=1,ban_reason=? WHERE id=?',(extra or 'No reason given.',uid))
            flash(f'Banned {user["display_name"]}.','success')
        elif action == 'unban':
            conn.execute('UPDATE users SET is_banned=0,ban_reason=NULL WHERE id=?',(uid,))
            flash(f'Unbanned {user["display_name"]}.','success')
        elif action == 'make_admin':
            conn.execute('UPDATE users SET is_admin=1 WHERE id=?',(uid,))
            flash(f'Made {user["display_name"]} an admin.','success')
        elif action == 'remove_admin':
            conn.execute('UPDATE users SET is_admin=0 WHERE id=?',(uid,))
            flash(f'Removed admin from {user["display_name"]}.','success')
        elif action == 'delete':
            conn.execute('DELETE FROM users WHERE id=?',(uid,))
            flash(f'Deleted {user["display_name"]}.','success')
        conn.commit()
    return redirect(url_for('main.admin_panel'))

@main_bp.app_errorhandler(404)
def not_found(e): return render_template_string(ERROR_404), 404
