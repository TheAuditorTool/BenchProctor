# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("load_metric", __name__)


@bp.route("/load_metric", methods=["POST"])
def load_metric():
    paragraph = request.cookies.get('session_token', '')
    if paragraph:
        gauge = paragraph
    else:
        gauge = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': gauge})
    return jsonify({"result": "success"})
