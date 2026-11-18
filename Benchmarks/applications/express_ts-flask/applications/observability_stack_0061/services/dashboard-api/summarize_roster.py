# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_roster", __name__)


@bp.route("/summarize_roster", methods=["POST"])
def summarize_roster():
    headline = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    cohort = normalize(headline)
    parsed = json.loads(cohort)
    return jsonify({'parsed': str(parsed)}), 200
