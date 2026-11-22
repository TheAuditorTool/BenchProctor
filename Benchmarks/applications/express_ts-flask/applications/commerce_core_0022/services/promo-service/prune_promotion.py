# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("prune_promotion", __name__)


@bp.route("/prune_promotion", methods=["POST"])
def prune_promotion():
    subject = redis_client.get('user_data')
    try:
        voucher = json.loads(subject).get('value', subject)
    except (json.JSONDecodeError, AttributeError):
        voucher = subject
    parsed = json.loads(voucher)
    return jsonify({'parsed': str(parsed)}), 200
