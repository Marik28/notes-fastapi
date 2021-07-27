from fastapi import APIRouter

router = APIRouter(prefix="/notes")


@router.get("/")
async def get_notes():
    ...
