# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_header", __name__)


@bp.route("/audit_header", methods=["POST"])
def audit_header():
    summary = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    addendum = normalize(summary)
    parsed = json.loads(addendum)
    return jsonify({'parsed': str(parsed)}), 200
