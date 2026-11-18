# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("publish_summary", __name__)


@bp.route("/publish_summary", methods=["POST"])
def publish_summary():
    passage = request.get_data(as_text=True)
    dossier = passage.decode('utf-8', 'ignore') if isinstance(passage, bytes) else passage
    db.execute('SELECT * FROM users WHERE id = ?', (dossier,))
    return jsonify({"result": "success"})
