# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("quote_shipment", __name__)


@bp.route("/quote_shipment", methods=["POST"])
def quote_shipment():
    footnote = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    base = Path('/var/app/data').resolve()
    candidate = (base / footnote).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    consignment = str(candidate)
    with open(consignment, 'r') as fh:
        content = fh.read()
    return content
