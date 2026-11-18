# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("build_header", __name__)


@bp.route("/build_header", methods=["POST"])
def build_header():
    summary = request.headers.get('Authorization', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    grievance = ','.join(parts)
    parsed = yaml.safe_load(grievance)
    return jsonify({'parsed': str(parsed)}), 200
