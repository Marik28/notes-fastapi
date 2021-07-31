import uvicorn

from .settings import settings

uvicorn.run(
    "notes_api.app:app",
    debug=settings.debug,
)
