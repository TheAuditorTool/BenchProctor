# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("invoke_connector", __name__)


@bp.route("/invoke_connector", methods=["POST"])
def invoke_connector():
    passage = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    requests.get(str(passage))
    return jsonify({"result": "success"})
