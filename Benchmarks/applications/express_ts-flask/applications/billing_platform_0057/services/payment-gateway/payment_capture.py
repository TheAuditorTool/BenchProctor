# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("capture_payment", __name__)


@bp.route("/capture_payment", methods=["POST"])
def capture_payment():
    arrears = (request.get_json(silent=True) or {}).get("billing_payload", "")
    return render_template_string('<div>{{ value|safe }}</div>', value=str(arrears))
