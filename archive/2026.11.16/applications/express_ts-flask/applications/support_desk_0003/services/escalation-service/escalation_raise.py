# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("raise_escalation", __name__)


@bp.route("/raise_escalation", methods=["POST"])
def raise_escalation():
    excerpt = (request.get_json(silent=True) or {}).get("support_payload", "")
    requests.get(str(excerpt))
    return jsonify({"result": "success"})
