# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, jsonify
import os
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

bp = Blueprint("collect_bundle", __name__)


@bp.route("/collect_bundle", methods=["POST"])
def collect_bundle():
    memo = os.environ.get('RISK_INPUT_0052', '')
    def normalize(value):
        return value.strip()
    verdict = normalize(memo)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(verdict) + "'")).all()
    return jsonify({"result": "success"})
