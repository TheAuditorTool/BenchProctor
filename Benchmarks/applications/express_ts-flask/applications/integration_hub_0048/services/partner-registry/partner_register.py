# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


_engine = create_engine("sqlite:///" + DB_PATH)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

bp = Blueprint("register_partner", __name__)


@bp.route("/register_partner", methods=["POST"])
def register_partner():
    preface = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(preface) + "'")).all()
    return jsonify({"result": "success"})
