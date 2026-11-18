# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00634", methods=["POST"])
def BenchmarkTest00634():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data, _sep, _rest = str(profile_value).partition('\x00')
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == data)).first()
    return jsonify({"result": "success"})
