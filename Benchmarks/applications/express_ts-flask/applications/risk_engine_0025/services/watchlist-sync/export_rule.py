# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, request, jsonify


bp = Blueprint("export_rule", __name__)


@bp.route("/export_rule", methods=["POST"])
def export_rule():
    excerpt = request.form.get('multipart_field', '')
    parts = str(excerpt).split(',')
    verdict = ' '.join(parts)
    parsed = json.loads(verdict)
    return jsonify({'parsed': str(parsed)}), 200
