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

bp = Blueprint("publish_roster", __name__)


@bp.route("/publish_roster", methods=["POST"])
def publish_roster():
    citation = request.args.get('id', '')
    handshake = (lambda v: v.strip())(citation)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    heading = handshake
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(heading) + "'")).all()
    return jsonify({"result": "success"})
