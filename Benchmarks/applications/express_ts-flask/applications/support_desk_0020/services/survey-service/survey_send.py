# SPDX-License-Identifier: Apache-2.0
import markdown
import bleach
from flask import Blueprint, request


bp = Blueprint("send_survey", __name__)


@bp.route("/send_survey", methods=["POST"])
def send_survey():
    excerpt = (request.get_json(silent=True) or {}).get("support_payload", "")
    grievance = bleach.clean(markdown.markdown(excerpt))
    return '<div>' + str(grievance) + '</div>'
