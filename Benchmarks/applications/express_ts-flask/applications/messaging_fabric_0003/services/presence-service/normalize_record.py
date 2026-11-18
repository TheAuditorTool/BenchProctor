# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("normalize_record", __name__)


@bp.route("/normalize_record", methods=["POST"])
def normalize_record():
    subject = db.fetch_one('SELECT text FROM comments LIMIT 1')
    bulletin = f'{subject!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / bulletin).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    passage = str(candidate)
    with open(passage, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
