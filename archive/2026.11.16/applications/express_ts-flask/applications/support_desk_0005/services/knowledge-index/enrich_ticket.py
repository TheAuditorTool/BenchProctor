# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("enrich_ticket", __name__)


@bp.route("/enrich_ticket", methods=["POST"])
def enrich_ticket():
    with open('/tmp/data', 'r') as fh:
        phrase = fh.read()
    inquiry = json.loads(phrase).get('value', '')
    try:
        _coerced = int(inquiry)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    grievance = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(grievance))
    return jsonify({"result": "success"})
