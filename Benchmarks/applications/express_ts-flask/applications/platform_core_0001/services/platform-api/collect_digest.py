# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_digest", __name__)


@bp.route("/collect_digest", methods=["POST"])
def collect_digest():
    tagline = request.args.get('id', '')
    parts = []
    for token in str(tagline).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    try:
        jsonschema.validate(str(persona), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    handshake = persona
    os.system('echo ' + str(handshake))
    return jsonify({"result": "success"})
