# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_snapshot", __name__)


@bp.route("/publish_snapshot", methods=["POST"])
def publish_snapshot():
    quotation = request.headers.get('Origin', '')
    pending = list(str(quotation).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    handshake = ','.join(collected)
    parsed = yaml.safe_load(handshake)
    return jsonify({'parsed': str(parsed)}), 200
