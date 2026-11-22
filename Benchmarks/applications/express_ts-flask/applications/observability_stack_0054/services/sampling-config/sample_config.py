# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("configure_sample", __name__)


@bp.route("/configure_sample", methods=["POST"])
def configure_sample():
    paragraph = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    return render_template_string('{{ value }}', value=paragraph)
