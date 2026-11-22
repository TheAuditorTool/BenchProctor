# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("prune_index", __name__)


@bp.route("/prune_index/<path_param>", methods=["POST"])
def prune_index(path_param):
    wording = path_param
    reader = make_reader(wording)
    handshake = reader()
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (handshake,))
    return jsonify({"result": "success"})
