# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("apply_redaction", __name__)


@bp.route("/apply_redaction", methods=["POST"])
def apply_redaction():
    synopsis = (request.get_json(silent=True) or {}).get("documents_payload", "")
    parsed = json.loads(synopsis)
    return jsonify({'parsed': str(parsed)}), 200
