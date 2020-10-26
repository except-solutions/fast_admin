"""Base PG schema discovering."""
from typing import Dict, List, Mapping, Tuple

import inject
from databases import Database

from fast_admin import PGResource
from fast_admin.connection_utils import get_connection
from fast_admin.pg.discover.map_utils import group_tables_meta
from fast_admin.pg.discover.models import ColumnModel
from fast_admin.pg.discover.sql_utils import select_tables_meta


async def get_tables_schema() -> Dict[str, Tuple[ColumnModel, ...]]:
    """Get schema for table users."""
    conn: Database = await get_connection()
    resources: Tuple[PGResource] = (
        inject.instance('fast_admin').storage_conf.resources  # type: ignore
    )
    tables_meta: List[Mapping[str, str]] = await conn.fetch_all(
        select_tables_meta(resource.table_name for resource in resources),
    )

    await conn.disconnect()
    return group_tables_meta(
        ColumnModel(
            table_name=row.get('table_name'),
            column_name=row.get('column_name'),
            data_type=row.get('data_type'),
        ) for row in tables_meta
    )
