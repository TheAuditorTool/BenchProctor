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

bp = Blueprint("merge_config", __name__)


@bp.route("/merge_config", methods=["POST"])
def merge_config():
    summary = request.args.get('id', '')
    handshake = (lambda v: v.strip())(summary)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    paragraph = handshake
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(paragraph) + "'")).all()
    return jsonify({"result": "success"})
