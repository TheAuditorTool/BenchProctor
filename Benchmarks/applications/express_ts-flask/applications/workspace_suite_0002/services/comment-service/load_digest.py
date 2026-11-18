# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("load_digest", __name__)


@bp.route("/load_digest", methods=["POST"])
def load_digest():
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    heading = f'{transcript!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / heading).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    passage = str(candidate)
    with open(passage, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
