# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_report", __name__)


@bp.route("/publish_report", methods=["POST"])
def publish_report():
    synopsis = request.get_data(as_text=True)
    pending = list(str(synopsis).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    verdict = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / verdict).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    grievance = str(candidate)
    with open(grievance, 'r') as fh:
        content = fh.read()
    return content
