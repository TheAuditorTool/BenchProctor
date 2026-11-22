# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_config", __name__)


@bp.route("/prune_config", methods=["POST"])
def prune_config():
    memo = request.get_data(as_text=True)
    verdict = (lambda v: v.strip())(memo)
    parsed = json.loads(verdict)
    return jsonify({'parsed': str(parsed)}), 200
