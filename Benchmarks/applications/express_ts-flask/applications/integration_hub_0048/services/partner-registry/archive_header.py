# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("archive_header", __name__)


@bp.route("/archive_header", methods=["POST"])
def archive_header():
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(citation).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if handshake not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    heading = '/var/app/data/' + handshake
    Path(heading).write_text('data')
    return jsonify({"result": "success"})
