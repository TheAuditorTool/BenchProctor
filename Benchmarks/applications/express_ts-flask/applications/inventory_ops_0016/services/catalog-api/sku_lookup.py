# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("lookup_sku", __name__)


@bp.route("/lookup_sku", methods=["POST"])
def lookup_sku():
    memo = (request.get_json(silent=True) or {}).get("inventory_payload", "")
    parsed = json.loads(memo)
    return jsonify({'parsed': str(parsed)}), 200
