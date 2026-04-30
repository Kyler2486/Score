from scorelab.templates.shell import BASE_CSS, THEME_SCRIPT

BANNED_TEMPLATE = """<!DOCTYPE html><html lang="en"><head>
""" + THEME_SCRIPT + """
<meta charset="UTF-8"/><meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Banned — ScoreLab</title>
<style>""" + BASE_CSS + """
body{align-items:center;justify-content:center;min-height:100vh;padding:20px}
.ban-card{background:var(--card);border:2px solid #7f1d1d;border-radius:16px;padding:48px 36px;
  max-width:480px;width:100%;text-align:center}
.ban-icon{font-size:4rem;margin-bottom:16px}
.ban-title{font-size:1.6rem;font-weight:800;color:#ef4444;margin-bottom:8px}
.ban-sub{color:var(--text-muted);font-size:.93rem;margin-bottom:24px}
.ban-reason{background:#2d1b1b;border:1px solid #7f1d1d;border-radius:10px;padding:16px 20px;
  font-size:.9rem;color:#fca5a5;text-align:left;margin-bottom:24px;line-height:1.6}
.ban-reason strong{color:#f87171;display:block;margin-bottom:4px;font-size:.78rem;text-transform:uppercase;letter-spacing:.06em}
</style></head><body>
<div class="ban-card">
  <div class="ban-icon">🔨</div>
  <div class="ban-title">You've been banned</div>
  <div class="ban-sub">Your account has been suspended from ScoreLab.</div>
  {% if reason %}
  <div class="ban-reason"><strong>Reason</strong>{{ reason }}</div>
  {% endif %}
  <div style="font-size:.83rem;color:var(--text-faint)">
    If you believe this was a mistake, contact the administrator.
  </div>
</div>
</body></html>"""

# ── Admin panel ───────────────────────────────────────────────────────────────
ADMIN_CSS = """
.admin-table{width:100%;border-collapse:collapse;font-size:.85rem}
.admin-table th{text-align:left;padding:8px 12px;border-bottom:2px solid var(--border);
  font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;color:var(--text-xfaint)}
.admin-table td{padding:10px 12px;border-bottom:1px solid var(--border);vertical-align:middle}
.admin-table tr:last-child td{border-bottom:none}
.admin-table tr:hover td{background:var(--hover-bg)}
.badge{display:inline-block;padding:2px 8px;border-radius:99px;font-size:.72rem;font-weight:700}
.badge-admin{background:rgba(99,102,241,.2);color:var(--accent-text)}
.badge-banned{background:rgba(239,68,68,.2);color:#f87171}
.badge-user{background:var(--hover-bg);color:var(--text-faint)}
.admin-actions{display:flex;gap:6px;flex-wrap:wrap}
.admin-actions button{padding:4px 10px;border-radius:6px;font-size:.78rem;cursor:pointer;
  border:1px solid var(--border);background:var(--input-bg);color:var(--text-muted);transition:all .15s}
.admin-actions button:hover{background:var(--hover-bg);color:var(--text)}
.admin-actions button.ban-btn{border-color:#7f1d1d;color:#f87171}
.admin-actions button.ban-btn:hover{background:#2d1b1b}
.admin-actions button.unban-btn{border-color:#166534;color:#86efac}
.admin-actions button.unban-btn:hover{background:#14261f}
.admin-actions button.admin-btn{border-color:#4f46e5;color:var(--accent-text)}
.admin-stats{display:flex;gap:14px;margin-bottom:20px;flex-wrap:wrap}
.admin-stat{background:var(--input-bg);border:1px solid var(--border);border-radius:10px;
  padding:12px 20px;text-align:center;flex:1;min-width:80px}
.admin-stat .n{font-size:1.8rem;font-weight:800;color:var(--accent-text)}
.admin-stat .l{font-size:.72rem;color:var(--text-faint);text-transform:uppercase}
"""

