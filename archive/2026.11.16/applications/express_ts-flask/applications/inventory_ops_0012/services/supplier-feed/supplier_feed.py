# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("pull_supplier_feed", __name__)


@bp.route("/pull_supplier_feed", methods=["POST"])
def pull_supplier_feed():
    summary = (request.get_json(silent=True) or {}).get("inventory_payload", "")
    parsed = yaml.safe_load(summary)
    return jsonify({'parsed': str(parsed)}), 200
