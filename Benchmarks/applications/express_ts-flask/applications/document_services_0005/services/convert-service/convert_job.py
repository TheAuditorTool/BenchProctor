# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("run_conversion", __name__)


@bp.route("/run_conversion", methods=["POST"])
def run_conversion():
    subtitle = (request.get_json(silent=True) or {}).get("documents_payload", "")
    parsed = json.loads(subtitle)
    return jsonify({'parsed': str(parsed)}), 200
