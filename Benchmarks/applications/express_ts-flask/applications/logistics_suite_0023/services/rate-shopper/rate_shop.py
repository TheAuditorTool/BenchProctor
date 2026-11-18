# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("shop_rate", __name__)


@bp.route("/shop_rate", methods=["POST"])
def shop_rate():
    headline = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    try:
        _coerced = int(headline)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    consignment = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(consignment))
    return jsonify({"result": "success"})
