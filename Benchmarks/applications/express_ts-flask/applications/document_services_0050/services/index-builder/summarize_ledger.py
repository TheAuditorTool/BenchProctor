# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import DB_PATH
from sqlalchemy import create_engine


_engine = create_engine("sqlite:///" + DB_PATH)

bp = Blueprint("summarize_ledger", __name__)


@bp.route("/summarize_ledger", methods=["POST"])
def summarize_ledger():
    citation = request.cookies.get('session_token', '')
    if citation:
        dossier = citation
    else:
        dossier = ''
    with _engine.connect() as conn:
        conn.exec_driver_sql('SELECT * FROM users WHERE id = :id', {'id': dossier})
    return jsonify({"result": "success"})
