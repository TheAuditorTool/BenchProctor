# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("map_field", __name__)


@bp.route("/map_field", methods=["POST"])
def map_field():
    summary = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(summary) + "'")
    return jsonify({"result": "success"})
