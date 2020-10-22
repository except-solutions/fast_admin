"""Register all app urls."""
from typing import Tuple

from fastapi import APIRouter, FastAPI


def get_admin_routers() -> Tuple[APIRouter, ...]:
    """Import and return all admin-app routers."""
    from fast_admin.routes import router as index_route  # noqa: WPS433
    from fast_admin.admin.view.get_schema import router as schema_route  # noqa: WPS433
    return index_route, schema_route


def register_admin_routers(app: FastAPI, admin_route: str) -> None:
    """Register admin-app routers in FastApi."""
    routers = get_admin_routers()
    for route in routers:
        app.include_router(
            route,
            prefix=admin_route,
        )
