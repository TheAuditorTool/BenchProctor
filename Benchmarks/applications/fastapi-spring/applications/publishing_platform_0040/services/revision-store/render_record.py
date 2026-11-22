# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


_engine = create_engine("sqlite:///" + DB_PATH)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

router = APIRouter()


@router.post("/render_record")
async def render_record(request: Request):
    transcript = request.headers.get('referer', '')
    addendum, _sep, _rest = str(transcript).partition('\x00')
    with Session(_engine) as _session:
        _session.query(User).filter(User.id == addendum).first()
    return {"updated": True}
