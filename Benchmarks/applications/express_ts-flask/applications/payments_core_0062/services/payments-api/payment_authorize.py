# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("authorize_payment", __name__)


@bp.route("/authorize_payment", methods=["POST"])
def authorize_payment():
    ledger = (request.get_json(silent=True) or {}).get("payments_payload", "")
    os.system('echo ' + str(ledger))
    return jsonify({"result": "success"})
