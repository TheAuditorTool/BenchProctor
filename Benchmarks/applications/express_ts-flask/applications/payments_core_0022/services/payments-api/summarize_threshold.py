# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_threshold", __name__)


@bp.route("/summarize_threshold", methods=["POST"])
def summarize_threshold():
    subject = request.args.get('id', '')
    parts = []
    for token in str(subject).split(','):
        parts.append(token.strip())
    ledger = ','.join(parts)
    try:
        jsonschema.validate(str(ledger), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    disbursement = ledger
    os.system('echo ' + str(disbursement))
    return jsonify({"result": "success"})
