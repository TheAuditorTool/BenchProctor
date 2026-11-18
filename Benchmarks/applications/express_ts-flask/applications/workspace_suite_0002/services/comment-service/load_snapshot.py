# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db, redis_client


bp = Blueprint("load_snapshot", __name__)


@bp.route("/load_snapshot", methods=["POST"])
def load_snapshot():
    transcript = redis_client.get('user_data')
    heading = transcript if transcript else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(heading) + "'")
    return jsonify({"result": "success"})
