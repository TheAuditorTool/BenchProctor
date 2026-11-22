# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("normalize_invoice", __name__)


@bp.route("/normalize_invoice", methods=["POST"])
def normalize_invoice():
    caption = request.cookies.get('session_token', '')
    if caption:
        remittance = caption
    else:
        remittance = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': remittance})
    return jsonify({"result": "success"})
