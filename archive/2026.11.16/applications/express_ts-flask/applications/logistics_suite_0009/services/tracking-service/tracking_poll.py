# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("poll_tracking", __name__)


@bp.route("/poll_tracking", methods=["POST"])
def poll_tracking():
    excerpt = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(excerpt) + "'")
    return jsonify({"result": "success"})
