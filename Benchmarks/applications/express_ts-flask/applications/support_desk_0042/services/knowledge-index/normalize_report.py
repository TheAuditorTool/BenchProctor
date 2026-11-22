# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("normalize_report", __name__)


@bp.route("/normalize_report", methods=["POST"])
def normalize_report():
    blurb = request.cookies.get('session_token', '')
    if blurb:
        inquiry = blurb
    else:
        inquiry = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': inquiry})
    return jsonify({"result": "success"})
