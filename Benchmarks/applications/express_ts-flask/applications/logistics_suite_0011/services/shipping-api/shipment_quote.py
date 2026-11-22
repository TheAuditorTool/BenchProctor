# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("quote_shipment", __name__)


@bp.route("/quote_shipment", methods=["POST"])
def quote_shipment():
    caption = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    db.execute("SELECT * FROM users WHERE id = '" + str(caption) + "'")
    return jsonify({"result": "success"})
