# SPDX-License-Identifier: Apache-2.0
import base64
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("enrich_record", __name__)


@bp.route("/enrich_record", methods=["POST"])
def enrich_record():
    subject = db.fetch_one('SELECT name FROM users LIMIT 1')
    bulletin = base64.b64decode(subject).decode('utf-8', 'ignore')
    try:
        _coerced = int(bulletin)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    passage = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(passage))
    return jsonify({"result": "success"})
