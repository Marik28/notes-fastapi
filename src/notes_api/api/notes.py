from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    status,
    Path,
    Response,
)
from fastapi.responses import JSONResponse

from ..models.notes import Note, NoteCreate, NoteUpdate
from ..models.responses import Message
from ..models.users import User
from ..services.auth import get_current_user
from ..services.notes import NotesService

router = APIRouter(prefix="/notes")


# todo добавить документацию для ответов с кодом UNAUTHORIZED
@router.get(
    "/",
    response_model=list[Note],
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not authenticated",
            "model": Message,
        },
    },
)
async def get_notes(service: NotesService = Depends(), user: User = Depends(get_current_user)):
    return service.get_list(user)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not authenticated",
            "model": Message,
        },
    }
)
async def create_note(note_data: NoteCreate, service: NotesService = Depends(), user: User = Depends(get_current_user)):
    created_note_id = str(service.create(note_data, user))
    created_note_location = router.url_path_for("get_note", note_id=created_note_id)
    return JSONResponse(status_code=status.HTTP_201_CREATED, headers={"Location": created_note_location})


@router.put(
    "/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not authenticated",
            "model": Message,
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Note was not found",
            "model": Message,
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "User does not have access permission to requested note",
            "model": Message,
        }
    }
)
async def update_note(note_data: NoteUpdate, note_id: UUID = Path(...), service: NotesService = Depends(),
                      user: User = Depends(get_current_user)):
    service.update(note_id, note_data, user)


@router.get(
    "/{note_id}",
    response_model=Note,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not authenticated",
            "model": Message,
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Note was not found",
            "model": Message,
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "User does not have access permission to requested note",
            "model": Message,
        }
    }
)
async def get_note(note_id: UUID = Path(...), service: NotesService = Depends(),
                   user: User = Depends(get_current_user)):
    return service.get(note_id, user)


@router.delete(
    "/{note_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "User is not authenticated",
            "model": Message,
        },
        status.HTTP_404_NOT_FOUND: {
            "description": "Note was not found",
            "model": Message,
        },
        status.HTTP_403_FORBIDDEN: {
            "description": "User does not have access permission to requested note",
            "model": Message,
        }
    }
)
async def delete_note(note_id: UUID = Path(...), service: NotesService = Depends(),
                      user: User = Depends(get_current_user)):
    service.delete(note_id, user)
