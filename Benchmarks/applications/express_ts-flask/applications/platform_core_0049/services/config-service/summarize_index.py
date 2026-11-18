# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_index", __name__)


@bp.route("/summarize_index", methods=["POST"])
def summarize_index():
    notice = request.headers.get('Authorization', '')
    parts = []
    for token in str(notice).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    parsed = yaml.safe_load(persona)
    return jsonify({'parsed': str(parsed)}), 200
