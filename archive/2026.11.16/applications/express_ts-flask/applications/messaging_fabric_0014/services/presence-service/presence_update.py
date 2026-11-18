# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("update_presence", __name__)


@bp.route("/update_presence", methods=["POST"])
def update_presence():
    heading = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    try:
        _coerced = int(heading)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    notice = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(notice))
    return jsonify({"result": "success"})
