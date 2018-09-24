import pytest
import requests
import six

import main

@pytest.fixture
def app():
    main.app.testing = True
    client = main.app.test_client()
    return client


def test_index(app):
    r = app.get('/')
    assert r.status_code == 200
