import psycopg

import click
from flask import current_app, g


def get_db():
    
    # REMOVE THIS 
    uri = 
    # REMOVE THIS

    if 'db' not in g:
        g.db  = psycopg.connect(uri) # optionally, we could configure the row factory type here
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

