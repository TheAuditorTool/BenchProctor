# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("invoke_connector", __name__)


@bp.route("/invoke_connector", methods=["POST"])
def invoke_connector():
    headline = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(headline) + "'")
    return jsonify({"result": "success"})
