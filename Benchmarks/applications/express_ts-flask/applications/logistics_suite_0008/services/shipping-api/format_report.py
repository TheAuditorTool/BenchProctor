# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("format_report", __name__)


@bp.route("/format_report", methods=["POST"])
def format_report():
    caption = request.form.get('multipart_field', '')
    parts = str(caption).split(',')
    consignment = ' '.join(parts)
    parsed = json.loads(consignment)
    return jsonify({'parsed': str(parsed)}), 200
