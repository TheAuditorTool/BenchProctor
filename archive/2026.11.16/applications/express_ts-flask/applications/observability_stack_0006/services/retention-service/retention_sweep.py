# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("sweep_retention", __name__)


@bp.route("/sweep_retention", methods=["POST"])
def sweep_retention():
    caption = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    return '<div>' + str(caption) + '</div>'
