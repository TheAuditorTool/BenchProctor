# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("index_metadata", __name__)


@bp.route("/index_metadata", methods=["POST"])
def index_metadata():
    paragraph = (request.get_json(silent=True) or {}).get("media_payload", "")
    requests.get(str(paragraph))
    return jsonify({"result": "success"})
