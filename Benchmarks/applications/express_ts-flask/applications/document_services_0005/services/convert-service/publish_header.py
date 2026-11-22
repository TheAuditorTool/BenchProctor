# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("publish_header", __name__)


@bp.route("/publish_header", methods=["POST"])
def publish_header():
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    addendum = json.loads(footnote).get('value', '')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(addendum) + "'")
    return jsonify({"result": "success"})
