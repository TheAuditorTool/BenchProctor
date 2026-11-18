# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("resolve_checkpoint", __name__)


@bp.route("/resolve_checkpoint", methods=["POST"])
def resolve_checkpoint():
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    bulletin = base64.b64decode(footnote).decode('utf-8', 'ignore')
    try:
        _coerced = int(bulletin)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    heading = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(heading))
    return jsonify({"result": "success"})
