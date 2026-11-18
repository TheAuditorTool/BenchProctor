# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("rotate_window", __name__)


@bp.route("/rotate_window", methods=["POST"])
def rotate_window():
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    backorder = base64.b64decode(citation).decode('utf-8', 'ignore')
    try:
        _coerced = int(backorder)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    voucher = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(voucher))
    return jsonify({"result": "success"})
