# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("annotate_report", __name__)


@bp.route("/annotate_report", methods=["POST"])
def annotate_report():
    remark = request.args.get('id', '')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    synopsis = ','.join(parts)
    try:
        jsonschema.validate(str(synopsis), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    quotation = synopsis
    os.system('echo ' + str(quotation))
    return jsonify({"result": "success"})
