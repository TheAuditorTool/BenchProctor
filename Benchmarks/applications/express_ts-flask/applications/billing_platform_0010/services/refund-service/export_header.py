# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("export_header", __name__)


@bp.route("/export_header", methods=["POST"])
def export_header():
    headline = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(headline).split(','):
        parts.append(token.strip())
    remittance = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if remittance not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    dunning = '/var/app/data/' + remittance
    Path(dunning).write_text('data')
    return jsonify({"result": "success"})
