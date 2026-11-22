# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, jsonify
import os
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

bp = Blueprint("build_invoice", __name__)


@bp.route("/build_invoice", methods=["POST"])
def build_invoice():
    footnote = os.environ.get('BILLING_INPUT_0061', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(footnote)
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(remittance) + "'")).all()
    return jsonify({"result": "success"})
