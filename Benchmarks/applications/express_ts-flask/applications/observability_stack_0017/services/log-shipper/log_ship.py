# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("ship_log", __name__)


@bp.route("/ship_log", methods=["POST"])
def ship_log():
    summary = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (summary,))
    return jsonify({"result": "success"})
