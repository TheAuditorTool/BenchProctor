# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("collect_snapshot", __name__)


@bp.route("/collect_snapshot/<path_param>", methods=["POST"])
def collect_snapshot(path_param):
    preface = path_param
    reader = make_reader(preface)
    addendum = reader()
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (addendum,))
    return jsonify({"result": "success"})
