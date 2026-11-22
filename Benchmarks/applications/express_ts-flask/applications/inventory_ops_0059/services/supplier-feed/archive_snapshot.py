# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("archive_snapshot", __name__)


@bp.route("/archive_snapshot", methods=["POST"])
def archive_snapshot():
    memo = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(memo)
    backorder = reader()
    with open('/var/app/data/' + str(backorder), 'r') as fh:
        content = fh.read()
    return content
