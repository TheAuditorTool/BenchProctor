# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("triage_alert", __name__)


@bp.route("/triage_alert", methods=["POST"])
def triage_alert():
    headline = (request.get_json(silent=True) or {}).get("risk_payload", "")
    s = socket.create_connection((str(headline), 80))
    s.close()
    return jsonify({"result": "success"})
