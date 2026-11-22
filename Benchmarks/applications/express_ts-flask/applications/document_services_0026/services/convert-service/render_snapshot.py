# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("render_snapshot", __name__)


@bp.route("/render_snapshot", methods=["POST"])
def render_snapshot():
    preface = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(preface)
    addendum = reader()
    with open('/var/app/data/' + str(addendum), 'r') as fh:
        content = fh.read()
    return content
