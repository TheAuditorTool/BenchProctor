# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_index", __name__)


@bp.route("/rotate_index", methods=["POST"])
def rotate_index():
    passage = request.form.get('multipart_field', '')
    def normalize(value):
        return value.strip()
    montage = normalize(passage)
    parsed = json.loads(montage)
    return jsonify({'parsed': str(parsed)}), 200
