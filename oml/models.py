from app import db


user_list = db.Table('user_list',
    db.Column('u_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('l_id', db.Integer, db.ForeignKey('list.id'), primary_key=True)
)


movie_list = db.Table('movie_list',
    db.Column('m_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('l_id', db.Integer, db.ForeignKey('list.id'), primary_key=True)
)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True)
    genre = db.Column(db.String(50), default='n/a')
    year = db.Column(db.String(4), default='n/a')
    director = db.Column(db.String(100), default='n/a')
    actor = db.Column(db.String(200), default='n/a')
    custom_input = db.Column(db.Boolean, default=False)
    imdb = db.Column(db.String(10), default='n/a')
    score = db.Column(db.Float, default=0)
    plot = db.Column(db.Text, default='n/a')

    def __repr__(self):
        return f'{self.title} ({self.year}) by {self.director}'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def hasList(self, list):
        return self.lists.filter(user_list.c.l_id == list.id).count() == 1

    def addList(self, list):
        if self.hasList(list):
            return
        else:
            self.lists.append(list)

    def removeList(self, list):
        if not self.hasList(list):
            return
        else:
            self.lists.remove(list)


    # def removeList(self, list):

    def __repr__(self):
        return f'<{self.id} {self.name}>'


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(80), nullable=False)
    movie_list = db.relationship('Movie', secondary=movie_list, lazy='dynamic',
        backref=db.backref('lists', lazy='dynamic'))
    user_list = db.relationship('User', secondary=user_list, lazy='dynamic',
        backref=db.backref('lists', lazy='dynamic'))


    def hasMovie(self, movie):
        return self.movie_list.filter(user_list.c.l_id == movie.id).count() == 1

    def addMovie(self, movie):
        if self.hasMovie(movie):
            return
        else:
            self.movie_list.append(movie)

    def removeMovie(self, movie):
        if not self.hasMovie(movie):
            return
        else:
            self.movie_list.remove(movie)

            
    def __repr__(self):
        return f'<{self.id} {self.name}>'

