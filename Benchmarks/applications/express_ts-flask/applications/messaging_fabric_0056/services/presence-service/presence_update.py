# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("update_presence", __name__)


@bp.route("/update_presence", methods=["POST"])
def update_presence():
    citation = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    requests.get(str(citation))
    return jsonify({"result": "success"})
