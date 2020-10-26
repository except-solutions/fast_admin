"""Base configuration and initialization fast_admin instance."""

import logging
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from jinja2 import Environment, FileSystemLoader

from fast_admin import FastAdmin, PGConfig, PGResource

logger = logging.getLogger(__name__)


def init_app() -> FastAPI:
    """Init test app with fast_admin."""
    file_loader = FileSystemLoader(os.path.dirname(__file__))
    env = Environment(loader=file_loader)

    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    fast_admin = FastAdmin(
        title='Fast Admin',
        app=app,
        route='/admin',
        index_template=env.get_template('index.jinja2'),
        storage_conf=PGConfig(  # noqa: S106 hard-code TODO: settings
            host='localhost',
            port=5432,  # noqa: WPS432 magic-number TODO: settings
            database='fast_admin',
            username='fast_admin',
            password='fast_admin',  # noqa: S106 hard-code TODO: settings
            resources=(
                PGResource(table_name='users'),
                PGResource(table_name='items'),
            ),
        ),
    )

    fast_admin.configure()

    logger.warning('Fast admin configured! \n{fast_admin}'.format(fast_admin=fast_admin))
    return app
