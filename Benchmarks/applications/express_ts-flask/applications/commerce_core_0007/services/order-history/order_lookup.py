# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("lookup_order", __name__)


@bp.route("/lookup_order", methods=["POST"])
def lookup_order():
    wording = (request.get_json(silent=True) or {}).get("orders_payload", "")
    parsed = yaml.safe_load(wording)
    return jsonify({'parsed': str(parsed)}), 200
