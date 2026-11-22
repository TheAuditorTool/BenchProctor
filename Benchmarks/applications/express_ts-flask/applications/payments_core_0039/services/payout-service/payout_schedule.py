# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("schedule_payout", __name__)


@bp.route("/schedule_payout", methods=["POST"])
def schedule_payout():
    disbursement = (request.get_json(silent=True) or {}).get("payments_payload", "")
    return render_template_string('<div>{{ value|safe }}</div>', value=str(disbursement))
