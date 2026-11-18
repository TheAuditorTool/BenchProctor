# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("validate_config", __name__)


@bp.route("/validate_config", methods=["POST"])
def validate_config():
    transcript = request.form.get('field', '')
    heading = f'{transcript!s}'
    parsed = json.loads(heading)
    return jsonify({'parsed': str(parsed)}), 200