ADMIN_CONTENT = """
<div class="page-title">🛡️ Admin Panel</div>
<p class="page-sub">Manage users, bans, and app activity.</p>

{% with messages = get_flashed_messages(with_categories=true) %}
{% for cat,msg in messages %}<div class="flash {{cat}}">{{msg}}</div>{% endfor %}
{% endwith %}

<div class="card">
  <div class="admin-stats">
    <div class="admin-stat"><div class="n">{{stats.total}}</div><div class="l">Users</div></div>
    <div class="admin-stat"><div class="n">{{stats.admins}}</div><div class="l">Admins</div></div>
    <div class="admin-stat"><div class="n" style="color:#ef4444">{{stats.banned}}</div><div class="l">Banned</div></div>
  </div>

  <div style="margin-bottom:14px">
    <input type="text" id="userSearch" placeholder="Search users…" style="margin-bottom:0"
      oninput="filterUsers(this.value)"/>
  </div>

  <table class="admin-table" id="userTable">
    <thead>
      <tr>
        <th>#</th><th>User</th><th>Email</th><th>Status</th><th>Actions</th>
      </tr>
    </thead>
    <tbody>
    {% for u in users %}
    <tr class="user-row" data-name="{{u.display_name|lower}} {{u.username|lower}} {{u.email|lower}}">
      <td style="color:var(--text-faint)">{{u.id}}</td>
      <td>
        <div style="font-weight:600;color:var(--text)">{{u.display_name}}</div>
        <div style="font-size:.76rem;color:var(--text-faint)">@{{u.username}}</div>
      </td>
      <td style="color:var(--text-muted);font-size:.82rem">{{u.email}}</td>
      <td>
        {% if u.is_admin %}<span class="badge badge-admin">Admin</span>{% endif %}
        {% if u.is_banned %}<span class="badge badge-banned">Banned</span>
          {% if u.ban_reason %}<div style="font-size:.74rem;color:#f87171;margin-top:3px">{{u.ban_reason}}</div>{% endif %}
        {% endif %}
        {% if not u.is_admin and not u.is_banned %}<span class="badge badge-user">User</span>{% endif %}
      </td>
      <td>
        {% if u.id != current_user.id %}
        <div class="admin-actions">
          {% if not u.is_banned %}
          <button class="ban-btn" onclick="showBanModal({{u.id}},'{{u.display_name|e}}')">🔨 Ban</button>
          {% else %}
          <button class="unban-btn" onclick="doAction({{u.id}},'unban')">✅ Unban</button>
          {% endif %}
          {% if not u.is_admin %}
          <button class="admin-btn" onclick="doAction({{u.id}},'make_admin')">⭐ Make Admin</button>
          {% else %}
          <button onclick="doAction({{u.id}},'remove_admin')">Remove Admin</button>
          {% endif %}
          <button onclick="doAction({{u.id}},'delete')" style="border-color:#7f1d1d;color:#f87171" 
            title="Permanently delete user">🗑️ Delete</button>
        </div>
        {% else %}
        <span style="font-size:.78rem;color:var(--text-faint)">That's you</span>
        {% endif %}
      </td>
    </tr>
    {% endfor %}
    </tbody>
  </table>
</div>

<!-- Ban modal -->
<div id="banModal" style="display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:9999;
  align-items:center;justify-content:center">
  <div style="background:var(--card);border:1px solid var(--border);border-radius:14px;padding:28px;
    max-width:420px;width:90%">
    <div style="font-size:1.1rem;font-weight:700;color:#ef4444;margin-bottom:16px">🔨 Ban User</div>
    <div id="banModalName" style="font-size:.9rem;color:var(--text-muted);margin-bottom:14px"></div>
    <label>Ban Reason (shown to user)</label>
    <input type="text" id="banReason" placeholder="e.g. Spamming, abuse, ToS violation…"/>
    <div style="display:flex;gap:10px;margin-top:4px">
      <button class="btn" id="banConfirm" style="background:#ef4444;border-color:#ef4444">🔨 Ban</button>
      <button class="btn secondary btn-sm" onclick="closeBanModal()" style="margin-top:0">Cancel</button>
    </div>
  </div>
</div>

<script>
var banTargetId=null;
function showBanModal(id,name){
  banTargetId=id;
  document.getElementById('banModalName').textContent='Banning: '+name;
  document.getElementById('banReason').value='';
  document.getElementById('banModal').style.display='flex';
  setTimeout(function(){document.getElementById('banReason').focus();},50);
}
function closeBanModal(){document.getElementById('banModal').style.display='none';banTargetId=null;}
document.getElementById('banConfirm').addEventListener('click',function(){
  if(!banTargetId)return;
  var reason=document.getElementById('banReason').value.trim();
  doAction(banTargetId,'ban',reason);closeBanModal();
});
function doAction(userId,action,extra){
  if(action==='delete'&&!confirm('Permanently delete this user? This cannot be undone.'))return;
  var f=document.createElement('form');f.method='POST';f.action='/admin/action';
  [['user_id',userId],['action',action],['extra',extra||'']].forEach(function(p){
    var i=document.createElement('input');i.type='hidden';i.name=p[0];i.value=p[1];f.appendChild(i);
  });
  document.body.appendChild(f);f.submit();
}
function filterUsers(q){
  q=q.toLowerCase();
  document.querySelectorAll('.user-row').forEach(function(r){
    r.style.display=r.dataset.name.includes(q)?'':'none';
  });
}
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeBanModal();});
</script>
"""


