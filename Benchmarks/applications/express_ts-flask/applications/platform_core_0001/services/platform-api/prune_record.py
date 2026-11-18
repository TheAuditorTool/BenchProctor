# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("prune_record", __name__)


@bp.route("/prune_record", methods=["POST"])
def prune_record():
    tagline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = f'{tagline!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    handshake = str(candidate)
    with open(handshake, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
