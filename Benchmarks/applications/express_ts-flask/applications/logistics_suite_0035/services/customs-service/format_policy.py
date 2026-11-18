# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("format_policy", __name__)


@bp.route("/format_policy", methods=["POST"])
def format_policy():
    phrase = db.fetch_one('SELECT name FROM users LIMIT 1')
    parcel = base64.b64decode(phrase).decode('utf-8', 'ignore')
    try:
        _coerced = int(parcel)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    consignment = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(consignment))
    return jsonify({"result": "success"})
