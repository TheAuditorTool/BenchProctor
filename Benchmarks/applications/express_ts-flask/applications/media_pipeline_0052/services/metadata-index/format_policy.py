# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("format_policy", __name__)


@bp.route("/format_policy", methods=["POST"])
def format_policy():
    tagline = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(tagline)
    parsed = json.loads(rendition)
    return jsonify({'parsed': str(parsed)}), 200
