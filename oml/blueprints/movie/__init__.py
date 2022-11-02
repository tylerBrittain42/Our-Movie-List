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
            'id':1,
            'poster':'harry_potter.jpg',
            'title':'Harry Potter and the Deathly Hallows',
            'year':2014,
            'genre':'Fantasy',
            'rating':'3/10',
            'added_by':'Bryanna',
            'director':'Joe Mama',
            'actor':'danny boi, emma watson',
            'synopsis':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus rhoncus dui urna, et iaculis odio ultrices et. Integer vel euismod sem. Etiam sed sapien sit amet massa blandit sollicitudin. In hac habitasse platea dictumst. Mauris pulvinar aliquet mauris, id egestas ante faucibus ac. Pellentesque eget erat venenatis nisi ultricies feugiat. ',
            'imdb':'tt0926084'
        }
    return render_template('movie/view_single.html', movie=a)