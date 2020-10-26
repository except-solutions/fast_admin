"""Common format sql methods."""
from typing import Any, Sequence


def join_sequence_with_coma(values_to_join: Sequence[Any]) -> str:
    """Join values in coma separated string."""
    return ', '.join("'{0}'".format(value_to_join) for value_to_join in values_to_join)
