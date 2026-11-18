# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("resolve_summary", __name__)


@bp.route("/resolve_summary", methods=["POST"])
def resolve_summary():
    footnote = request.args.get('id', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    try:
        jsonschema.validate(str(consignment), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    parcel = consignment
    os.system('echo ' + str(parcel))
    return jsonify({"result": "success"})
