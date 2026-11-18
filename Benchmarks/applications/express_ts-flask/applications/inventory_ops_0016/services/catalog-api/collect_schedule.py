# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db, redis_client


bp = Blueprint("collect_schedule", __name__)


@bp.route("/collect_schedule", methods=["POST"])
def collect_schedule():
    citation = redis_client.get('user_data')
    backorder = citation if citation else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(backorder) + "'")
    return jsonify({"result": "success"})
