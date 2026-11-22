# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

bp = Blueprint("fetch_profile", __name__)


@bp.route("/fetch_profile", methods=["POST"])
def fetch_profile():
    citation = (request.get_json(silent=True) or {}).get('payload', '')
    reader = make_reader(citation)
    rendition = reader()
    with open('/var/app/data/' + str(rendition), 'r') as fh:
        content = fh.read()
    return content
