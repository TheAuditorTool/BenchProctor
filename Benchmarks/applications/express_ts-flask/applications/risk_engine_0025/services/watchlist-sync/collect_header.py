# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_header", __name__)


@bp.route("/collect_header", methods=["POST"])
def collect_header():
    excerpt = request.form.get('multipart_field', '')
    parts = str(excerpt).split(',')
    verdict = ' '.join(parts)
    parsed = json.loads(verdict)
    return jsonify({'parsed': str(parsed)}), 200
