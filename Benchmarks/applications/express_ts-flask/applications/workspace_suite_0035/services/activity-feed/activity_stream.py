# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("stream_activity", __name__)


@bp.route("/stream_activity", methods=["POST"])
def stream_activity():
    note = (request.get_json(silent=True) or {}).get("workspace_payload", "")
    requests.get(str(note))
    return jsonify({"result": "success"})
