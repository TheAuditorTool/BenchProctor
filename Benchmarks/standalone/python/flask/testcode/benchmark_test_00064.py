# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Flask, jsonify
import os
import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


redis_client = redis.Redis.from_url(os.environ.get("REDIS_URL", "redis://cache:6379"))
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


@app.route("/BenchmarkTest00064", methods=["POST"])
def BenchmarkTest00064():
    redis_value = redis_client.get('user_data')
    parts = str(redis_value).split(',')
    data = ' '.join(parts)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(data) + "'")).all()
    return jsonify({"result": "success"})
