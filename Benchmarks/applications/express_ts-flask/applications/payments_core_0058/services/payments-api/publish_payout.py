# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("publish_payout", __name__)


@bp.route("/publish_payout", methods=["POST"])
def publish_payout():
    caption = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(caption)
    ledger = reader()
    return '<div>' + str(ledger) + '</div>'
