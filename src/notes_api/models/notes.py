import datetime as dt
from uuid import UUID

from pydantic import BaseModel, Field

from ..settings import settings


class BaseNote(BaseModel):
    title: str = Field(..., max_length=settings.max_note_title_length, title="Текст заметки")
    text: str = Field(..., max_length=settings.max_note_text_length, title="Текст заметки")


class Note(BaseNote):
    id: UUID
    date_create: dt.datetime = Field(..., title="Время создания заметки. Unix timestamp")
    date_update: dt.datetime = Field(..., title="Время последнего обновления заметки. Unix timestamp")

    class Config:
        orm_mode = True


class NoteCreate(BaseNote):
    pass


class NoteUpdate(BaseNote):
    pass
