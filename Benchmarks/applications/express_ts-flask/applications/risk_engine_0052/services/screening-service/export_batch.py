# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("export_batch", __name__)


@bp.route("/export_batch", methods=["POST"])
def export_batch():
    memo = request.get_data(as_text=True)
    verdict = (lambda v: v.strip())(memo)
    parsed = json.loads(verdict)
    return jsonify({'parsed': str(parsed)}), 200
