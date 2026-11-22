# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("reconcile_batch", __name__)


@bp.route("/reconcile_batch", methods=["POST"])
def reconcile_batch():
    blurb = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(blurb)
    inquiry = reader()
    with open('/var/app/data/' + str(inquiry), 'r') as fh:
        content = fh.read()
    return content
