# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("shop_rate", __name__)


@bp.route("/shop_rate", methods=["POST"])
def shop_rate():
    quotation = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    parsed = yaml.safe_load(quotation)
    return jsonify({'parsed': str(parsed)}), 200
