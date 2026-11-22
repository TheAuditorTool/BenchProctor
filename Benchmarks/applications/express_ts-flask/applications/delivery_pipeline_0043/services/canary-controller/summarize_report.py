# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_report", __name__)


@bp.route("/summarize_report", methods=["POST"])
def summarize_report():
    remark = request.get_data(as_text=True)
    note = (lambda v: v.strip())(remark)
    parsed = json.loads(note)
    return jsonify({'parsed': str(parsed)}), 200
