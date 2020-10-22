"""Admin api models."""
from typing import Any, Dict

from pydantic import BaseModel


class StorageSchema(BaseModel):
    """Describe resource schema."""

    storage_type: str = 'pg'
    resources: Dict[str, Any]
