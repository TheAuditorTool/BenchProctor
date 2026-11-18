# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("merge_summary", __name__)


@bp.route("/merge_summary", methods=["POST"])
def merge_summary():
    transcript = request.headers.get('Authorization', '')
    parts = []
    for token in str(transcript).split(','):
        parts.append(token.strip())
    rendition = ','.join(parts)
    parsed = yaml.safe_load(rendition)
    return jsonify({'parsed': str(parsed)}), 200
