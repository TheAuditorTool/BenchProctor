# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("compact_window", __name__)


@bp.route("/compact_window", methods=["POST"])
def compact_window():
    footnote = request.files['upload'].filename
    if footnote:
        parcel = footnote
    else:
        parcel = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(parcel) + "'")
    return jsonify({"result": "success"})
