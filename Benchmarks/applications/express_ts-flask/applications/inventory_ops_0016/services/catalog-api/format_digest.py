# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("format_digest", __name__)


@bp.route("/format_digest", methods=["POST"])
def format_digest():
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(citation)
    backorder = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    restock = backorder
    return '<div>' + str(restock) + '</div>'
