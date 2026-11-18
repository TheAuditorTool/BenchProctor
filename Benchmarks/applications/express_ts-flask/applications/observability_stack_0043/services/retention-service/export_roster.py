# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("export_roster", __name__)


@bp.route("/export_roster", methods=["POST"])
def export_roster():
    note = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(note)
    gauge = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", gauge):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    return '<div>' + str(cohort) + '</div>'
