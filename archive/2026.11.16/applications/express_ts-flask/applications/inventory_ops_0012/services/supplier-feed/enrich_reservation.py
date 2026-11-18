# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("enrich_reservation", __name__)


@bp.route("/enrich_reservation", methods=["POST"])
def enrich_reservation():
    with open('/tmp/data', 'r') as fh:
        phrase = fh.read()
    backorder = json.loads(phrase).get('value', '')
    try:
        _coerced = int(backorder)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    restock = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(restock))
    return jsonify({"result": "success"})
