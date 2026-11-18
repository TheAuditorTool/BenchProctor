# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("compact_record", __name__)


@bp.route("/compact_record", methods=["POST"])
def compact_record():
    remark = db.fetch_one('SELECT text FROM comments LIMIT 1')
    inquiry = f'{remark!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / inquiry).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    grievance = str(candidate)
    with open(grievance, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
