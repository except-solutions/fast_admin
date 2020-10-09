"""Basic app instances."""
import abc

from fastapi import FastAPI
from pydantic import BaseModel


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Config:
        arbitrary_types_allowed = True
