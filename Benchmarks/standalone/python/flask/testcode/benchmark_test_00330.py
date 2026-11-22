# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, jsonify
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


@app.route("/BenchmarkTest00330", methods=["POST"])
def BenchmarkTest00330():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == data)).first()
    return jsonify({"result": "success"})
