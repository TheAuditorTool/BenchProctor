# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("format_summary", __name__)


@bp.route("/format_summary", methods=["POST"])
def format_summary():
    excerpt = request.headers.get('Origin', '')
    pending = list(str(excerpt).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    dossier = ','.join(collected)
    parsed = yaml.safe_load(dossier)
    return jsonify({'parsed': str(parsed)}), 200
