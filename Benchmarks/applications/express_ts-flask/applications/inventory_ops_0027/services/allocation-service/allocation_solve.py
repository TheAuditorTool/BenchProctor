# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("solve_allocation", __name__)


@bp.route("/solve_allocation", methods=["POST"])
def solve_allocation():
    headline = (request.get_json(silent=True) or {}).get("inventory_payload", "")
    with open('/var/app/data/' + str(headline), 'r') as fh:
        content = fh.read()
    return content
