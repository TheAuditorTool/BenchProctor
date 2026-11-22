# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("collect_policy", __name__)


@bp.route("/collect_policy/<path_param>", methods=["POST"])
def collect_policy(path_param):
    preface = path_param
    reader = make_reader(preface)
    grievance = reader()
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (grievance,))
    return jsonify({"result": "success"})
