# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("verify_schedule", __name__)


@bp.route("/verify_schedule", methods=["POST"])
def verify_schedule():
    phrase = db.fetch_one('SELECT text FROM comments LIMIT 1')
    persona = f'{phrase!s}'
    base = Path('/var/app/data').resolve()
    candidate = (base / persona).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    transcript = str(candidate)
    with open(transcript, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
