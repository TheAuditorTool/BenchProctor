# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, request, jsonify


bp = Blueprint("dispatch_delivery", __name__)


@bp.route("/dispatch_delivery", methods=["POST"])
def dispatch_delivery():
    preface = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    base = Path('/var/app/data').resolve()
    candidate = (base / preface).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    heading = str(candidate)
    with open(heading, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
