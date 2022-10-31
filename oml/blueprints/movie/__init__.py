from flask import Blueprint, g, render_template
from oml.blueprints.auth import login_required

bp = Blueprint('movie', __name__, url_prefix='/movie', template_folder='templates')

@bp.route("/")
@login_required
def index():
    return '<h1>movie index (temp)</h1>'

@bp.get('/<movie_title>')
def indiv_movie(movie_title):
    
    a = {
        'title': 'title',
        'year':'123',
        'rating':'asd',
        'genre':'asd',
        'director':'asd',
        'actor':'asd',
        'synopsis':'asd',
        'poster':'a'


    }
    return render_template('movie/view_single.html', movie=a)