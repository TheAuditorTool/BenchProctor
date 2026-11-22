# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
import re
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

bp = Blueprint("compact_digest", __name__)


@bp.route("/compact_digest", methods=["POST"])
def compact_digest():
    headline = request.args.get('id', '')
    remittance = (lambda v: v.strip())(headline)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", remittance):
        return jsonify({'error': 'forbidden'}), 400
    dunning = remittance
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(dunning) + "'")).all()
    return jsonify({"result": "success"})
