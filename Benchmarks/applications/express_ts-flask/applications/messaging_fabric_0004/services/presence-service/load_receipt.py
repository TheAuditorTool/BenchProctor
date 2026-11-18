# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("load_receipt", __name__)


@bp.route("/load_receipt", methods=["POST"])
def load_receipt():
    paragraph = request.get_data(as_text=True)
    bulletin = paragraph.decode('utf-8', 'ignore') if isinstance(paragraph, bytes) else paragraph
    db.execute('SELECT * FROM users WHERE id = ?', (bulletin,))
    return jsonify({"result": "success"})
