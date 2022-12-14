# from config import Config
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app,db)

# from app import routes, models

import os
from flask import Flask, g
from config import Config

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.url_map.strict_slashes = False # REMOVE ME LATER
    
    if test_config is None:
        app.config.from_object(Config)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        print('in except OSerror')
        pass


    from . import db
    db.init_app(app)

    from .blueprints import auth
    app.register_blueprint(auth.bp)

    from .blueprints import movie
    app.register_blueprint(movie.bp)

    # example blueprint showing how to create 'main' blueprint
    # from . import tst_bp
    # app.register_blueprint(tst_bp.bp)

    @app.route('/')
    def index():
        g.a = 'qwe'
        print(g.a)
        return 'it works'

    return app