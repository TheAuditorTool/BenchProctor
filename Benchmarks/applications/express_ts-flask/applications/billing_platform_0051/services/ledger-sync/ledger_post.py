# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("post_ledger_entry", __name__)


@bp.route("/post_ledger_entry", methods=["POST"])
def post_ledger_entry():
    remittance = (request.get_json(silent=True) or {}).get("billing_payload", "")
    return '<div>' + str(remittance) + '</div>'
