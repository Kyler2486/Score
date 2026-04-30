import os
from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

AVATAR_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'avatars')
BANNER_DIR  = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'banners')
ALLOWED_IMAGE = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
DB_PATH = 'users.db'

os.makedirs(AVATAR_DIR, exist_ok=True)
os.makedirs(BANNER_DIR, exist_ok=True)


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.secret_key = os.environ.get('SECRET_KEY') or os.urandom(32)
    app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024

    login_manager.login_view = 'auth.landing'
    login_manager.init_app(app)

    from scorelab.routes.auth import auth_bp
    from scorelab.routes.main import main_bp
    from scorelab.routes.extensions_store import ext_store_bp
    from scorelab.routes.extensions import ext_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(ext_store_bp)
    app.register_blueprint(ext_bp)

    return app
