# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Flask, jsonify
from app_runtime import db
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


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


@app.route("/BenchmarkTest00064", methods=["POST"])
def BenchmarkTest00064():
    profile_value = db.fetch_one('SELECT bio FROM profiles LIMIT 1')
    data = '{}'.format(profile_value)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM "' + str(data).replace('"', '""') + '"')).all()
    return jsonify({"result": "success"})
