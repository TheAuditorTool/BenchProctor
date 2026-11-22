# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, jsonify
import requests
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

bp = Blueprint("enrich_bundle", __name__)


@bp.route("/enrich_bundle", methods=["POST"])
def enrich_bundle():
    synopsis = requests.get('https://api.partner.example.com/v1/profile').text
    byline = synopsis if synopsis else 'default'
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(byline) + "'")).all()
    return jsonify({"result": "success"})
