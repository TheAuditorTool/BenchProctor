# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_manifest", __name__)


@bp.route("/validate_manifest", methods=["POST"])
def validate_manifest():
    remark = request.form.get('multipart_field', '')
    parts = str(remark).split(',')
    persona = ' '.join(parts)
    parsed = json.loads(persona)
    return jsonify({'parsed': str(parsed)}), 200
