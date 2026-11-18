# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("load_threshold", __name__)


@bp.route("/load_threshold", methods=["POST"])
def load_threshold():
    passage = request.get_data(as_text=True)
    pending = list(str(passage).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    montage = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / montage).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    rendition = str(candidate)
    with open(rendition, 'r') as fh:
        content = fh.read()
    return content
