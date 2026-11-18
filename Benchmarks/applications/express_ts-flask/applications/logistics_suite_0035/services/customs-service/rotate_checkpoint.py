# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db


bp = Blueprint("rotate_checkpoint", __name__)


@bp.route("/rotate_checkpoint", methods=["POST"])
def rotate_checkpoint():
    phrase = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(phrase).split(',')
    parcel = ' '.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(parcel) + "'")
    return jsonify({"result": "success"})
