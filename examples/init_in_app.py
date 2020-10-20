"""Base configuration and initialization fast_admin instance."""

import logging
import os
from typing import Optional

from fastapi import FastAPI
from jinja2 import Environment, FileSystemLoader

from fast_admin import FastAdmin, PGConfig, PGResource

logger = logging.getLogger(__name__)

app = FastAPI()


def init_app() -> FastAPI:
    """Init test app with fast_admin."""
    file_loader = FileSystemLoader(os.path.dirname(__file__))
    env = Environment(loader=file_loader)

    fast_admin = FastAdmin(
        title='hello world',
        app=app,
        route='/admin',
        index_template=env.get_template('index.jinja2'),
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
