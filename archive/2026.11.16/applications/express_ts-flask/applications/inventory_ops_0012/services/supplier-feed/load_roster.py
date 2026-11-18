# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("load_roster", __name__)


@bp.route("/load_roster", methods=["POST"])
def load_roster():
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
