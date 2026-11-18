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

bp = Blueprint("verify_checkpoint", __name__)


@bp.route("/verify_checkpoint", methods=["POST"])
def verify_checkpoint():
    citation = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(citation)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == parcel)).first()
    return jsonify({"result": "success"})
