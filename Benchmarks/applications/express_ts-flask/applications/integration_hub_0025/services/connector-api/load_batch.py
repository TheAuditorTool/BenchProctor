# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("load_batch", __name__)


@bp.route("/load_batch", methods=["POST"])
def load_batch():
    footnote = request.get_data(as_text=True)
    pending = list(str(footnote).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    handshake = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    blurb = str(candidate)
    with open(blurb, 'r') as fh:
        content = fh.read()
    return content
