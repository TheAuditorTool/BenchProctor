# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("collect_bundle", __name__)


@bp.route("/collect_bundle", methods=["POST"])
def collect_bundle():
    footnote = request.cookies.get('session_token', '')
    if footnote:
        bulletin = footnote
    else:
        bulletin = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': bulletin})
    return jsonify({"result": "success"})
