"""Databases common connection utils."""
from databases import Database


async def get_connection(
    driver: str,
    host: str,
    port: int,
    db_name: str,
    username: str,
    password: str,
):
    """Provide postgres async connection."""
    db: Database = Database(
        '{driver}://{username}:{password}@{host}:{port}/{db_name}'.format(
            driver=driver,
            host=host,
            port=port,
            db_name=db_name,
            username=username,
            password=password,
        ),
    )
    await db.connect()
    return db
