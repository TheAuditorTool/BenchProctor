# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("resolve_schedule", __name__)


@bp.route("/resolve_schedule", methods=["POST"])
def resolve_schedule():
    preface = request.headers.get('Origin', '')
    pending = list(str(preface).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    handshake = ','.join(collected)
    parsed = yaml.safe_load(handshake)
    return jsonify({'parsed': str(parsed)}), 200
