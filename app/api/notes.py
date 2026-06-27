from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.schemas.note import (
    NoteCreate,
    NoteUpdate,
    NoteResponse
)
from app.services.note_service import (
    create_note,
    get_notes,
    get_note,
    update_note,
    delete_note
)

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)
@router.post(
    "",
    response_model=NoteResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_note(
    note: NoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_note(
        note,
        db,
        current_user
    )
@router.get(
    "",
    response_model=list[NoteResponse]
)
def read_notes(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_notes(
        db,
        current_user
    )

@router.get(
    "/{note_id}",
    response_model=NoteResponse
)
def read_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_note(
        note_id,
        db,
        current_user
    )

@router.put(
    "/{note_id}",
    response_model=NoteResponse
)
def edit_note(
    note_id: int,
    note: NoteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_note(
        note_id,
        note,
        db,
        current_user
    )


@router.delete(
    "/{note_id}"
)
def remove_note(
    note_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_note(
        note_id,
        db,
        current_user
    )