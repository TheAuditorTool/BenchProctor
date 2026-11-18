# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


bp = Blueprint("create_session", __name__)


@bp.route("/create_session", methods=["POST"])
def create_session():
    transcript = (request.get_json(silent=True) or {}).get("identity_payload", "")
    pickle.loads(base64.b64decode(transcript))
    return jsonify({"result": "success"})
