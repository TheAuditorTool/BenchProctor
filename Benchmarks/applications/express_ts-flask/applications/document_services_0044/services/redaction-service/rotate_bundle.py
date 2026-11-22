# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import db
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("rotate_bundle", __name__)


@bp.route("/rotate_bundle", methods=["POST"])
def rotate_bundle():
    phrase = db.fetch_one('SELECT name FROM users LIMIT 1')
    dossier = json.loads(phrase).get('value', '')
    with _engine.connect() as conn:
        conn.exec_driver_sql("SELECT * FROM users WHERE name = '" + str(dossier) + "'")
    return jsonify({"result": "success"})
