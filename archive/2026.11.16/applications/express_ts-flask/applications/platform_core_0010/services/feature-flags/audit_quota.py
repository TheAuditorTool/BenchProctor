# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("audit_quota", __name__)


@bp.route("/audit_quota", methods=["POST"])
def audit_quota():
    notice = request.headers.get('Origin', '')
    pending = list(str(notice).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    persona = ','.join(collected)
    parsed = yaml.safe_load(persona)
    return jsonify({'parsed': str(parsed)}), 200
