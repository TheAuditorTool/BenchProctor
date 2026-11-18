# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("edit_document", __name__)


@bp.route("/edit_document", methods=["POST"])
def edit_document():
    excerpt = (request.get_json(silent=True) or {}).get("workspace_payload", "")
    requests.get(str(excerpt))
    return jsonify({"result": "success"})
