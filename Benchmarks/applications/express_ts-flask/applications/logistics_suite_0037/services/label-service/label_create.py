# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("create_label", __name__)


@bp.route("/create_label", methods=["POST"])
def create_label():
    memo = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    db.execute('SELECT * FROM users WHERE id = ?', (memo,))
    return jsonify({"result": "success"})
