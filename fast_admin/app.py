"""Basic app instances."""
import abc
from pathlib import PurePath
from typing import Any, Tuple, Union

from fastapi import FastAPI
from jinja2 import Template
from pydantic import BaseModel

from fast_admin.di import app_inject_module as inject
from fast_admin.di import configure_container


class StorageResource(BaseModel, abc.ABC):
    """Abstract storage resource: table, model, document etc."""


class StorageConfig(BaseModel, abc.ABC):
    """Abstract storage config."""

    host: str
    port: int
    database: str
    username: str
    password: str
    resources: Tuple[StorageResource, ...]

    @abc.abstractmethod
    async def get_connection(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        db_name: str,
        *,
        connection_provider,
    ) -> Any:
        """Provide storage connection."""


class PGConfig(StorageConfig):
    """Postgres config."""

    @inject.params(connection_provider='pg_connection_provider')
    async def get_connection(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        db_name: str,
        connection_provider,
    ):
        return await connection_provider(host, port, username, password, db_name)


class PGResource(StorageResource):
    """Postgres table config."""

    table_name: str


class FastAdmin(BaseModel):
    """Admin application instance."""

    title: str
    route: str
    app: FastAPI
    storage_conf: StorageConfig
    app_route: PurePath = PurePath(__file__).parent
    index_template: Union[Template, str] = 'index.jinja2'

    class Config:  # noqa: WPS431
        """Pydantic model meta."""

        arbitrary_types_allowed: bool = True

    def configure(self) -> None:
        """
        Configure application.

        - Init container
        - Add routes
        - Check storage connections
        """
        from fast_admin.routes import router  # noqa: WPS433

        configure_container(self)
        self.app.include_router(
            router,
            prefix=self.route,
        )
