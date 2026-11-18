# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("update_cart", __name__)


@bp.route("/update_cart", methods=["POST"])
def update_cart():
    transcript = (request.get_json(silent=True) or {}).get("orders_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(transcript) + "'")
    return jsonify({"result": "success"})
