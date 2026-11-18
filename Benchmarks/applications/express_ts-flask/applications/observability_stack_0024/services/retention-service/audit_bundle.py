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

bp = Blueprint("audit_bundle", __name__)


@bp.route("/audit_bundle", methods=["POST"])
def audit_bundle():
    summary = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    cohort = normalize(summary)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == cohort)).first()
    return jsonify({"result": "success"})
