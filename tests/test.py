import pytest
from url_shortener import create_app
from flask import url_for


@pytest.fixture
def app():
    app = create_app()
    return app

@pytest.fixture
def client(app):
    with app.test_client() as c:
        yield c

@pytest.fixture
def res(client):
    return client.get('/')

def test_url_shortener(res):
    assert res.status_code == 200