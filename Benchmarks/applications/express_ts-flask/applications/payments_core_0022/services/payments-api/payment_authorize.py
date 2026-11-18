# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("authorize_payment", __name__)


@bp.route("/authorize_payment", methods=["POST"])
def authorize_payment():
    remittance = (request.get_json(silent=True) or {}).get("payments_payload", "")
    requests.get(str(remittance))
    return jsonify({"result": "success"})
