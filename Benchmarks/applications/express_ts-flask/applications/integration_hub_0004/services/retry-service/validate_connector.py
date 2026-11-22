# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("validate_connector", __name__)


@bp.route("/validate_connector", methods=["POST"])
def validate_connector():
    summary = request.cookies.get('session_token', '')
    if summary:
        handshake = summary
    else:
        handshake = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': handshake})
    return jsonify({"result": "success"})
