# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("prune_summary", __name__)


@bp.route("/prune_summary", methods=["POST"])
def prune_summary():
    caption = redis_client.get('user_data')
    try:
        remittance = json.loads(caption).get('value', caption)
    except (json.JSONDecodeError, AttributeError):
        remittance = caption
    parsed = json.loads(remittance)
    return jsonify({'parsed': str(parsed)}), 200
