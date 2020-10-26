"""Format tables sql module."""
from fast_admin.sql_utils import join_sequence_with_coma


def select_tables_meta(tables):
    """Select tables metadata."""
    return """
        SELECT
           table_name,
           column_name,
           data_type
        FROM
           information_schema.columns
        WHERE
           table_name IN ({tables})
    """.format(tables=join_sequence_with_coma(tables))  # noqa: S608
