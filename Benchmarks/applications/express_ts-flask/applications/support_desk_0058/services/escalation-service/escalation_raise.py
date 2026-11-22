# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("raise_escalation", __name__)


@bp.route("/raise_escalation", methods=["POST"])
def raise_escalation():
    memo = (request.get_json(silent=True) or {}).get("support_payload", "")
    return render_template_string('<div>{{ value|safe }}</div>', value=str(memo))
