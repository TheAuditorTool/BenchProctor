# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("enrich_summary", __name__)


@bp.route("/enrich_summary", methods=["POST"])
def enrich_summary():
    wording = request.cookies.get('session_token', '')
    if wording:
        consignment = wording
    else:
        consignment = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': consignment})
    return jsonify({"result": "success"})
