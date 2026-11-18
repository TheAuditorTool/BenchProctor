# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("build_config", __name__)


@bp.route("/build_config", methods=["POST"])
def build_config():
    tagline = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    persona = normalize(tagline)
    parsed = json.loads(persona)
    return jsonify({'parsed': str(parsed)}), 200
