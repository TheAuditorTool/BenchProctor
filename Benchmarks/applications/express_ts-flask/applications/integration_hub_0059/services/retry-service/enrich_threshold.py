# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db, redis_client


bp = Blueprint("enrich_threshold", __name__)


@bp.route("/enrich_threshold", methods=["POST"])
def enrich_threshold():
    synopsis = redis_client.get('user_data')
    handshake = synopsis if synopsis else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(handshake) + "'")
    return jsonify({"result": "success"})
