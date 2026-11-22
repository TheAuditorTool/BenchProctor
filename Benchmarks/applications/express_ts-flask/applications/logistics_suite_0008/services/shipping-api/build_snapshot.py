# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("build_snapshot", __name__)


@bp.route("/build_snapshot", methods=["POST"])
def build_snapshot():
    caption = request.form.get('multipart_field', '')
    parts = str(caption).split(',')
    consignment = ' '.join(parts)
    parsed = json.loads(consignment)
    return jsonify({'parsed': str(parsed)}), 200
