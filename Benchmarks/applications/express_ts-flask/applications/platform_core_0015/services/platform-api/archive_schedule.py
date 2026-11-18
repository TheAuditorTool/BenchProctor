# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("archive_schedule", __name__)


@bp.route("/archive_schedule", methods=["POST"])
def archive_schedule():
    note = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(note)
    handshake = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    persona = handshake
    return '<div>' + str(persona) + '</div>'
