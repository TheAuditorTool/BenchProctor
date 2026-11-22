# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from sqlalchemy import text
from starlette.responses import JSONResponse
import re
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


_engine = create_engine("sqlite:///" + DB_PATH)
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

router = APIRouter()


@router.post("/render_receipt")
async def render_receipt(request: Request):
    tagline = (await request.form()).get('field', '')
    persona = (lambda v: v.strip())(tagline)
    if not re.fullmatch("^(asc|desc|name|created)$", str(persona)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    note = persona
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users ORDER BY ' + str(note))).all()
    return {"updated": True}
