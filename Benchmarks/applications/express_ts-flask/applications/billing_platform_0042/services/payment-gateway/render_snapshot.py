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

bp = Blueprint("render_snapshot", __name__)


@bp.route("/render_snapshot", methods=["POST"])
def render_snapshot():
    remark = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    with Session(_engine) as _session:
        _session.scalars(select(User).where(User.id == remittance)).first()
    return jsonify({"result": "success"})
