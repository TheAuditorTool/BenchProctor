# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_address", __name__)


@bp.route("/validate_address", methods=["POST"])
def validate_address():
    note = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    parsed = json.loads(note)
    return jsonify({'parsed': str(parsed)}), 200
