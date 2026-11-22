# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, jsonify
from app_runtime import db
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


_engine = create_engine("sqlite:///" + DB_PATH)
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

bp = Blueprint("load_summary", __name__)


@bp.route("/load_summary", methods=["POST"])
def load_summary():
    caption = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if caption:
        handshake = caption
    else:
        handshake = ''
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users WHERE id = :id')).params(id=handshake).all()
    return jsonify({"result": "success"})
