# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request


bp = Blueprint("convert_fx", __name__)


@bp.route("/convert_fx", methods=["POST"])
def convert_fx():
    ledger = (request.get_json(silent=True) or {}).get("payments_payload", "")
    return '<div>' + str(ledger) + '</div>'
