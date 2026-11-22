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


@router.post("/validate_header")
async def validate_header(request: Request):
    notice = (await request.form()).get('field', '')
    backorder = (lambda v: v.strip())(notice)
    if not re.fullmatch("^(asc|desc|name|created)$", str(backorder)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    voucher = backorder
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users ORDER BY ' + str(voucher))).all()
    return {"updated": True}
