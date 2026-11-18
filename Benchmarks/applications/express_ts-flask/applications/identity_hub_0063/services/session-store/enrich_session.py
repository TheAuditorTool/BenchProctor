# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_session", __name__)


@bp.route("/enrich_session", methods=["POST"])
def enrich_session():
    paragraph = request.headers.get('Authorization', '')
    parts = []
    for token in str(paragraph).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    parsed = yaml.safe_load(persona)
    return jsonify({'parsed': str(parsed)}), 200
