# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("annotate_secret", __name__)


@bp.route("/annotate_secret", methods=["POST"])
def annotate_secret():
    passage = request.get_data(as_text=True)
    persona = passage.decode('utf-8', 'ignore') if isinstance(passage, bytes) else passage
    db.execute('SELECT * FROM users WHERE id = ?', (persona,))
    return jsonify({"result": "success"})
