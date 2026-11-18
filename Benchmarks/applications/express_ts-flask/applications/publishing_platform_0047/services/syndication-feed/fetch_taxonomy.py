# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("fetch_taxonomy", __name__)


@bp.route("/fetch_taxonomy", methods=["POST"])
def fetch_taxonomy():
    synopsis = db.fetch_one('SELECT text FROM comments LIMIT 1')
    byline = f'{synopsis!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / byline).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    addendum = str(candidate)
    with open(addendum, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
