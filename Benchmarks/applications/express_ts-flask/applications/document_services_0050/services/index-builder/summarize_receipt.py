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

bp = Blueprint("summarize_receipt", __name__)


@bp.route("/summarize_receipt", methods=["POST"])
def summarize_receipt():
    citation = os.environ.get('DOCUMENTS_INPUT_0050', '')
    def normalize(value):
        return value.strip()
    dossier = normalize(citation)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(dossier) + "'")).all()
    return jsonify({"result": "success"})
