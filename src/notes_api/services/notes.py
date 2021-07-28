from fastapi import Depends
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.notes import NoteCreate
from ..models.users import User


class NotesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self, user: User) -> list[tables.Note]:
        notes = (
            self.session
                .query(tables.Note)
                .filter(tables.Note.owner_id == user.id)
                .order_by(tables.Note.date_create.desc())
                .all()
        )
        return notes

    def create(self, user: User, note_data: NoteCreate):
        note = tables.Note(**note_data.dict(), owner_id=user.id)
        self.session.add(note)
        self.session.commit()
