"""Base realisation getting table schemas."""
from typing import List, Tuple

from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from fast_admin.pg.discover.models import ColumnModel
from fast_admin.pg.discover.tables import get_tables_schema

router: APIRouter = APIRouter()


@router.get('/schema', response_model=List[ColumnModel])
async def get_database_schema() -> JSONResponse:
    """Get tables schema route."""
    table_schema: Tuple[ColumnModel, ...] = await get_tables_schema()
    return JSONResponse(jsonable_encoder(table_schema))
