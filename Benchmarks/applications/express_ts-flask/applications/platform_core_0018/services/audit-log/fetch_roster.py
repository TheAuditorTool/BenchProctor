# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("fetch_roster", __name__)


@bp.route("/fetch_roster/<path_param>", methods=["POST"])
def fetch_roster(path_param):
    subtitle = path_param
    reader = make_reader(subtitle)
    persona = reader()
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (persona,))
    return jsonify({"result": "success"})
