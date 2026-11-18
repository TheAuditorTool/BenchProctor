# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("load_roster", __name__)


@bp.route("/load_roster", methods=["POST"])
def load_roster():
    summary = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(summary).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            subtitle = str(summary).strip()
        case _:
            subtitle = str(summary)
    with open('/var/app/data/' + str(subtitle), 'r') as fh:
        content = fh.read()
    return content
