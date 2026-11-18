# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("format_policy", __name__)


@bp.route("/format_policy", methods=["POST"])
def format_policy():
    footnote = request.headers.get('Authorization', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    parsed = yaml.safe_load(handshake)
    return jsonify({'parsed': str(parsed)}), 200
