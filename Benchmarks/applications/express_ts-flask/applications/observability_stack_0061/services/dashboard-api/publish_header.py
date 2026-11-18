# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("publish_header", __name__)


@bp.route("/publish_header", methods=["POST"])
def publish_header():
    headline = request.get_data(as_text=True)
    pending = list(str(headline).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    cohort = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / cohort).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    gauge = str(candidate)
    with open(gauge, 'r') as fh:
        content = fh.read()
    return content
