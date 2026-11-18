# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
from app_runtime import db


bp = Blueprint("prune_threshold", __name__)


@bp.route("/prune_threshold", methods=["POST"])
def prune_threshold():
    citation = request.files['upload'].filename
    if citation:
        grievance = citation
    else:
        grievance = ''
    db.execute("SELECT * FROM users WHERE id = '" + str(grievance) + "'")
    return jsonify({"result": "success"})
