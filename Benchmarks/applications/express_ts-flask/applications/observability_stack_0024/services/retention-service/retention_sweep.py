# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("sweep_retention", __name__)


@bp.route("/sweep_retention", methods=["POST"])
def sweep_retention():
    excerpt = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    parsed = json.loads(excerpt)
    return jsonify({'parsed': str(parsed)}), 200
