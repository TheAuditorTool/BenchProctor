# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("archive_ledger", __name__)


@bp.route("/archive_ledger", methods=["POST"])
def archive_ledger():
    citation = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(citation)
    backorder = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    voucher = backorder
    return '<div>' + str(voucher) + '</div>'
