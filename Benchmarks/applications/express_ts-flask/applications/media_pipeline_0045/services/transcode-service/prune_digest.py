# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_digest", __name__)


@bp.route("/prune_digest", methods=["POST"])
def prune_digest():
    notice = request.get_data(as_text=True)
    pending = list(str(notice).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    rendition = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / rendition).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    montage = str(candidate)
    with open(montage, 'r') as fh:
        content = fh.read()
    return content
