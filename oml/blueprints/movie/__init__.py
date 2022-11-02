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
    movie_data = db.execute('SELECT * FROM movie WHERE id = (%s)', (movie_id,)).fetchone()
    if movie_data is not None:
        return render_template('movie/view_single.html', movie=movie_data, poster='harry_potter.jpg')
    else:
        return '<h1> INVALID ID </h1>'