# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("export_window", __name__)


@bp.route("/export_window", methods=["POST"])
def export_window():
    transcript = request.get_data(as_text=True)
    rendition = transcript.decode('utf-8', 'ignore') if isinstance(transcript, bytes) else transcript
    db.execute('SELECT * FROM users WHERE id = ?', (rendition,))
    return jsonify({"result": "success"})
