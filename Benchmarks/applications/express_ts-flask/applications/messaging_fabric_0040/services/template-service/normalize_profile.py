# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("normalize_profile", __name__)


@bp.route("/normalize_profile", methods=["POST"])
def normalize_profile():
    preface = request.get_data(as_text=True)
    pending = list(str(preface).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    bulletin = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / bulletin).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    notice = str(candidate)
    with open(notice, 'r') as fh:
        content = fh.read()
    return content
