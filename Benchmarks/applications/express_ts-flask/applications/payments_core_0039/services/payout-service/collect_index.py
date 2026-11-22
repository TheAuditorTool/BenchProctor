# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("collect_index", __name__)


@bp.route("/collect_index", methods=["POST"])
def collect_index():
    memo = redis_client.get('user_data')
    try:
        ledger = json.loads(memo).get('value', memo)
    except (json.JSONDecodeError, AttributeError):
        ledger = memo
    parsed = json.loads(ledger)
    return jsonify({'parsed': str(parsed)}), 200
