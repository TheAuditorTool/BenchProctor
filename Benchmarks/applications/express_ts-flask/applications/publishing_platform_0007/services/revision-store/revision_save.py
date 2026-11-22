# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("save_revision", __name__)


@bp.route("/save_revision", methods=["POST"])
def save_revision():
    transcript = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    with open('/var/app/data/' + str(transcript), 'r') as fh:
        content = fh.read()
    return content
