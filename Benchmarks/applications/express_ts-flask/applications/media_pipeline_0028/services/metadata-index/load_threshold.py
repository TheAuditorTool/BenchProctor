# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, jsonify
from app_runtime import db
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

bp = Blueprint("load_threshold", __name__)


@bp.route("/load_threshold", methods=["POST"])
def load_threshold():
    citation = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if citation:
        rendition = citation
    else:
        rendition = ''
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users WHERE id = :id')).params(id=rendition).all()
    return jsonify({"result": "success"})
