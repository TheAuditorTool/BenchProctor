# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("publish_receipt", __name__)


@bp.route("/publish_receipt", methods=["POST"])
def publish_receipt():
    excerpt = request.headers.get('X-Forwarded-For', '')
    kind = 'json' if str(excerpt).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            dossier = str(excerpt).strip()
        case _:
            dossier = str(excerpt)
    with open('/var/app/data/' + str(dossier), 'r') as fh:
        content = fh.read()
    return content
