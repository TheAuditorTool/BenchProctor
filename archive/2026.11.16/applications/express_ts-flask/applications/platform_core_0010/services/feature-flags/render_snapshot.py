# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("render_snapshot", __name__)


@bp.route("/render_snapshot", methods=["POST"])
def render_snapshot():
    notice = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(notice).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            persona = str(notice).strip()
        case _:
            persona = str(notice)
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return content
