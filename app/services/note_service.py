from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.note import Note
from app.models.user import User
from app.schemas.note import(NoteCreate, NoteUpdate)


def create_note(
    note: NoteCreate,
    db: Session,
    current_user: User
):
    new_note = Note(
        title=note.title,
        content=note.content,
        user_id=current_user.id
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)

    return new_note

def get_notes(
    db: Session,
    current_user: User
):
    return (
        db.query(Note)
        .filter(
            Note.user_id == current_user.id
        )
        .all()
    )

def get_note(
    note_id: int,
    db: Session,
    current_user: User
):
    note = (
        db.query(Note)
        .filter(
            Note.id == note_id,
            Note.user_id == current_user.id
        )
        .first()
    )

    if note is None:
        raise HTTPException(
            status_code=404,
            detail="Note not found"
        )

    return note


def update_note(
    note_id: int,
    note_data: NoteUpdate,
    db: Session,
    current_user: User
):
    note = get_note(
        note_id,
        db,
        current_user
    )

    note.title = note_data.title
    note.content = note_data.content

    db.commit()
    db.refresh(note)

    return note


def delete_note(
    note_id: int,
    db: Session,
    current_user: User
):
    note = get_note(
        note_id,
        db,
        current_user
    )

    db.delete(note)
    db.commit()

    return {
        "message": "Note deleted successfully"
    }