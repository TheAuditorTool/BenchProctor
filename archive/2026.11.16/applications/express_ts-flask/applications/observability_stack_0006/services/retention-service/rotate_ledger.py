# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("rotate_ledger", __name__)


@bp.route("/rotate_ledger", methods=["POST"])
def rotate_ledger():
    with open('/tmp/data', 'r') as fh:
        preface = fh.read()
    cohort = json.loads(preface).get('value', '')
    try:
        _coerced = int(cohort)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    gauge = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(gauge))
    return jsonify({"result": "success"})
