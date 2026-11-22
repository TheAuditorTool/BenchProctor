# SPDX-License-Identifier: Apache-2.0
import json
from flask import Blueprint, jsonify
from app_runtime import redis_client


bp = Blueprint("render_caption", __name__)


@bp.route("/render_caption", methods=["POST"])
def render_caption():
    synopsis = redis_client.get('user_data')
    try:
        rendition = json.loads(synopsis).get('value', synopsis)
    except (json.JSONDecodeError, AttributeError):
        rendition = synopsis
    parsed = json.loads(rendition)
    return jsonify({'parsed': str(parsed)}), 200
