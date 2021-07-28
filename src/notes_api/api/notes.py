from fastapi import (
    APIRouter,
    Depends,
    status
)

from ..models.notes import Note, NoteCreate
from ..models.users import User
from ..services.auth import get_current_user
from ..services.notes import NotesService

router = APIRouter(prefix="/notes")


@router.get("/", response_model=list[Note])
async def get_notes(service: NotesService = Depends(), user: User = Depends(get_current_user)):
    return service.get_list(user)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(note_data: NoteCreate, service: NotesService = Depends(), user: User = Depends(get_current_user)):
    service.create(user.id, note_data)
