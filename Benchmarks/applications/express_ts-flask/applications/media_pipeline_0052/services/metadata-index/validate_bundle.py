# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_bundle", __name__)


@bp.route("/validate_bundle", methods=["POST"])
def validate_bundle():
    tagline = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    rendition = normalize(tagline)
    parsed = json.loads(rendition)
    return jsonify({'parsed': str(parsed)}), 200
