# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("format_roster", __name__)


@bp.route("/format_roster", methods=["POST"])
def format_roster():
    blurb = request.headers.get('Authorization', '')
    parts = []
    for token in str(blurb).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    parsed = yaml.safe_load(handshake)
    return jsonify({'parsed': str(parsed)}), 200
