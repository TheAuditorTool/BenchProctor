# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("enrich_window", __name__)


@bp.route("/enrich_window", methods=["POST"])
def enrich_window():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(summary)
    cohort = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", cohort):
        return jsonify({'error': 'forbidden'}), 400
    gauge = cohort
    return '<div>' + str(gauge) + '</div>'
