# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("archive_schedule", __name__)


@bp.route("/archive_schedule", methods=["POST"])
def archive_schedule():
    summary = request.headers.get('Authorization', '')
    parts = []
    for token in str(summary).split(','):
        parts.append(token.strip())
    grievance = ','.join(parts)
    parsed = yaml.safe_load(grievance)
    return jsonify({'parsed': str(parsed)}), 200
