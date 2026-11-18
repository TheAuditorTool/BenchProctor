# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_header", __name__)


@bp.route("/audit_header", methods=["POST"])
def audit_header():
    citation = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(citation)
    parcel = reader()
    return '<div>' + str(parcel) + '</div>'
