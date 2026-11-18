# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("reconcile_profile", __name__)


@bp.route("/reconcile_profile", methods=["POST"])
def reconcile_profile():
    with open('/tmp/data', 'r') as fh:
        excerpt = fh.read()
    dossier = json.loads(excerpt).get('value', '')
    try:
        _coerced = int(dossier)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    addendum = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(addendum))
    return jsonify({"result": "success"})
