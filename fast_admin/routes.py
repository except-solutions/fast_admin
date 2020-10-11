"""Main application routes."""
from fastapi import APIRouter

router: APIRouter = APIRouter()


@router.get('/')
async def index() -> str:
    """Admin panel dashboard index page."""
    return 'Index page'
