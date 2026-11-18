# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("prune_report", __name__)


@bp.route("/prune_report", methods=["POST"])
def prune_report():
    remark = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    remittance = normalize(remark)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", remittance):
        return jsonify({'error': 'forbidden'}), 400
    arrears = remittance
    db.execute("SELECT * FROM users WHERE id = '" + str(arrears) + "'")
    return jsonify({"result": "success"})
