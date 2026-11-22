# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request


bp = Blueprint("invoke_connector", __name__)


@bp.route("/invoke_connector", methods=["POST"])
def invoke_connector():
    excerpt = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    subject = os.path.join('/var/app/data', os.path.basename(excerpt))
    with open(subject, 'r') as fh:
        content = fh.read()
    return content
