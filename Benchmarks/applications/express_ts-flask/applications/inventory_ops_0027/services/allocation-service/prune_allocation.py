# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("prune_allocation", __name__)


@bp.route("/prune_allocation", methods=["POST"])
def prune_allocation():
    summary = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(summary)
    restock = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", restock):
        return jsonify({'error': 'forbidden'}), 400
    backorder = restock
    return '<div>' + str(backorder) + '</div>'
