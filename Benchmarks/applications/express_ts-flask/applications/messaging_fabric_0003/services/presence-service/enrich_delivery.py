# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_delivery", __name__)


@bp.route("/enrich_delivery", methods=["POST"])
def enrich_delivery():
    subject = request.args.get('id', '')
    parts = []
    for token in str(subject).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    try:
        jsonschema.validate(str(bulletin), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    passage = bulletin
    os.system('echo ' + str(passage))
    return jsonify({"result": "success"})
