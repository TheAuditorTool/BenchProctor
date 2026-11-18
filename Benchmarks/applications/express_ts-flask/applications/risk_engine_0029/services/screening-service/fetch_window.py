# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("fetch_window", __name__)


@bp.route("/fetch_window", methods=["POST"])
def fetch_window():
    subject = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    grievance = normalize(subject)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", grievance):
        return jsonify({'error': 'forbidden'}), 400
    verdict = grievance
    db.execute("SELECT * FROM users WHERE id = '" + str(verdict) + "'")
    return jsonify({"result": "success"})
