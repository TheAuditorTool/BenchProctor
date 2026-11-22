# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("verify_threshold", __name__)


@bp.route("/verify_threshold", methods=["POST"])
def verify_threshold():
    caption = request.form.get('multipart_field', '')
    parts = str(caption).split(',')
    consignment = ' '.join(parts)
    parsed = json.loads(consignment)
    return jsonify({'parsed': str(parsed)}), 200
