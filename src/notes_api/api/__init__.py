from fastapi import APIRouter

from . import notes
from . import auth

router = APIRouter()
router.include_router(notes.router)
router.include_router(auth.router)
