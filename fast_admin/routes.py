"""Main application routes."""
import inject
from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.templating import _TemplateResponse as TemplateResponse  # noqa: WPS450

from fast_admin import FastAdmin

router: APIRouter = APIRouter()


@router.get('/', response_class=HTMLResponse)
async def index(request: Request) -> TemplateResponse:
    """Admin panel dashboard index page."""
    fast_admin: FastAdmin = inject.instance('fast_admin')  # type: ignore
    templates: Jinja2Templates = Jinja2Templates(
        directory=str(fast_admin.app_route / 'templates'),
    )
    return templates.TemplateResponse(
        'index.jinja2',
        {
            'request': request,
            'title': fast_admin.title,
        },
    )
