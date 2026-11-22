# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("format_roster", __name__)


@bp.route("/format_roster", methods=["POST"])
def format_roster():
    excerpt = request.get_data(as_text=True)
    cohort = (lambda v: v.strip())(excerpt)
    parsed = json.loads(cohort)
    return jsonify({'parsed': str(parsed)}), 200
