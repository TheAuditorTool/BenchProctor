# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("resolve_index", __name__)


@bp.route("/resolve_index", methods=["POST"])
def resolve_index():
    preface = request.cookies.get('session_token', '')
    if preface:
        grievance = preface
    else:
        grievance = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': grievance})
    return jsonify({"result": "success"})
