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

bp = Blueprint("export_header", __name__)


@bp.route("/export_header", methods=["POST"])
def export_header():
    paragraph = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if paragraph:
        gauge = paragraph
    else:
        gauge = ''
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users WHERE id = :id')).params(id=gauge).all()
    return jsonify({"result": "success"})
