# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket
import urllib.parse


bp = Blueprint("run_screening", __name__)


@bp.route("/run_screening", methods=["POST"])
def run_screening():
    phrase = (request.get_json(silent=True) or {}).get("risk_payload", "")
    s = socket.create_connection((urllib.parse.urlparse(str(phrase)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
