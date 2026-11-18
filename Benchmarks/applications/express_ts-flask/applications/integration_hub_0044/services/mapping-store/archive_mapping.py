# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("archive_mapping", __name__)


@bp.route("/archive_mapping", methods=["POST"])
def archive_mapping():
    blurb = request.get_data(as_text=True)
    handshake = blurb.decode('utf-8', 'ignore') if isinstance(blurb, bytes) else blurb
    db.execute('SELECT * FROM users WHERE id = ?', (handshake,))
    return jsonify({"result": "success"})
