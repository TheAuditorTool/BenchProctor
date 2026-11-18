# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("render_article", __name__)


@bp.route("/render_article", methods=["POST"])
def render_article():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(summary)
    addendum = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", addendum):
        return jsonify({'error': 'forbidden'}), 400
    byline = addendum
    return '<div>' + str(byline) + '</div>'
