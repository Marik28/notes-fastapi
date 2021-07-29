from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    status,
    Path,
    Response
)

from ..models.notes import Note, NoteCreate, NoteUpdate
from ..models.users import User
from ..services.auth import get_current_user
from ..services.notes import NotesService

router = APIRouter(prefix="/notes")


@router.get("/", response_model=list[Note])
async def get_notes(service: NotesService = Depends(), user: User = Depends(get_current_user)):
    return service.get_list(user)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_note(note_data: NoteCreate, service: NotesService = Depends(), user: User = Depends(get_current_user)):
    # todo сделать header location с полным путем до созданной заметки
    service.create(note_data, user)


@router.put("/{note_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def update_note(note_data: NoteUpdate, note_id: UUID = Path(...), service: NotesService = Depends(),
                      user: User = Depends(get_current_user)):
    service.update(note_id, note_data, user)


@router.get("/{note_id}", response_model=Note)
async def get_note(note_id: UUID = Path(...), service: NotesService = Depends(),
                   user: User = Depends(get_current_user)):
    return service.get(note_id, user)


@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_note(note_id: UUID = Path(...), service: NotesService = Depends(),
                      user: User = Depends(get_current_user)):
    service.delete(note_id, user)
