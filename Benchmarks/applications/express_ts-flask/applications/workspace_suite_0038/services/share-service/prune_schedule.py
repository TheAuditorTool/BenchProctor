# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("prune_schedule", __name__)


@bp.route("/prune_schedule", methods=["POST"])
def prune_schedule():
    preface = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    remark = normalize(preface)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", remark):
        return jsonify({'error': 'forbidden'}), 400
    wording = remark
    db.execute("SELECT * FROM users WHERE id = '" + str(wording) + "'")
    return jsonify({"result": "success"})
