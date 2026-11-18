# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("record_bounce", __name__)


@bp.route("/record_bounce", methods=["POST"])
def record_bounce():
    wording = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    requests.get(str(wording))
    return jsonify({"result": "success"})
