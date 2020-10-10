"""Basic application functional test."""
import hamcrest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from fast_admin import FastAdmin, PGConfig


def test_app_instancing():
    """Test basic app functions."""
    app = FastAPI()
    route = '/admin'
    port = 5446
    fast_admin = FastAdmin(
        title='hello world',
        app=app,
        route=route,
        storage_conf=PGConfig(
            host='localhost',
            port=port,
            database='fast_admin',
            username='fast_admin',
            password='fast_admin',
        ),
    )
    fast_admin.configure()
    client = TestClient(app)
    response = client.get(route)
    hamcrest.assert_that(response.text, hamcrest.contains_string('Index page'))
