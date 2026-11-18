# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_receipt", __name__)


@bp.route("/collect_receipt", methods=["POST"])
def collect_receipt():
    snippet = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    persona = normalize(snippet)
    parsed = json.loads(persona)
    return jsonify({'parsed': str(parsed)}), 200
