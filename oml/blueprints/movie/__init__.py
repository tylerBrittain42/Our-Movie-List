from flask import Blueprint, g, render_template
from oml.blueprints.auth import login_required
from oml.db import get_db

bp = Blueprint('movie', __name__, url_prefix='/movie', template_folder='templates')

@bp.route("/")
@login_required
def index():
    return '<h1>movie index (temp)</h1>'

@bp.get('/<movie_id>')
@login_required
def indiv_movie(movie_id):
    
    # getting movie info
    db = get_db()
    movie_data = db.execute('SELECT * FROM movie WHERE id = (%s);', (movie_id,)).fetchone()
    if movie_data is not None:
        return render_template('movie/view_single.html', movie=movie_data, poster='harry_potter.jpg')
    else:
        return '<h1> INVALID ID </h1>'

@bp.get('/all/<page>')
@login_required
def browse_all(page):

    offset_value = int(page) * 10
    PAGE_SIZE = 10

    db = get_db()
    movie_list = db.execute('''SELECT id, title, year FROM movie 
                               ORDER BY id 
                               ASC OFFSET (%s) 
                               LIMIT (%s);''', (offset_value, PAGE_SIZE)).fetchall()

    return render_template('movie/view_all.html', movie_list=movie_list, poster='harry_potter.jpg')