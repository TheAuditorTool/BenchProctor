# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("render_macro", __name__)


@bp.route("/render_macro", methods=["POST"])
def render_macro():
    phrase = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(phrase).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            inquiry = str(phrase).strip()
        case _:
            inquiry = str(phrase)
    with open('/var/app/data/' + str(inquiry), 'r') as fh:
        content = fh.read()
    return content
