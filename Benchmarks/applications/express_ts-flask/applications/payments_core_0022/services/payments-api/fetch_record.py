# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("fetch_record", __name__)


@bp.route("/fetch_record", methods=["POST"])
def fetch_record():
    subject = db.fetch_one('SELECT name FROM users LIMIT 1')
    ledger = base64.b64decode(subject).decode('utf-8', 'ignore')
    try:
        _coerced = int(ledger)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    disbursement = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(disbursement))
    return jsonify({"result": "success"})
