import psycopg

import click
from flask import current_app, g

# replace me with config file
from dotenv import dotenv_values

env_vals = dotenv_values('.env')

def get_db():
    
    # REMOVE THIS 
    URI = f'{env_vals["DB_TYPE"]}://{env_vals["USER"]}:{env_vals["PASSWORD"]}@' + \
        f'{env_vals["HOST"]}:{env_vals["PORT"]}/{env_vals["DBNAME"]}'    # REMOVE THIS

    if 'db' not in g:
        g.db  = psycopg.connect(URI) # optionally, we could configure the row factory type here
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()