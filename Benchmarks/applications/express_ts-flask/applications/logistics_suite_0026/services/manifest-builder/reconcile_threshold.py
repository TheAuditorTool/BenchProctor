# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("reconcile_threshold", __name__)


@bp.route("/reconcile_threshold", methods=["POST"])
def reconcile_threshold():
    citation = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    parcel = normalize(citation)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", parcel):
        return jsonify({'error': 'forbidden'}), 400
    consignment = parcel
    db.execute("SELECT * FROM users WHERE id = '" + str(consignment) + "'")
    return jsonify({"result": "success"})
