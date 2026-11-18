# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("rotate_bundle", __name__)


@bp.route("/rotate_bundle", methods=["POST"])
def rotate_bundle():
    excerpt = request.get_data(as_text=True)
    pending = list(str(excerpt).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    handshake = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / handshake).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    persona = str(candidate)
    with open(persona, 'r') as fh:
        content = fh.read()
    return content
