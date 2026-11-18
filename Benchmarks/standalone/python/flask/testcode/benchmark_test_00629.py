# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


def make_reader(raw):
    def read():
        return raw.strip()
    return read
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


@app.route("/BenchmarkTest00629", methods=["POST"])
def BenchmarkTest00629():
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    reader = make_reader(config_value)
    data = reader()
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == data)).first()
    return jsonify({"result": "success"})
