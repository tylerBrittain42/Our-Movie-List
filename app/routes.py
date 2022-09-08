
from logging import error
from re import A
from flask import render_template
from app import app, db
from app.models import Movie, List, User
import csv



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


@app.route('/reset4321')
def reset_db():

    return 200

@app.route('/c')
def testing_db():

    import_csv('sample_movie.csv',Movie)
    # import_csv('sample_list',List)
    # import_csv('sample_user',User)
    return 'a'
       
        

def import_csv(file_name, obj):
    """Import a csv to a database, provided that the csv maps to the model
    """

    # Deleting existing records
    try:
        print()
        print(f'Import CSV {file_name}')
        print('*' * 40)
        
        num_deleted = db.session.query(obj).delete()
        print(f'{num_deleted} {obj} records deleted')

        with open(f'./db_scripts/{file_name}', 'r') as f:
            row_count = 0
            reader = csv.reader(f)
            header = next(reader)
            for i in reader:
                row_count += 1
                kwargs = {column: value for column, value in zip(header, i)}
                obj_instance = obj(**kwargs)
                db.session.add(obj_instance)
            print(f'added {row_count} entries from {file_name}')
            db.session.commit()
    except Exception as e:
        print('ERROR')
        print(e)
        print('Reverting database changes')
        db.session.rollback()
    else:
        print(f'\nSUCCESS!!! {file_name} has been imported\n')
    
    return


    # with open('./db_scripts/sample_movie.csv', 'r') as csv_file:
    #     header = f.readline().rstrip("\n").split(',')

    #     attribute_dict = {}
    #     for index, attr in enumerate(header):
    #         attribute_dict[index] = attr

    #     print(attribute_dict)

    #     for line in f:
    #         movie = Movie()

    #         set_obj_attr(movie, attribute_dict, line)
    #         print(movie.id)
    #         # loop to iterate through dict here
    #         #  use set attr for each key value and update movie
    #         # add movie to session
    #         # commit after loop
    
    #         break

    #     # use setattr to set attributes with dictionary
    #     # print(header)
    # return 'hi'

