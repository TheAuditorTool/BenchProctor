# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
import re
from urllib.parse import unquote
from flask import Flask, request, jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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


@app.route("/BenchmarkTest00296", methods=["POST"])
def BenchmarkTest00296():
    referer_value = request.headers.get('Referer', '')
    data = unquote(referer_value)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(processed) + "'")).all()
    return jsonify({"result": "success"})
