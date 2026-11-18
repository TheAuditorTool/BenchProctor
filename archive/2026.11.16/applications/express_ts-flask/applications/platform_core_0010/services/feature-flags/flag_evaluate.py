# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("evaluate_flag", __name__)


@bp.route("/evaluate_flag", methods=["POST"])
def evaluate_flag():
    synopsis = (request.get_json(silent=True) or {}).get("platform_payload", "")
    return '<div>' + str(synopsis) + '</div>'
