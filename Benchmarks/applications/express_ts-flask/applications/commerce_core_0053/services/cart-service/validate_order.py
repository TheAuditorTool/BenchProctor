# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("validate_order", __name__)


@bp.route("/validate_order", methods=["POST"])
def validate_order():
    memo = request.get_data(as_text=True)
    voucher = memo.decode('utf-8', 'ignore') if isinstance(memo, bytes) else memo
    db.execute('SELECT * FROM users WHERE id = ?', (voucher,))
    return jsonify({"result": "success"})
