# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("route_alert", __name__)


@bp.route("/route_alert", methods=["POST"])
def route_alert():
    snippet = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(snippet) + "'")
    return jsonify({"result": "success"})
