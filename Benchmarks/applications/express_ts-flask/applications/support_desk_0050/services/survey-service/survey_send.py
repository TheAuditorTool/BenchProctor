# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("send_survey", __name__)


@bp.route("/send_survey", methods=["POST"])
def send_survey():
    passage = (request.get_json(silent=True) or {}).get("support_payload", "")
    requests.get(str(passage))
    return jsonify({"result": "success"})
