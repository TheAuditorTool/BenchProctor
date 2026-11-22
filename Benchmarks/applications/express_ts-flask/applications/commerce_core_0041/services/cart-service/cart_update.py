# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import base64
import pickle


bp = Blueprint("update_cart", __name__)


@bp.route("/update_cart", methods=["POST"])
def update_cart():
    subtitle = (request.get_json(silent=True) or {}).get("orders_payload", "")
    pickle.loads(base64.b64decode(subtitle))
    return jsonify({"result": "success"})
