"""Map table data methods."""
from itertools import groupby
from typing import Dict, Generator, Tuple

from fast_admin.pg.discover.models import ColumnModel


def group_tables_meta(
    tables_meta: Generator[ColumnModel, None, None],
) -> Dict[str, Tuple[ColumnModel, ...]]:
    """Group tables meta by tables name."""
    return {
        table_name: tuple(table_meta)
        for table_name, table_meta in groupby(
            tables_meta,
            key=lambda table: table.table_name,
        )
    }
