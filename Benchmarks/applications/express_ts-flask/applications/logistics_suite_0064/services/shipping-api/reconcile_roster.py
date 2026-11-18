# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("reconcile_roster", __name__)


@bp.route("/reconcile_roster", methods=["POST"])
def reconcile_roster():
    transcript = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(transcript)
    parcel = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", parcel):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    return '<div>' + str(consignment) + '</div>'
