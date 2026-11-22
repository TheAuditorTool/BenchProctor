# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("format_policy", __name__)


@bp.route("/format_policy", methods=["POST"])
def format_policy():
    memo = request.get_data(as_text=True)
    backorder = (lambda v: v.strip())(memo)
    parsed = json.loads(backorder)
    return jsonify({'parsed': str(parsed)}), 200
