# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("request_return", __name__)


@bp.route("/request_return", methods=["POST"])
def request_return():
    transcript = (request.get_json(silent=True) or {}).get("orders_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", transcript):
        return jsonify({'error': 'forbidden'}), 400
    voucher = transcript
    db.execute("SELECT * FROM users WHERE id = '" + str(voucher) + "'")
    return jsonify({"result": "success"})
