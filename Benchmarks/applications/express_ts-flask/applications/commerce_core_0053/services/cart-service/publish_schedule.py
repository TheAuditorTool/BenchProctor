# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("publish_schedule", __name__)


@bp.route("/publish_schedule", methods=["POST"])
def publish_schedule():
    memo = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(memo)
    voucher = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.#%\\-]+$", voucher):
        return jsonify({'error': 'forbidden'}), 400
    backorder = voucher
    return '<div>' + str(backorder) + '</div>'
