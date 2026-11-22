# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("summarize_window", __name__)


@bp.route("/summarize_window", methods=["POST"])
def summarize_window():
    remark = request.cookies.get('session_token', '')
    if remark:
        persona = remark
    else:
        persona = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': persona})
    return jsonify({"result": "success"})
