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

bp = Blueprint("prune_ledger", __name__)


@bp.route("/prune_ledger", methods=["POST"])
def prune_ledger():
    notice = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(notice)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == rendition)).first()
    return jsonify({"result": "success"})
