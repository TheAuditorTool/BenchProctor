# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("enrich_header", __name__)


@bp.route("/enrich_header", methods=["POST"])
def enrich_header():
    headline = request.cookies.get('session_token', '')
    if headline:
        disbursement = headline
    else:
        disbursement = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': disbursement})
    return jsonify({"result": "success"})
