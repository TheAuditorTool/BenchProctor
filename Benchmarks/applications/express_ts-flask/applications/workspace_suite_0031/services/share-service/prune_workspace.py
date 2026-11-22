# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("prune_workspace", __name__)


@bp.route("/prune_workspace", methods=["POST"])
def prune_workspace():
    caption = db.fetch_one('SELECT name FROM users LIMIT 1')
    synopsis = json.loads(caption).get('value', '')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(synopsis) + "'")
    return jsonify({"result": "success"})
