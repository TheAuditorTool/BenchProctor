# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
import re
from flask import Blueprint, request, jsonify
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

bp = Blueprint("normalize_record", __name__)


@bp.route("/normalize_record", methods=["POST"])
def normalize_record():
    caption = request.args.get('id', '')
    synopsis = (lambda v: v.strip())(caption)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", synopsis):
        return jsonify({'error': 'forbidden'}), 400
    snippet = synopsis
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(snippet) + "'")).all()
    return jsonify({"result": "success"})
