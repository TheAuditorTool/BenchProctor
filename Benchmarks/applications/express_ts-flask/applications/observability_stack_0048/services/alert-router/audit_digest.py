# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_digest", __name__)


@bp.route("/audit_digest", methods=["POST"])
def audit_digest():
    excerpt = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(excerpt)
    gauge = reader()
    return '<div>' + str(gauge) + '</div>'
