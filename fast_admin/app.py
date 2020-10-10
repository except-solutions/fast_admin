"""Basic app instances."""
import abc

from fastapi import FastAPI
from pydantic import BaseModel

from fast_admin.routes import router


class StorageConfig(BaseModel, abc.ABC):
    """Abstract storage config."""

    host: str
    port: int
    database: str
    username: str
    password: str


class PGConfig(StorageConfig):
    """Postgres config."""


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
        self.app.include_router(
            router,
            prefix=self.route,
        )
