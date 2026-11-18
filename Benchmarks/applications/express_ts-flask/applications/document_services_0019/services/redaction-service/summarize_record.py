# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_record", __name__)


@bp.route("/summarize_record", methods=["POST"])
def summarize_record():
    passage = request.args.get('id', '')
    parts = []
    for token in str(passage).split(','):
        parts.append(token.strip())
    dossier = ','.join(parts)
    try:
        jsonschema.validate(str(dossier), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    addendum = dossier
    os.system('echo ' + str(addendum))
    return jsonify({"result": "success"})
