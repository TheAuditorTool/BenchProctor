# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("run_screening", __name__)


@bp.route("/run_screening", methods=["POST"])
def run_screening():
    remark = (request.get_json(silent=True) or {}).get("risk_payload", "")
    return '<div>' + str(remark) + '</div>'
