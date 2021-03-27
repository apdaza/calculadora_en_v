import pytest

from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def Cliente(app):
    return app.test_cliente()