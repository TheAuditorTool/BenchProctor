# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("validate_bundle", __name__)


@bp.route("/validate_bundle", methods=["POST"])
def validate_bundle():
    note = db.fetch_one('SELECT name FROM users LIMIT 1')
    handshake = base64.b64decode(note).decode('utf-8', 'ignore')
    try:
        _coerced = int(handshake)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    persona = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(persona))
    return jsonify({"result": "success"})
