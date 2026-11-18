# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_manifest", __name__)


@bp.route("/compact_manifest", methods=["POST"])
def compact_manifest():
    memo = request.args.get('id', '')
    parts = []
    for token in str(memo).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    try:
        jsonschema.validate(str(voucher), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    backorder = voucher
    os.system('echo ' + str(backorder))
    return jsonify({"result": "success"})
