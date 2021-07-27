import datetime as dt
from uuid import uuid4

from pydantic import BaseModel, Field

from ..settings import settings


class BaseNote(BaseModel):
    title: str = Field(..., max_length=settings.max_note_title_length, title="Текст заметки")
    text: str = Field(..., max_length=settings.max_note_text_length, title="Текст заметки")


class Note(BaseNote):
    id: uuid4
    date_create: dt.time = Field(..., title="Время создания заметки")
    date_update: dt.time = Field(..., title="Время последнего обновления заметки")

    class Config:
        orm_mode = True


class NoteCreate(BaseNote):
    pass


class NoteUpdate(BaseNote):
    pass
