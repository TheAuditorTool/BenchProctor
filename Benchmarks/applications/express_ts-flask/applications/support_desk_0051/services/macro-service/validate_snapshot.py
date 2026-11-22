# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("validate_snapshot", __name__)


@bp.route("/validate_snapshot", methods=["POST"])
def validate_snapshot():
    preface = redis_client.get('user_data')
    try:
        grievance = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        grievance = preface
    parsed = json.loads(grievance)
    return jsonify({'parsed': str(parsed)}), 200
