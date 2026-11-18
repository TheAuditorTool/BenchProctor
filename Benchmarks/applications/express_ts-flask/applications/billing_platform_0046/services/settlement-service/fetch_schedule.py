# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("fetch_schedule", __name__)


@bp.route("/fetch_schedule", methods=["POST"])
def fetch_schedule():
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    remittance = base64.b64decode(remark).decode('utf-8', 'ignore')
    try:
        _coerced = int(remittance)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    arrears = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(arrears))
    return jsonify({"result": "success"})
