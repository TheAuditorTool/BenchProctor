# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("compact_digest", __name__)


@bp.route("/compact_digest", methods=["POST"])
def compact_digest():
    paragraph = request.args.get('id', '')
    if paragraph:
        persona = paragraph
    else:
        persona = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return jsonify({"result": "success"})
