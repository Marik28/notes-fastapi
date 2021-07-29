from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.notes import NoteCreate, NoteUpdate
from ..models.users import User


class NotesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, note_id: UUID, user: User) -> tables.Note:
        note: Optional[tables.Note] = (
            self.session.query(tables.Note)
                .filter(tables.Note.id == note_id)
                .first()
        )

        # todo - если заметка с таким id есть, но у другого пользователя, что делать?
        if note is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        if note.owner_id != user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
        return note

    def get_list(self, user: User) -> list[tables.Note]:
        notes = (
            self.session.query(tables.Note)
                .filter(tables.Note.owner_id == user.id)
                .order_by(tables.Note.date_create.desc())
                .all()
        )
        return notes

    def create(self, note_data: NoteCreate, user: User):
        note = tables.Note(**note_data.dict(), owner_id=user.id)
        self.session.add(note)
        self.session.commit()

    def update(self, note_id: UUID, note_new_data: NoteUpdate, user: User):
        note = self._get(note_id, user)
        for field, value in note_new_data:
            setattr(note, field, value)
        self.session.add(note)
        self.session.commit()

    def get(self, note_id: UUID, user: User):
        return self._get(note_id, user)

    def delete(self, note_id: UUID, user: User):
        note = self._get(note_id, user)
        self.session.delete(note)
        self.session.commit()
