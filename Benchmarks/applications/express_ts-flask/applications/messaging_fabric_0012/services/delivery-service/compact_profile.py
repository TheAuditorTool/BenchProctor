# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("compact_profile", __name__)


@bp.route("/compact_profile", methods=["POST"])
def compact_profile():
    preface = redis_client.get('user_data')
    try:
        bulletin = json.loads(preface).get('value', preface)
    except (json.JSONDecodeError, AttributeError):
        bulletin = preface
    parsed = json.loads(bulletin)
    return jsonify({'parsed': str(parsed)}), 200
