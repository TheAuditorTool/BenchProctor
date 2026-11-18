# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("prune_receipt", __name__)


@bp.route("/prune_receipt", methods=["POST"])
def prune_receipt():
    heading = request.get_data(as_text=True)
    pending = list(str(heading).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    voucher = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / voucher).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    backorder = str(candidate)
    with open(backorder, 'r') as fh:
        content = fh.read()
    return content
