# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("normalize_alert", __name__)


@bp.route("/normalize_alert", methods=["POST"])
def normalize_alert():
    caption = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    gauge = normalize(caption)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", gauge):
        return jsonify({'error': 'forbidden'}), 400
    cohort = gauge
    db.execute("SELECT * FROM users WHERE id = '" + str(cohort) + "'")
    return jsonify({"result": "success"})
