# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("export_policy", __name__)


@bp.route("/export_policy", methods=["POST"])
def export_policy():
    with open('/tmp/data', 'r') as fh:
        subtitle = fh.read()
    ledger = json.loads(subtitle).get('value', '')
    try:
        _coerced = int(ledger)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    remittance = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(remittance))
    return jsonify({"result": "success"})
