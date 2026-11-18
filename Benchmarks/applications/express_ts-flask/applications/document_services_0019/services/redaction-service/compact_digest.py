# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("compact_digest", __name__)


@bp.route("/compact_digest", methods=["POST"])
def compact_digest():
    passage = request.args.get('id', '')
    if passage:
        dossier = passage
    else:
        dossier = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(dossier) + "'")
    return jsonify({"result": "success"})
