# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("collect_digest", __name__)


@bp.route("/collect_digest", methods=["POST"])
def collect_digest():
    footnote = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    wording = normalize(footnote)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", wording):
        return jsonify({'error': 'forbidden'}), 400
    note = wording
    db.execute("SELECT * FROM users WHERE id = '" + str(note) + "'")
    return jsonify({"result": "success"})
