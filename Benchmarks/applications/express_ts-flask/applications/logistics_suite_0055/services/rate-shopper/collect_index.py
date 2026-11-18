# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_index", __name__)


@bp.route("/collect_index", methods=["POST"])
def collect_index():
    heading = request.args.get('id', '')
    parts = []
    for token in str(heading).split(','):
        parts.append(token.strip())
    consignment = ','.join(parts)
    try:
        jsonschema.validate(str(consignment), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    parcel = consignment
    os.system('echo ' + str(parcel))
    return jsonify({"result": "success"})
