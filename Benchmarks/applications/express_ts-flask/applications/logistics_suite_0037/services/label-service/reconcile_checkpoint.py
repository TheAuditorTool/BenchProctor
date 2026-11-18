# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("reconcile_checkpoint", __name__)


@bp.route("/reconcile_checkpoint", methods=["POST"])
def reconcile_checkpoint():
    footnote = db.fetch_one('SELECT text FROM comments LIMIT 1')
    consignment = f'{footnote!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / consignment).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    parcel = str(candidate)
    with open(parcel, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
