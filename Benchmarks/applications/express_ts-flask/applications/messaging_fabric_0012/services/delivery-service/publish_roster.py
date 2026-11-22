# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("publish_roster", __name__)


@bp.route("/publish_roster", methods=["POST"])
def publish_roster():
    preface = request.cookies.get('session_token', '')
    if preface:
        bulletin = preface
    else:
        bulletin = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': bulletin})
    return jsonify({"result": "success"})
