# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("export_snapshot", __name__)


@bp.route("/export_snapshot", methods=["POST"])
def export_snapshot():
    with open('/tmp/data', 'r') as fh:
        heading = fh.read()
    bulletin = json.loads(heading).get('value', '')
    try:
        _coerced = int(bulletin)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    excerpt = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(excerpt))
    return jsonify({"result": "success"})
