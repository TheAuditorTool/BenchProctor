# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("reconcile_report", __name__)


@bp.route("/reconcile_report", methods=["POST"])
def reconcile_report():
    synopsis = request.cookies.get('session_token', '')
    if synopsis:
        rendition = synopsis
    else:
        rendition = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': rendition})
    return jsonify({"result": "success"})
