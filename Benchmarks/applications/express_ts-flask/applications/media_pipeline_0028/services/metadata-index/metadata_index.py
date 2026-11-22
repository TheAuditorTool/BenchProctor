# SPDX-License-Identifier: Apache-2.0
import html
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("index_metadata", __name__)


@bp.route("/index_metadata", methods=["POST"])
def index_metadata():
    heading = (request.get_json(silent=True) or {}).get("media_payload", "")
    montage = html.escape(heading)
    return render_template_string('<div>{{ value|safe }}</div>', value=str(montage))
