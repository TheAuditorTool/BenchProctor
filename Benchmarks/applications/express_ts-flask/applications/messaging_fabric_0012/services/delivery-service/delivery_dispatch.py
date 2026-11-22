# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("dispatch_delivery", __name__)


@bp.route("/dispatch_delivery", methods=["POST"])
def dispatch_delivery():
    remark = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    parsed = yaml.safe_load(remark)
    return jsonify({'parsed': str(parsed)}), 200
