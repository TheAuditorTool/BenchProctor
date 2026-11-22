# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("load_bundle", __name__)


@bp.route("/load_bundle", methods=["POST"])
def load_bundle():
    notice = redis_client.get('user_data')
    try:
        backorder = json.loads(notice).get('value', notice)
    except (json.JSONDecodeError, AttributeError):
        backorder = notice
    parsed = json.loads(backorder)
    return jsonify({'parsed': str(parsed)}), 200
