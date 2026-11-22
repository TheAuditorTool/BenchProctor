# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("build_summary", __name__)


@bp.route("/build_summary", methods=["POST"])
def build_summary():
    summary = request.get_data(as_text=True)
    phrase = (lambda v: v.strip())(summary)
    parsed = json.loads(phrase)
    return jsonify({'parsed': str(parsed)}), 200
