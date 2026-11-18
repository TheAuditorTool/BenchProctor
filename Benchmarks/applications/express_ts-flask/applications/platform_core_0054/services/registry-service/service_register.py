# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("register_service", __name__)


@bp.route("/register_service", methods=["POST"])
def register_service():
    caption = (request.get_json(silent=True) or {}).get("platform_payload", "")
    requests.get(str(caption))
    return jsonify({"result": "success"})
