# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("resolve_roster", __name__)


@bp.route("/resolve_roster", methods=["POST"])
def resolve_roster():
    heading = request.get_data(as_text=True)
    voucher = heading.decode('utf-8', 'ignore') if isinstance(heading, bytes) else heading
    db.execute('SELECT * FROM users WHERE id = ?', (voucher,))
    return jsonify({"result": "success"})
