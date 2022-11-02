import click
import psycopg
from psycopg.rows import dict_row
from flask import current_app, g
# replace me with config file
from dotenv import dotenv_values
# replace me with config file


env_vals = dotenv_values('.env')


def get_db():
    

    # URI = current_app
    if 'db' not in g:
        URI = current_app.config["URI"]
        g.db  = psycopg.connect(URI, row_factory=dict_row) # optionally, we could configure the row factory type here
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
    


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.execute(f.read().decode('utf8'))
        db.commit()

def load_db():
    db = get_db()
    with current_app.open_resource('sample_movie.csv') as f:
        with db.cursor().copy("COPY movie (title, genre, plot, director,actor,year,score) FROM STDIN WITH (FORMAT CSV)" ) as copy:
         while data := f.read(1000):
            copy.write(data)
        db.commit()

@click.command("init-db")
def init_db_command():
    """Clear existing DB and create new tables"""
    init_db()
    click.echo("Initialized the database")

    # load sample data
    load_db()
    click.echo("Loaded the database")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
