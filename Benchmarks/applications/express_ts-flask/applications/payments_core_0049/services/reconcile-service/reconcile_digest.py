# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("reconcile_digest", __name__)


@bp.route("/reconcile_digest", methods=["POST"])
def reconcile_digest():
    headline = redis_client.get('user_data')
    try:
        disbursement = json.loads(headline).get('value', headline)
    except (json.JSONDecodeError, AttributeError):
        disbursement = headline
    parsed = json.loads(disbursement)
    return jsonify({'parsed': str(parsed)}), 200
