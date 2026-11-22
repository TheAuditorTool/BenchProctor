# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from sqlalchemy import text
from app_runtime import db
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from fastapi.responses import JSONResponse


_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00136")
async def BenchmarkTest00136(request: Request):
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '{}'.format(profile_value)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM "' + str(data).replace('"', '""') + '"')).all()
    return {"updated": True}
