# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("resolve_config", __name__)


@bp.route("/resolve_config", methods=["POST"])
def resolve_config():
    notice = request.get_data(as_text=True)
    persona = notice.decode('utf-8', 'ignore') if isinstance(notice, bytes) else notice
    db.execute('SELECT * FROM users WHERE id = ?', (persona,))
    return jsonify({"result": "success"})
