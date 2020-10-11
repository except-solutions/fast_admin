"""DI configuration module."""
import inject

from fast_admin.connection_utils import get_connection


def configure_pg_connection(*args, **kwargs):
    """Configure pg connection instance."""
    return get_connection('postgresql', *args, **kwargs)


def di_config(binder: inject.Binder) -> None:
    """Add container bindings."""
    binder.bind('pg_connection_provider', configure_pg_connection)


inject.configure(di_config)

app_inject_module = inject
