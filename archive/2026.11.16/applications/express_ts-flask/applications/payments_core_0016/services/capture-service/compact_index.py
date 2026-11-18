# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("compact_index", __name__)


@bp.route("/compact_index", methods=["POST"])
def compact_index():
    passage = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(passage).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            remittance = str(passage).strip()
        case _:
            remittance = str(passage)
    with open('/var/app/data/' + str(remittance), 'r') as fh:
        content = fh.read()
    return content
