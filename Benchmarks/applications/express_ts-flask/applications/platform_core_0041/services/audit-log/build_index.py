# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("build_index", __name__)


@bp.route("/build_index", methods=["POST"])
def build_index():
    passage = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(passage)
    persona = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    return '<div>' + str(handshake) + '</div>'
