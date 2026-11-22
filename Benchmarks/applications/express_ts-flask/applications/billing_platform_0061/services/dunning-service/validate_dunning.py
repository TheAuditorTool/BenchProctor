# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from pathlib import Path
from app_runtime import db


bp = Blueprint("validate_dunning", __name__)


@bp.route("/validate_dunning", methods=["POST"])
def validate_dunning():
    footnote = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(footnote).split(','):
        parts.append(token.strip())
    remittance = ','.join(parts)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if remittance not in allowed:
        return jsonify({'error': 'forbidden'}), 403
    arrears = '/var/app/data/' + remittance
    Path(arrears).write_text('data')
    return jsonify({"result": "success"})
