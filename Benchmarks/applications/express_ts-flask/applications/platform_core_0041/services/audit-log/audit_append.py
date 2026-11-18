# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("append_audit", __name__)


@bp.route("/append_audit", methods=["POST"])
def append_audit():
    transcript = (request.get_json(silent=True) or {}).get("platform_payload", "")
    s = socket.create_connection((str(transcript), 80))
    s.close()
    return jsonify({"result": "success"})
