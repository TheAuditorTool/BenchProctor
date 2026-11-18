# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("export_header", __name__)


@bp.route("/export_header", methods=["POST"])
def export_header():
    note = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(note)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", gauge):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    db.execute("SELECT * FROM users WHERE id = '" + str(cohort) + "'")
    return jsonify({"result": "success"})
