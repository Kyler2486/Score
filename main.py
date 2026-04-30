from scorelab.app import create_app
from scorelab.models import init_db
import scorelab.models  # registers @login_manager.user_loader

app = create_app()

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)
