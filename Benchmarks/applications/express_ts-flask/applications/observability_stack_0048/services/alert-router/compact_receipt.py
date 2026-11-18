# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("compact_receipt", __name__)


@bp.route("/compact_receipt", methods=["POST"])
def compact_receipt():
    excerpt = db.fetch_one('SELECT name FROM users LIMIT 1')
    gauge = base64.b64decode(excerpt).decode('utf-8', 'ignore')
    try:
        _coerced = int(gauge)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    cohort = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(cohort))
    return jsonify({"result": "success"})
