import os
from dotenv import dotenv_values

basedir = os.path.abspath(os.path.dirname(__file__))
env_vals = dotenv_values('.env')

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = f'{env_vals["DB_TYPE"]}://{env_vals["USER"]}:{env_vals["PASSWORD"]}@' + \
        f'{env_vals["HOST"]}:{env_vals["PORT"]}/{env_vals["DBNAME"]}'
    URI = os.environ.get('URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # app.config['SQLALCHEMY_DATABASE_URI'] = f'{app.config["DB_TYPE"]}://{app.config["USER"]}:{app.config["PASSWORD"]}@{app.config["HOST"]}:{app.config["PORT"]}/{app.config["DBNAME"]}'
