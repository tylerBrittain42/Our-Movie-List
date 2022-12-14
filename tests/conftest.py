import os
import tempfile
import pytest
from oml import create_app
from oml.db import get_db, init_db

with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
    _data_sql = f.read().decode('utf8')


@pytest.fixture
def app():
    # db_fd, db_path = tempfile.mkstemp()

    app = create_app({
        'TESTING': True,
        'URI': 'postgresql://tyler:pass@127.0.0.1:5432/oml_test',
        'SECRET_KEY':'aggdhjwqewqeasdwea'
    })

    with app.app_context():
        init_db()
        get_db().execute(_data_sql)
        get_db().commit()

    yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)