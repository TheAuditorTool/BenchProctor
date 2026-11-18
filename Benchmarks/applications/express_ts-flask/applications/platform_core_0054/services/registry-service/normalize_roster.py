# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("normalize_roster", __name__)


@bp.route("/normalize_roster", methods=["POST"])
def normalize_roster():
    snippet = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = f'{snippet!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    handshake = str(candidate)
    with open(handshake, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
