# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("validate_receipt", __name__)


@bp.route("/validate_receipt", methods=["POST"])
def validate_receipt():
    headline = db.fetch_one('SELECT name FROM users LIMIT 1')
    disbursement = base64.b64decode(headline).decode('utf-8', 'ignore')
    try:
        _coerced = int(disbursement)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    remittance = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(remittance))
    return jsonify({"result": "success"})
