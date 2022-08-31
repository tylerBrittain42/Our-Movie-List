
from re import A
from flask import render_template
from app import app



@app.route('/')
def index():
    sample_movies = [
        {
            'rank':1,
            'ico':'ico',
            'title':'Get Smart',
            'genre':'Comedy',
            'rating':'8.5/10',
            'added_by':'Tyler'
        },
        {
            'rank':2,
            'ico':'ico',
            'title':'Harry Potter and the Deathly HAllows',
            'genre':'Fantasy',
            'rating':'3/10',
            'added_by':'Bryanna'
        }
    ]
    return render_template('view_list.html', movies=sample_movies)


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/view/<int:id>')
def view_single(id=0):
    if id == 0:
        return '<h1> Error! </br> Invalid ID </h1>'
    else:
        sample = {
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
    return render_template('view_single.html', movie=sample)


@app.route('/add')
def add_single():
    return render_template('add_single.html')