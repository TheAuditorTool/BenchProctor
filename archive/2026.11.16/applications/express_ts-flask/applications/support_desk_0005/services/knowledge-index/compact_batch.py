# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_batch", __name__)


@bp.route("/compact_batch", methods=["POST"])
def compact_batch():
    phrase = request.headers.get('Origin', '')
    pending = list(str(phrase).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    inquiry = ','.join(collected)
    parsed = yaml.safe_load(inquiry)
    return jsonify({'parsed': str(parsed)}), 200
