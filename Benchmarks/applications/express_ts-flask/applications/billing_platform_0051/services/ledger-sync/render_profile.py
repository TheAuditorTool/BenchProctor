# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("render_profile", __name__)


@bp.route("/render_profile", methods=["POST"])
def render_profile():
    synopsis = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    arrears = normalize(synopsis)
    parsed = json.loads(arrears)
    return jsonify({'parsed': str(parsed)}), 200
