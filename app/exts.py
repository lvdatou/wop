from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap5()