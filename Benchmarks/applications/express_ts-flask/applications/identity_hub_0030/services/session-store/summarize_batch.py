# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("summarize_batch", __name__)


@bp.route("/summarize_batch", methods=["POST"])
def summarize_batch():
    tagline = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(tagline).split(','):
        parts.append(token.strip())
    persona = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if persona not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    note = '/var/app/data/' + persona
    Path(note).write_text('data')
    return jsonify({"result": "success"})
