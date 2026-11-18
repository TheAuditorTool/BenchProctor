# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


bp = Blueprint("authorize_payment", __name__)


@bp.route("/authorize_payment", methods=["POST"])
def authorize_payment():
    disbursement = (request.get_json(silent=True) or {}).get("payments_payload", "")
    pickle.loads(base64.b64decode(disbursement))
    return jsonify({"result": "success"})
