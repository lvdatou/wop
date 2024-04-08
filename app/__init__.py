from flask import Flask
# from flask_babelex import Babel # test

from . import blog
from . exts import db,migrate,bootstrap
from . import auth
from . import settings
from . exts import login_manager



def create_app():
    wop = Flask(__name__)
    # babel = Babel(wop)
    bootstrap.init_app(wop)
    login_manager.init_app(wop)

    wop.config.from_object(settings.Default)
    wop.config['BABEL_DEFALUT_LOCALE']='en'

    wop.register_blueprint(blog.bp)
    wop.register_blueprint(auth.bp)

    db.init_app(wop)
    migrate.init_app(wop,db)

    return wop

