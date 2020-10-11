"""Basic app instances."""
import abc
from typing import Any, Tuple

from fastapi import FastAPI
from pydantic import BaseModel

from fast_admin.di import app_inject_module as inject
from fast_admin.routes import router


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

    class Config:  # noqa: WPS431
        """Pydantic model meta."""

        arbitrary_types_allowed: bool = True

    def configure(self) -> None:
        """
        Configure application.

        - Add routes
        - Check storage connections
        """
        self.app.include_router(
            router,
            prefix=self.route,
        )

        self._configure().send(None)

    async def _configure(self):
        await self.storage_conf.get_connection(
            self.storage_conf.host,
            self.storage_conf.port,
            self.storage_conf.username,
            self.storage_conf.password,
            self.storage_conf.database,
        )
