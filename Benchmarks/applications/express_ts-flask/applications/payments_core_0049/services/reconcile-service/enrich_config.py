# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


def make_reader(raw):
    def read():
        return raw.strip()
    return read
_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("enrich_config", __name__)


@bp.route("/enrich_config/<path_param>", methods=["POST"])
def enrich_config(path_param):
    headline = path_param
    reader = make_reader(headline)
    disbursement = reader()
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = ?', (disbursement,))
    return jsonify({"result": "success"})
