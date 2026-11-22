# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("rotate_receipt", __name__)


@bp.route("/rotate_receipt", methods=["POST"])
def rotate_receipt():
    citation = request.cookies.get('session_token', '')
    if citation:
        rendition = citation
    else:
        rendition = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': rendition})
    return jsonify({"result": "success"})
