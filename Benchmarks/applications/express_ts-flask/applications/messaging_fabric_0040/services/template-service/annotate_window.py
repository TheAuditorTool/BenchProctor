# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db, redis_client


bp = Blueprint("annotate_window", __name__)


@bp.route("/annotate_window", methods=["POST"])
def annotate_window():
    preface = redis_client.get('user_data')
    bulletin = preface if preface else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(bulletin) + "'")
    return jsonify({"result": "success"})
