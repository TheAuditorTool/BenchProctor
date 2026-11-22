# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("poll_tracking", __name__)


@bp.route("/poll_tracking", methods=["POST"])
def poll_tracking():
    memo = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': memo})
    return jsonify({"result": "success"})
