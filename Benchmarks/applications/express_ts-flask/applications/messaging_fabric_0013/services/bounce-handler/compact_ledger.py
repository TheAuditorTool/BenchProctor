# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("compact_ledger", __name__)


@bp.route("/compact_ledger", methods=["POST"])
def compact_ledger():
    summary = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(summary)
    bulletin = reader()
    return '<div>' + str(bulletin) + '</div>'
