# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("reconcile_digest", __name__)


@bp.route("/reconcile_digest", methods=["POST"])
def reconcile_digest():
    summary = request.args.get('id', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    restock = ','.join(parts)
    try:
        jsonschema.validate(str(restock), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    backorder = restock
    os.system('echo ' + str(backorder))
    return jsonify({"result": "success"})
