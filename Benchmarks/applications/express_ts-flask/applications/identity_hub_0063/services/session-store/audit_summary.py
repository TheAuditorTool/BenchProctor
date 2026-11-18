# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


_engine = create_engine("sqlite:///" + DB_PATH)
class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

bp = Blueprint("audit_summary", __name__)


@bp.route("/audit_summary", methods=["POST"])
def audit_summary():
    paragraph = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    persona = normalize(paragraph)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == persona)).first()
    return jsonify({"result": "success"})
