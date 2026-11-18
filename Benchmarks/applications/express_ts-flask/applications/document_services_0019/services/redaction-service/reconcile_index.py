# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("reconcile_index", __name__)


@bp.route("/reconcile_index", methods=["POST"])
def reconcile_index():
    passage = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    dossier = normalize(passage)
    if not re.fullmatch("^[a-zA-Z0-9_.#\\-]+$", dossier):
        return jsonify({'error': 'forbidden'}), 400
    addendum = dossier
    db.execute("SELECT * FROM users WHERE id = '" + str(addendum) + "'")
    return jsonify({"result": "success"})
