# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("prune_roster", __name__)


@bp.route("/prune_roster", methods=["POST"])
def prune_roster():
    preface = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(preface)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    notice = bulletin
    db.execute("SELECT * FROM users WHERE id = '" + str(notice) + "'")
    return jsonify({"result": "success"})
