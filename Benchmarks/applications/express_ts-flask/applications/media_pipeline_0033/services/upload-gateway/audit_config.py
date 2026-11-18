# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("audit_config", __name__)


@bp.route("/audit_config", methods=["POST"])
def audit_config():
    transcript = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(transcript)
    rendition = reader()
    return '<div>' + str(rendition) + '</div>'
