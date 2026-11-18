# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("compact_config", __name__)


@bp.route("/compact_config", methods=["POST"])
def compact_config():
    with open('/tmp/data', 'r') as fh:
        excerpt = fh.read()
    persona = json.loads(excerpt).get('value', '')
    try:
        _coerced = int(persona)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    wording = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(wording))
    return jsonify({"result": "success"})
