"""Base realisation getting table schemas."""
from typing import Dict, Tuple

from fastapi import APIRouter

from fast_admin.admin.api_models import StorageSchema
from fast_admin.pg.discover.models import ColumnModel
from fast_admin.pg.discover.tables import get_tables_schema

router: APIRouter = APIRouter()


@router.get('/schema', response_model=StorageSchema)
async def get_database_schema() -> StorageSchema:
    """Get tables schema route."""
    table_schema: Dict[str, Tuple[ColumnModel, ...]] = await get_tables_schema()
    return StorageSchema(resources=table_schema)
