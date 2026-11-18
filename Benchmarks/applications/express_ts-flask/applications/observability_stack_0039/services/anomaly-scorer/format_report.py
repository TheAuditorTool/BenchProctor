# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("format_report", __name__)


@bp.route("/format_report", methods=["POST"])
def format_report():
    caption = request.get_data(as_text=True)
    cohort = caption.decode('utf-8', 'ignore') if isinstance(caption, bytes) else caption
    db.execute('SELECT * FROM users WHERE id = ?', (cohort,))
    return jsonify({"result": "success"})
