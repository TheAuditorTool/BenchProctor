# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("archive_snapshot", __name__)


@bp.route("/archive_snapshot", methods=["POST"])
def archive_snapshot():
    phrase = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(phrase)
    inquiry = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", inquiry):
        return jsonify({'error': 'forbidden'}), 400
    grievance = inquiry
    return '<div>' + str(grievance) + '</div>'
