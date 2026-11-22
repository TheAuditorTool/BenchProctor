# SPDX-License-Identifier: Apache-2.0
from fastapi import APIRouter, Request
from sqlalchemy import text
from starlette.responses import JSONResponse
import re
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


@router.post("/enrich_index")
async def enrich_index(request: Request):
    citation = (await request.form()).get('field', '')
    consignment = (lambda v: v.strip())(citation)
    if not re.fullmatch("^(asc|desc|name|created)$", str(consignment)):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    parcel = consignment
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users ORDER BY ' + str(parcel))).all()
    return {"updated": True}
