# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("load_index", __name__)


@bp.route("/load_index", methods=["POST"])
def load_index():
    caption = request.args.get('id', '')
    if caption:
        cohort = caption
    else:
        cohort = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(cohort) + "'")
    return jsonify({"result": "success"})
