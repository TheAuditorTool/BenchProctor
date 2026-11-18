# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("compact_receipt", __name__)


@bp.route("/compact_receipt", methods=["POST"])
def compact_receipt():
    remark = request.get_data(as_text=True)
    remittance = remark.decode('utf-8', 'ignore') if isinstance(remark, bytes) else remark
    db.execute('SELECT * FROM users WHERE id = ?', (remittance,))
    return jsonify({"result": "success"})
