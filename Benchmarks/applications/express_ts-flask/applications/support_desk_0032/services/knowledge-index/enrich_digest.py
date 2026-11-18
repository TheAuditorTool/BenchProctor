# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("enrich_digest", __name__)


@bp.route("/enrich_digest", methods=["POST"])
def enrich_digest():
    note = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(note)
    inquiry = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    return '<div>' + str(grievance) + '</div>'
