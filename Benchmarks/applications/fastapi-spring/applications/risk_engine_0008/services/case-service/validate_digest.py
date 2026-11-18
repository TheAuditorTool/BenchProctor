# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import db
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


_engine = create_engine("sqlite:///" + DB_PATH)
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

router = APIRouter()


@router.post("/validate_digest")
async def validate_digest(request: Request):
    synopsis = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    verdict = (lambda v: v.strip())(synopsis)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == verdict)).first()
    return {"updated": True}
