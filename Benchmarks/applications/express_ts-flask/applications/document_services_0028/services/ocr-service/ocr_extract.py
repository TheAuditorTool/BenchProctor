# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("extract_text", __name__)


@bp.route("/extract_text", methods=["POST"])
def extract_text():
    heading = (request.get_json(silent=True) or {}).get("documents_payload", "")
    requests.get(str(heading))
    return jsonify({"result": "success"})
