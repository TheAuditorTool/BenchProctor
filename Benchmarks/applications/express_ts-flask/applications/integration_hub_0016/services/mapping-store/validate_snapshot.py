# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_snapshot", __name__)


@bp.route("/validate_snapshot", methods=["POST"])
def validate_snapshot():
    wording = request.get_data(as_text=True)
    handshake = (lambda v: v.strip())(wording)
    parsed = json.loads(handshake)
    return jsonify({'parsed': str(parsed)}), 200
