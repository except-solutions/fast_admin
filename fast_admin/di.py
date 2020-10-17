"""DI configuration module."""
import inject

from fast_admin.connection_utils import get_connection


def configure_pg_connection(*args, **kwargs):
    """Configure pg connection instance."""
    return get_connection('postgresql', *args, **kwargs)


def configure_container(fast_admin):
    """Configure inject function."""
    def di_config(binder: inject.Binder) -> None:  # noqa: WPS430
        """Add container bindings."""
        binder.bind('fast_admin', fast_admin)
        binder.bind('pg_connection_provider', configure_pg_connection)
    inject.configure(di_config)


app_inject_module = inject
