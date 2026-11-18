# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("load_record", __name__)


@bp.route("/load_record", methods=["POST"])
def load_record():
    snippet = request.get_data(as_text=True)
    pending = list(str(snippet).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    persona = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    synopsis = str(candidate)
    with open(synopsis, 'r') as fh:
        content = fh.read()
    return content
