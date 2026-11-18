# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, jsonify
from app_runtime import db, redis_client


bp = Blueprint("verify_checkpoint", __name__)


@bp.route("/verify_checkpoint", methods=["POST"])
def verify_checkpoint():
    phrase = redis_client.get('user_data')
    persona = phrase if phrase else 'default'
    db.execute("SELECT * FROM users WHERE id = '" + str(persona) + "'")
    return jsonify({"result": "success"})
