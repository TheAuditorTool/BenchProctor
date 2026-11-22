# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + os.environ.get("DATABASE_PATH", "app.db"))
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00080", methods=["POST"])
def BenchmarkTest00080():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    with Session(_engine) as _session:
        _session.query(User).filter(User.id == data).first()
    return jsonify({"result": "success"})
