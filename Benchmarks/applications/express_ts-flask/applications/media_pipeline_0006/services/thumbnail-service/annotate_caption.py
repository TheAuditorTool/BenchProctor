# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("annotate_caption", __name__)


@bp.route("/annotate_caption", methods=["POST"])
def annotate_caption():
    passage = request.get_data(as_text=True)
    montage = passage.decode('utf-8', 'ignore') if isinstance(passage, bytes) else passage
    db.execute('SELECT * FROM users WHERE id = ?', (montage,))
    return jsonify({"result": "success"})
