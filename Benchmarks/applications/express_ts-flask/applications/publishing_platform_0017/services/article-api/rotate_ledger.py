# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("rotate_ledger", __name__)


@bp.route("/rotate_ledger", methods=["POST"])
def rotate_ledger():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    addendum = base64.b64decode(summary).decode('utf-8', 'ignore')
    try:
        _coerced = int(addendum)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    byline = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(byline))
    return jsonify({"result": "success"})
