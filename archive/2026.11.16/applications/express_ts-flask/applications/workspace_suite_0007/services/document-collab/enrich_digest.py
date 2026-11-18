# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("enrich_digest", __name__)


@bp.route("/enrich_digest", methods=["POST"])
def enrich_digest():
    summary = request.headers.get('Origin', '')
    pending = list(str(summary).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    subtitle = ','.join(collected)
    parsed = yaml.safe_load(subtitle)
    return jsonify({'parsed': str(parsed)}), 200
