# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("validate_schedule", __name__)


@bp.route("/validate_schedule", methods=["POST"])
def validate_schedule():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    restock = base64.b64decode(summary).decode('utf-8', 'ignore')
    try:
        _coerced = int(restock)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    backorder = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(backorder))
    return jsonify({"result": "success"})
