# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("compact_carrier", __name__)


@bp.route("/compact_carrier", methods=["POST"])
def compact_carrier():
    with open('/tmp/data', 'r') as fh:
        subject = fh.read()
    parcel = json.loads(subject).get('value', '')
    try:
        _coerced = int(parcel)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    consignment = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(consignment))
    return jsonify({"result": "success"})
