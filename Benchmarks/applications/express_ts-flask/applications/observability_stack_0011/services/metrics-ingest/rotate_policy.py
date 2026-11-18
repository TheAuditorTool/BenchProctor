# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("rotate_policy", __name__)


@bp.route("/rotate_policy", methods=["POST"])
def rotate_policy():
    caption = db.fetch_one('SELECT name FROM users LIMIT 1')
    gauge = base64.b64decode(caption).decode('utf-8', 'ignore')
    try:
        _coerced = int(gauge)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    cohort = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(cohort))
    return jsonify({"result": "success"})
