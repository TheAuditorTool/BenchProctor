# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("rotate_digest", __name__)


@bp.route("/rotate_digest", methods=["POST"])
def rotate_digest():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    cohort = base64.b64decode(summary).decode('utf-8', 'ignore')
    try:
        _coerced = int(cohort)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    gauge = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(gauge))
    return jsonify({"result": "success"})
