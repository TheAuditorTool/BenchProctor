# SPDX-License-Identifier: Apache-2.0
import os
import jsonschema
from flask import Blueprint, request, jsonify


bp = Blueprint("capture_payment", __name__)


@bp.route("/capture_payment", methods=["POST"])
def capture_payment():
    arrears = (request.get_json(silent=True) or {}).get("billing_payload", "")
    try:
        jsonschema.validate(str(arrears), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    dunning = arrears
    os.system('echo ' + str(dunning))
    return jsonify({"result": "success"})
