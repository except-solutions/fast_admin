"""Basic application functional test."""
import hamcrest
import pytest
from fastapi import FastAPI
from httpx import AsyncClient

from fast_admin import FastAdmin, PGConfig, PGResource


@pytest.mark.asyncio
async def test_app_instancing():
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
            resources=(PGResource(table_name='users'),),
        ),
    )
    fast_admin.configure()
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.get(route)
        hamcrest.assert_that(response.text, hamcrest.contains_string('Index page'))
