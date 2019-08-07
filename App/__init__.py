import functools
import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_login import LoginManager, current_user
from flask_socketio import SocketIO

# ===================================================================
#                          instantiate app
# ===================================================================
app = Flask(__name__)
app.config.from_object('Config.config.DevelopmentConfig')
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
mail = Mail(app)
socketio = SocketIO(app)


# ===================================================================
#                       flask-login settings
# ===================================================================
login_manager = LoginManager()
login_manager.login_view = 'auth.login'  # route to login page
login_manager.session_protection = "strong"
login_manager.init_app(app)


# ===================================================================
#                       File upload directories
# ===================================================================
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPOLAD_DIRECTORY = os.path.join(APP_ROOT, "static/uploads/")
AVATAR_UPOLAD_DIRECTORY = os.path.join(UPOLAD_DIRECTORY, "avatars/")
if not os.path.isdir(AVATAR_UPOLAD_DIRECTORY):
    os.mkdir(AVATAR_UPOLAD_DIRECTORY)




# ============================================================
#           restricting views through permissions
# ============================================================
def permission_required(permission_names):
    def decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            go_back_url = request.referrer
            result = f(*args, **kwargs)
            from Models.models import User
            if User.query.count() <= 1:
                return result
            for p in permission_names:
                if current_user.has_permission(p):
                    return result
            return render_template("403.html.jinja2", go_back_url=go_back_url)
        return wrapped
    return decorator





# ============================================================================
#       passing settings variable to templates through Context_Processor
# ============================================================================
from Models.models import Settings
@app.context_processor
def settings_context_processor():
    if Settings.query.count() < 1:
        website_settings = Settings(website_name="Set Website Name", website_title="Set Website Title")
        db.session.add(website_settings)
        db.session.commit()
    website_settings = Settings.query.first()
    return dict(website_settings=website_settings)





# ===================================================================
#                 import & register View blueprints
# ===================================================================
from App.auth.views.auth_views import auth_views_module
app.register_blueprint(auth_views_module)

from App.site.views.site_index_views import site_index_views_module
app.register_blueprint(site_index_views_module)


