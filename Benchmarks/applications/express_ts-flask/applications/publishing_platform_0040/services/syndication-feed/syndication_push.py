# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("push_syndication", __name__)


@bp.route("/push_syndication", methods=["POST"])
def push_syndication():
    subtitle = (request.get_json(silent=True) or {}).get("publishing_payload", "")
    return render_template_string('<div>{{ value|safe }}</div>', value=str(subtitle))
