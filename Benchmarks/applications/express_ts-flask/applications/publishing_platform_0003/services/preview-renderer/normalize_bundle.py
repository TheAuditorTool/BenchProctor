# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("normalize_bundle", __name__)


@bp.route("/normalize_bundle", methods=["POST"])
def normalize_bundle():
    heading = request.cookies.get('session_token', '')
    if heading:
        addendum = heading
    else:
        addendum = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': addendum})
    return jsonify({"result": "success"})
