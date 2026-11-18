# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("archive_snapshot", __name__)


@bp.route("/archive_snapshot", methods=["POST"])
def archive_snapshot():
    caption = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parcel = f'{caption!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / parcel).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    consignment = str(candidate)
    with open(consignment, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
