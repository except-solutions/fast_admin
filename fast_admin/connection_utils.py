"""Databases common connection utils."""
import inject
from databases import Database


def get_db_provired(
    driver: str,
    host: str,
    port: int,
    db_name: str,
    username: str,
    password: str,
):
    """Provide postgres async connection."""
    return Database(
        '{driver}://{username}:{password}@{host}:{port}/{db_name}'.format(
            driver=driver,
            host=host,
            port=port,
            db_name=db_name,
            username=username,
            password=password,
        ),
    )


async def get_connection() -> Database:
    """Return establish connection."""
    conn: Database = inject.instance('fast_admin').db_provider  # type: ignore
    await conn.connect()
    return conn
