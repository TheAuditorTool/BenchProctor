# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("run_reconciliation", __name__)


@bp.route("/run_reconciliation", methods=["POST"])
def run_reconciliation():
    ledger = (request.get_json(silent=True) or {}).get("payments_payload", "")
    return '<div>' + str(ledger) + '</div>'
