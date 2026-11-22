# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
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


@app.route("/BenchmarkTest00310", methods=["POST"])
def BenchmarkTest00310():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _coerced
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users WHERE id = ' + str(processed))).all()
    return jsonify({"result": "success"})
