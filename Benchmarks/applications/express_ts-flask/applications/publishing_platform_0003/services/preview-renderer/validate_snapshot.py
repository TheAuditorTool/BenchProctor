# SPDX-License-Identifier: Apache-2.0
from sqlalchemy import text
from flask import Blueprint, jsonify
import requests
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

bp = Blueprint("validate_snapshot", __name__)


@bp.route("/validate_snapshot", methods=["POST"])
def validate_snapshot():
    heading = requests.get('https://api.partner.example.com/v1/profile').text
    addendum = heading if heading else 'default'
    with Session(_engine) as _session:
        _session.query(User).from_statement(text("SELECT * FROM users WHERE name = '" + str(addendum) + "'")).all()
    return jsonify({"result": "success"})
