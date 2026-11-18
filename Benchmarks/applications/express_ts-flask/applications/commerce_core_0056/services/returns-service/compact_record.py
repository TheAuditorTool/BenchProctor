# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_record", __name__)


@bp.route("/compact_record", methods=["POST"])
def compact_record():
    citation = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    backorder = normalize(citation)
    parsed = json.loads(backorder)
    return jsonify({'parsed': str(parsed)}), 200
