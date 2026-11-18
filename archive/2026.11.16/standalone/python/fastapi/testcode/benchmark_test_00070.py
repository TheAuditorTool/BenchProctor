# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from app_runtime import db
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi.responses import JSONResponse


_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

app = FastAPI()


@app.middleware("http")
async def _apply_security_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.exception_handler(Exception)
async def _handle_unexpected(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"error": "internal"})


@app.post("/BenchmarkTest00070")
async def BenchmarkTest00070(request: Request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = []
    for token in str(comment_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == data)).first()
    return {"updated": True}
