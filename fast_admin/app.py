"""Basic app instances."""
import abc
from pathlib import PurePath
from typing import Any, Optional, Tuple, Union

from databases import Database
from fastapi import FastAPI
from jinja2 import Template
from pydantic import BaseModel

from fast_admin.di import app_inject_module as inject
from fast_admin.di import configure_container
from fast_admin.urls import register_admin_routers


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
    def get_connection(
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
    def get_connection(
        self,
        host: str,
        port: int,
        username: str,
        password: str,
        db_name: str,
        connection_provider,
    ):
        return connection_provider(host, port, username, password, db_name)


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
    db_provider: Optional[Database]

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
        configure_container(self)
        register_admin_routers(app=self.app, admin_route=self.route)
        self._configure()

    def _configure(self):
        self.db_provider = self.storage_conf.get_connection(
            self.storage_conf.host,
            self.storage_conf.port,
            self.storage_conf.username,
            self.storage_conf.password,
            self.storage_conf.database,
        )
