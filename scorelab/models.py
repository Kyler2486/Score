import os, sqlite3
from flask import session
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from scorelab.app import login_manager, DB_PATH


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    with get_db() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL, username TEXT UNIQUE NOT NULL,
            display_name TEXT NOT NULL, password TEXT NOT NULL,
            avatar TEXT, banner TEXT)''')
        cols = [r[1] for r in conn.execute("PRAGMA table_info(users)").fetchall()]
        for col, defn in [('display_name', "TEXT NOT NULL DEFAULT ''"),
                          ('avatar', 'TEXT'), ('banner', 'TEXT'),
                          ('is_admin', "INTEGER NOT NULL DEFAULT 0"),
                          ('is_banned', "INTEGER NOT NULL DEFAULT 0"),
                          ('ban_reason', "TEXT DEFAULT NULL")]:
            if col not in cols:
                conn.execute(f"ALTER TABLE users ADD COLUMN {col} {defn}")
        conn.execute('''CREATE TABLE IF NOT EXISTS metronome_presets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            name TEXT NOT NULL,
            bpm INTEGER NOT NULL,
            time_sig INTEGER NOT NULL DEFAULT 4,
            sound TEXT NOT NULL DEFAULT 'click',
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id))''')
        conn.commit()
    seed_admin()


def seed_admin():
    email    = os.environ.get('ADMIN_EMAIL')
    username = os.environ.get('ADMIN_USERNAME')
    display  = os.environ.get('ADMIN_DISPLAY', username)
    password = os.environ.get('ADMIN_PASSWORD')
    if not email or not password:
        return
    with get_db() as conn:
        row = conn.execute('SELECT id FROM users WHERE email=?', (email,)).fetchone()
        if not row:
            conn.execute(
                'INSERT INTO users (email,username,display_name,password,is_admin) VALUES(?,?,?,?,1)',
                (email, username or email, display or email, generate_password_hash(password)))
        else:
            if username:
                conn.execute('UPDATE users SET username=?,display_name=?,is_admin=1 WHERE email=?',
                             (username, display or username, email))
            conn.execute('UPDATE users SET is_admin=1 WHERE email=?', (email,))
        conn.commit()


class User(UserMixin):
    def __init__(self, id, email, username, display_name,
                 avatar=None, banner=None, is_admin=0, is_banned=0, ban_reason=None):
        self.id = id; self.email = email; self.username = username
        self.display_name = display_name; self.avatar = avatar; self.banner = banner
        self.is_admin = bool(is_admin); self.is_banned = bool(is_banned)
        self.ban_reason = ban_reason

    @property
    def avatar_url(self): return f'/static/avatars/{self.avatar}' if self.avatar else None
    @property
    def banner_url(self): return f'/static/banners/{self.banner}' if self.banner else None


@login_manager.user_loader
def load_user(user_id):
    with get_db() as conn:
        r = conn.execute('SELECT * FROM users WHERE id=?', (user_id,)).fetchone()
    if not r: return None
    keys = r.keys()
    return User(r['id'], r['email'], r['username'], r['display_name'],
                r['avatar'], r['banner'],
                r['is_admin']    if 'is_admin'    in keys else 0,
                r['is_banned']   if 'is_banned'   in keys else 0,
                r['ban_reason']  if 'ban_reason'  in keys else None)


def is_admin_user():
    return current_user.is_authenticated and current_user.is_admin


def reload_current_user():
    return load_user(current_user.id)


def push_msg(cat, text):
    m = session.get('profile_msgs', [])
    m.append((text, cat))
    session['profile_msgs'] = m


def pop_msgs():
    return session.pop('profile_msgs', [])
