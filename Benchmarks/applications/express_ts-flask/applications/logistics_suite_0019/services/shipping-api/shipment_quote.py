# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


_engine = create_engine("sqlite:///" + DB_PATH)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

bp = Blueprint("quote_shipment", __name__)


@bp.route("/quote_shipment", methods=["POST"])
def quote_shipment():
    remark = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    with Session(_engine) as _session:
        _session.query(User).from_statement(text('SELECT * FROM users WHERE id = :id')).params(id=remark).all()
    return jsonify({"result": "success"})
