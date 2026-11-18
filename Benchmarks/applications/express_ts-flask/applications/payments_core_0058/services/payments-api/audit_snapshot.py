# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("audit_snapshot", __name__)


@bp.route("/audit_snapshot", methods=["POST"])
def audit_snapshot():
    caption = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ledger = f'{caption!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / ledger).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    remittance = str(candidate)
    with open(remittance, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
