from flask import Blueprint
from flask_login import login_required
from scorelab.templates.shell import make_shell, nav_ctx
from scorelab.templates.extensions_content import EXTENSIONS_CSS, EXTENSIONS_CONTENT

ext_store_bp = Blueprint('ext_store', __name__)

@ext_store_bp.route('/extensions')
@login_required
def extensions():
    return make_shell(EXTENSIONS_CONTENT, extra_css=EXTENSIONS_CSS, **nav_ctx())
