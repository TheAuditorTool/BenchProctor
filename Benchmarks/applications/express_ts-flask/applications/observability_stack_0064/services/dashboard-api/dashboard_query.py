# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("query_dashboard", __name__)


@bp.route("/query_dashboard", methods=["POST"])
def query_dashboard():
    paragraph = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    return render_template_string('<div>{{ value|safe }}</div>', value=str(paragraph))
