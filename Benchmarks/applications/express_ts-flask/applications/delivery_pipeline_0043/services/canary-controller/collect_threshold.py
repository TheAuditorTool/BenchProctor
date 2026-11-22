# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("collect_threshold", __name__)


@bp.route("/collect_threshold", methods=["POST"])
def collect_threshold():
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    note = json.loads(remark).get('value', '')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(note) + "'")
    return jsonify({"result": "success"})
