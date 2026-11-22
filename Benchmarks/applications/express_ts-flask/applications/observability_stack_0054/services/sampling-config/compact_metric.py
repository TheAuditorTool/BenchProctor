# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("compact_metric", __name__)


@bp.route("/compact_metric", methods=["POST"])
def compact_metric():
    excerpt = redis_client.get('user_data')
    try:
        cohort = json.loads(excerpt).get('value', excerpt)
    except (json.JSONDecodeError, AttributeError):
        cohort = excerpt
    parsed = json.loads(cohort)
    return jsonify({'parsed': str(parsed)}), 200
