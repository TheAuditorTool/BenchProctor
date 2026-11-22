# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("search_knowledge", __name__)


@bp.route("/search_knowledge", methods=["POST"])
def search_knowledge():
    note = (request.get_json(silent=True) or {}).get("support_payload", "")
    requests.get(str(note))
    return jsonify({"result": "success"})
