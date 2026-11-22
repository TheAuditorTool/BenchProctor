# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("render_header", __name__)


@bp.route("/render_header", methods=["POST"])
def render_header():
    phrase = request.cookies.get('session_token', '')
    if phrase:
        grievance = phrase
    else:
        grievance = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': grievance})
    return jsonify({"result": "success"})
