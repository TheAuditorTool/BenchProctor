# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("append_audit", __name__)


@bp.route("/append_audit", methods=["POST"])
def append_audit():
    heading = (request.get_json(silent=True) or {}).get("platform_payload", "")
    handshake = bleach.clean(markdown.markdown(heading))
    return '<div>' + str(handshake) + '</div>'
