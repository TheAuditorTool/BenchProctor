# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
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


@router.post("/export_report")
async def export_report(request: Request):
    subject = request.headers.get('referer', '')
    voucher, _sep, _rest = str(subject).partition('\x00')
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == voucher)).first()
    return {"updated": True}
