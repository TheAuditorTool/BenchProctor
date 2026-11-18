# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("build_roster", __name__)


@bp.route("/build_roster", methods=["POST"])
def build_roster():
    passage = request.get_data(as_text=True)
    montage = passage.decode('utf-8', 'ignore') if isinstance(passage, bytes) else passage
    db.execute('SELECT * FROM users WHERE id = ?', (montage,))
    return jsonify({"result": "success"})
