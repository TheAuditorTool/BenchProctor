# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request
from flask import render_template_string


bp = Blueprint("apply_promo", __name__)


@bp.route("/apply_promo", methods=["POST"])
def apply_promo():
    phrase = (request.get_json(silent=True) or {}).get("orders_payload", "")
    return render_template_string('<div>{{ value|safe }}</div>', value=str(phrase))
