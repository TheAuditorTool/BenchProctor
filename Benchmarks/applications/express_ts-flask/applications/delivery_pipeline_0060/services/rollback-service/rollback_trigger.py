# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("trigger_rollback", __name__)


@bp.route("/trigger_rollback", methods=["POST"])
def trigger_rollback():
    subtitle = (request.get_json(silent=True) or {}).get("delivery_payload", "")
    return '<div>' + str(subtitle) + '</div>'
