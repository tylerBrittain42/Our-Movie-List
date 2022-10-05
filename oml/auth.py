import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from oml.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM users WHERE id = (%s)', (user_id,)).fetchone()

@bp.post('/register')
def register_post():
    print('register post start')
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    error = None

    if not username:
        error = 'username is required'
    elif not password:
        error = 'password is required'
    
    if error is None:
        try:
            db.execute("""
                INSERT INTO USERS (name, password)
                VALUES(%s, %s)
                """, (username, generate_password_hash(password)))
            db.commit()
        except db.IntegrityError:
            error = f'User {username} is already registered'
            print(error)
        except Exception as e:
            print(e)
        else:
            return redirect(url_for('auth.login_get'))
    
    flash(error)
    return render_template('auth/register.html')

@bp.get('/register')
def register_get():
    return render_template('auth/register.html')


@bp.post('/login')
def login_post():
    db = get_db()
    username = request.form['username']
    password = request.form['password']
    error = None

    with db.cursor() as cur:
        cur.execute("""
            SELECT *
            FROM users
            WHERE name = (%s)
            """, (username,))
        user = cur.fetchone()
    
    if user is None:
        error = 'Incorrect username'
    elif not check_password_hash(user['password'],password):
        error = 'Incorrect password'
    
    if error is None:
        session.clear()
        session['user_id'] = user['id']

        return redirect(url_for('index'))

    flash(error)
    return render_template('auth/login.html')

@bp.get('/login')
def login_get():
    return render_template('auth/login.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login_get'))

        return view(**kwargs)

    return wrapped_view