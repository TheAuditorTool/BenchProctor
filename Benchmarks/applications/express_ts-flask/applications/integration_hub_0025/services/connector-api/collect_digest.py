# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_digest", __name__)


@bp.route("/collect_digest", methods=["POST"])
def collect_digest():
    footnote = request.headers.get('Authorization', '')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    parsed = yaml.safe_load(handshake)
    return jsonify({'parsed': str(parsed)}), 200
