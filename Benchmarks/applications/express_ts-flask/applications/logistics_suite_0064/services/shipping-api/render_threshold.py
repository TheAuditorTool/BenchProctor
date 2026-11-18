# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("render_threshold", __name__)


@bp.route("/render_threshold", methods=["POST"])
def render_threshold():
    transcript = request.headers.get('Host', '')
    try:
        parcel = json.loads(transcript).get('value', transcript)
    except (json.JSONDecodeError, AttributeError):
        parcel = transcript
    yaml.load(parcel, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
