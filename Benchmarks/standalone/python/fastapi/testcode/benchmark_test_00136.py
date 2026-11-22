# SPDX-License-Identifier: Apache-2.0
from fastapi import FastAPI, Request
from sqlalchemy import text
import os
import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from fastapi.responses import JSONResponse


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))
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


@app.post("/BenchmarkTest00136")
async def BenchmarkTest00136(request: Request):
    redis_value = redis_client.get('user_data')
    parts = str(redis_value).split(',')
    data = ' '.join(parts)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(data) + "'")).all()
    return {"updated": True}
