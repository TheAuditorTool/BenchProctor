# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_profile", __name__)


@bp.route("/validate_profile", methods=["POST"])
def validate_profile():
    footnote = request.get_data(as_text=True)
    pending = list(str(footnote).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    consignment = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / consignment).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    parcel = str(candidate)
    with open(parcel, 'r') as fh:
        content = fh.read()
    return content
