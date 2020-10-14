"""Base configuration and initialization fast_admin instance."""

import logging
from typing import Optional

from fastapi import FastAPI

from fast_admin import FastAdmin, PGConfig, PGResource

logger = logging.getLogger(__name__)

app = FastAPI()


def init_app() -> FastAPI:
    """Init test app with fast_admin."""
    fast_admin = FastAdmin(
        title='hello world',
        app=app,
        route='/admin',
        storage_conf=PGConfig(  # noqa: S106 hard-code TODO: settings
            host='localhost',
            port=5446,  # noqa: WPS432 magic-number TODO: settings
            database='fast_admin',
            username='fast_admin',
            password='fast_admin',  # noqa: S106 hard-code TODO: settings
            resources=(
                PGResource(table_name='users'),
            ),
        ),
    )

    fast_admin.configure()

    logger.warning('Fast admin configured! \n{fast_admin}'.format(fast_admin=fast_admin))
    return app


@app.get('/')
def read_root():
    """read_root."""
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, query: Optional[str] = None):
    """read_item."""
    return {'item_id': item_id, 'q': query}
