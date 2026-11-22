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

bp = Blueprint("validate_tenant", __name__)


@bp.route("/validate_tenant", methods=["POST"])
def validate_tenant():
    subtitle = request.args.get('id', '')
    persona = (lambda v: v.strip())(subtitle)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(handshake) + "'")).all()
    return jsonify({"result": "success"})
