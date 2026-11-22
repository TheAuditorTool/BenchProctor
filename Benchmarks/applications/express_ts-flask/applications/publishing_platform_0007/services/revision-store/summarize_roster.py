# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("summarize_roster", __name__)


@bp.route("/summarize_roster", methods=["POST"])
def summarize_roster():
    remark = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(remark).split(','):
        parts.append(token.strip())
    byline = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if byline not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    addendum = '/var/app/data/' + byline
    Path(addendum).write_text('data')
    return jsonify({"result": "success"})
