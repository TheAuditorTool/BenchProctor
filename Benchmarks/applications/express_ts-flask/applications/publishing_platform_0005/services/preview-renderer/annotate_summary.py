# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db, redis_client


bp = Blueprint("annotate_summary", __name__)


@bp.route("/annotate_summary", methods=["POST"])
def annotate_summary():
    footnote = redis_client.get('user_data')
    byline = footnote if footnote else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(byline) + "'")
    return jsonify({"result": "success"})
