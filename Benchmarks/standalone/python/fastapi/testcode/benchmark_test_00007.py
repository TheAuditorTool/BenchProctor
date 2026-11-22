# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from sqlalchemy import text
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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


@app.post("/BenchmarkTest00007")
async def BenchmarkTest00007(request: Request):
    referer_value = request.headers.get('referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(data) + "'")).all()
    return {"updated": True}
