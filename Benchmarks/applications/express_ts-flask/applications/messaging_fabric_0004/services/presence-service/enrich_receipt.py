# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("enrich_receipt", __name__)


@bp.route("/enrich_receipt", methods=["POST"])
def enrich_receipt():
    paragraph = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    bulletin = normalize(paragraph)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", bulletin):
        return jsonify({'error': 'forbidden'}), 400
    synopsis = bulletin
    db.execute("SELECT * FROM users WHERE id = '" + str(synopsis) + "'")
    return jsonify({"result": "success"})
