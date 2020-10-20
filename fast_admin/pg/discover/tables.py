"""Base PG schema discovering."""
from typing import List, Mapping, Tuple

from fast_admin.connection_utils import get_connection
from fast_admin.pg.discover.models import ColumnModel

GET_COLUMNS_SQL = """
SELECT
   table_name,
   column_name,
   data_type
FROM
   information_schema.columns
WHERE
   table_name = 'users';
"""


async def get_tables_schema() -> Tuple[ColumnModel, ...]:
    """Get schema for table users."""
    conn = await get_connection()
    table_info: List[Mapping[str, str]] = await conn.fetch_all(
        GET_COLUMNS_SQL,
    )
    await conn.disconnect()
    return tuple(
        ColumnModel(
            table_name=row.get('table_name'),
            column_name=row.get('column_name'),
            data_type=row.get('data_type'),
        ) for row in table_info
    )
