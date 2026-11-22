# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("merge_ledger", __name__)


@bp.route("/merge_ledger", methods=["POST"])
def merge_ledger():
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    bulletin = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if bulletin not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    snippet = '/var/app/data/' + bulletin
    Path(snippet).write_text('data')
    return jsonify({"result": "success"})
