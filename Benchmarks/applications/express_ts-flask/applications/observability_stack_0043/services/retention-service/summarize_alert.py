# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("summarize_alert", __name__)


@bp.route("/summarize_alert", methods=["POST"])
def summarize_alert():
    note = request.headers.get('Host', '')
    try:
        gauge = json.loads(note).get('value', note)
    except (json.JSONDecodeError, AttributeError):
        gauge = note
    yaml.load(gauge, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
