import sqlite3
from flask import Blueprint, request, render_template_string, redirect, url_for
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from scorelab.models import get_db, User
from scorelab.templates.tools_content import AUTH_TEMPLATE
from scorelab.templates.extensions_content import LANDING_TEMPLATE

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('main.index'))
    messages, form = [], {'email': '', 'username': '', 'display_name': ''}
    if request.method == 'POST':
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', ''); form['email'] = email
        with get_db() as conn:
            row = conn.execute('SELECT * FROM users WHERE email=?', (email,)).fetchone()
        if row and check_password_hash(row['password'], password):
            login_user(User(row['id'], row['email'], row['username'], row['display_name'],
                            row['avatar'], row['banner']))
            return redirect(url_for('main.index'))
        messages.append(('Invalid email or password.', 'error'))
    return render_template_string(AUTH_TEMPLATE, title='Log In', subtitle='Welcome back',
        show_register=False, btn='Log In',
        footer_text='Don\'t have an account? <a href="/register">Sign up</a>',
        messages=messages, form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated: return redirect(url_for('main.index'))
    messages, form = [], {'email': '', 'username': '', 'display_name': ''}
    if request.method == 'POST':
        dn = request.form.get('display_name', '').strip()
        un = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip().lower()
        pw = request.form.get('password', '')
        form = {'email': email, 'username': un, 'display_name': dn}
        if not all([dn, un, email, pw]):
            messages.append(('All fields are required.', 'error'))
        elif len(pw) < 6:
            messages.append(('Password must be at least 6 characters.', 'error'))
        else:
            try:
                with get_db() as conn:
                    conn.execute(
                        'INSERT INTO users (email,username,display_name,password) VALUES(?,?,?,?)',
                        (email, un, dn, generate_password_hash(pw)))
                    conn.commit()
                return render_template_string(AUTH_TEMPLATE, title='Log In', subtitle='Welcome back',
                    show_register=False, btn='Log In',
                    footer_text='Don\'t have an account? <a href="/register">Sign up</a>',
                    messages=[('Account created! Please log in.', 'success')],
                    form={'email': email, 'username': '', 'display_name': ''})
            except sqlite3.IntegrityError as e:
                err = str(e)
                if 'username' in err:   messages.append(('That username is already taken.', 'error'))
                elif 'email' in err:    messages.append(('An account with that email already exists.', 'error'))
                else:                   messages.append(('Registration failed.', 'error'))
    return render_template_string(AUTH_TEMPLATE, title='Sign Up', subtitle='Create your account',
        show_register=True, btn='Create Account',
        footer_text='Already have an account? <a href="/login">Log in</a>',
        messages=messages, form=form)


@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth_bp.route('/landing')
def landing():
    if current_user.is_authenticated: return redirect(url_for('main.index'))
    return render_template_string(LANDING_TEMPLATE)
