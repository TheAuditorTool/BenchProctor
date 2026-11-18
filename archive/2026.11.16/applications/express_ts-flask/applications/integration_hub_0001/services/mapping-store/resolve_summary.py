# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("resolve_summary", __name__)


@bp.route("/resolve_summary", methods=["POST"])
def resolve_summary():
    quotation = request.headers.get('Origin', '')
    pending = list(str(quotation).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    handshake = ','.join(collected)
    parsed = yaml.safe_load(handshake)
    return jsonify({'parsed': str(parsed)}), 200
