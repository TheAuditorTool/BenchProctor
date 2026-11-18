# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_index", __name__)


@bp.route("/compact_index", methods=["POST"])
def compact_index():
    transcript = request.headers.get('Authorization', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    backorder = ','.join(parts)
    parsed = yaml.safe_load(backorder)
    return jsonify({'parsed': str(parsed)}), 200
