# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("verify_record", __name__)


@bp.route("/verify_record", methods=["POST"])
def verify_record():
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    rendition = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if rendition not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    montage = '/var/app/data/' + rendition
    Path(montage).write_text('data')
    return jsonify({"result": "success"})
