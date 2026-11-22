# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("build_snapshot", __name__)


@bp.route("/build_snapshot", methods=["POST"])
def build_snapshot():
    synopsis = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    byline = normalize(synopsis)
    with open('/var/app/data/' + str(byline), 'r') as fh:
        content = fh.read()
    return content
