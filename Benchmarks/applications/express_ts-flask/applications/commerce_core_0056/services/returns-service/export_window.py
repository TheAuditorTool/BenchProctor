# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("export_window", __name__)


@bp.route("/export_window", methods=["POST"])
def export_window():
    citation = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    backorder = normalize(citation)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", backorder):
        return jsonify({'error': 'forbidden'}), 400
    voucher = backorder
    db.execute("SELECT * FROM users WHERE id = '" + str(voucher) + "'")
    return jsonify({"result": "success"})
