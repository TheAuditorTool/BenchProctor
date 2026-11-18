# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("collect_manifest", __name__)


@bp.route("/collect_manifest", methods=["POST"])
def collect_manifest():
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
    handshake = str(candidate)
    with open(handshake, 'r') as fh:
        content = fh.read()
    return content
