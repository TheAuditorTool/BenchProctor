# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("load_escalation", __name__)


@bp.route("/load_escalation/<path_param>", methods=["POST"])
def load_escalation(path_param):
    snippet = path_param
    reader = make_reader(snippet)
    inquiry = reader()
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (inquiry,))
    return jsonify({"result": "success"})
