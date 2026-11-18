# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("fetch_batch", __name__)


@bp.route("/fetch_batch", methods=["POST"])
def fetch_batch():
    tagline = request.args.get('id', '')
    parts = []
    for token in str(tagline).split(','):
        parts.append(token.strip())
    rendition = ','.join(parts)
    try:
        jsonschema.validate(str(rendition), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    montage = rendition
    os.system('echo ' + str(montage))
    return jsonify({"result": "success"})
