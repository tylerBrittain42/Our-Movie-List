from email.policy import default
from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), index=True, unique=True)
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