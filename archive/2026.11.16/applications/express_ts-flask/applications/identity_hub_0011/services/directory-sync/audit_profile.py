# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("audit_profile", __name__)


@bp.route("/audit_profile", methods=["POST"])
def audit_profile():
    excerpt = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(excerpt).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            persona = str(excerpt).strip()
        case _:
            persona = str(excerpt)
    with open('/var/app/data/' + str(persona), 'r') as fh:
        content = fh.read()
    return content
