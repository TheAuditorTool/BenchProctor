# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("reconcile_policy", __name__)


@bp.route("/reconcile_policy", methods=["POST"])
def reconcile_policy():
    heading = request.cookies.get('session_token', '')
    if heading:
        handshake = heading
    else:
        handshake = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': handshake})
    return jsonify({"result": "success"})
