# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("resolve_batch", __name__)


@bp.route("/resolve_batch", methods=["POST"])
def resolve_batch():
    notice = request.get_data(as_text=True)
    persona = notice.decode('utf-8', 'ignore') if isinstance(notice, bytes) else notice
    db.execute('SELECT * FROM users WHERE id = ?', (persona,))
    return jsonify({"result": "success"})
