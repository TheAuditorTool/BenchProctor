# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("load_threshold", __name__)


@bp.route("/load_threshold", methods=["POST"])
def load_threshold():
    caption = db.fetch_one('SELECT text FROM comments LIMIT 1')
    gauge = f'{caption!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / gauge).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    cohort = str(candidate)
    with open(cohort, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
