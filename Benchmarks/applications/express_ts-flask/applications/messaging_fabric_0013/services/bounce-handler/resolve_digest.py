# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("resolve_digest", __name__)


@bp.route("/resolve_digest", methods=["POST"])
def resolve_digest():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(summary)
    bulletin = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    snippet = bulletin
    return '<div>' + str(snippet) + '</div>'
