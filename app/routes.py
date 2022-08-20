from re import A
from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def search():
    return render_template('search.html')


@app.route('/view')
def view_single():
    return render_template('view_single.html')


@app.route('/add')
def add_single():
    return render_template('add_single.html')