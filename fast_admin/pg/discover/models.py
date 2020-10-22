"""Pydantic models for PG results."""

from pydantic import BaseModel


class ColumnModel(BaseModel):
    """Model for fetched table."""

    table_name: str
    column_name: str
    data_type: str
