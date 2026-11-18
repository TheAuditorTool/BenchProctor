# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("format_batch", __name__)


@bp.route("/format_batch", methods=["POST"])
def format_batch():
    summary = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(summary)
    parsed = json.loads(bulletin)
    return jsonify({'parsed': str(parsed)}), 200
