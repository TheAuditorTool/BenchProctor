# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("validate_header", __name__)


@bp.route("/validate_header", methods=["POST"])
def validate_header():
    synopsis = request.headers.get('Host', '')
    try:
        arrears = json.loads(synopsis).get('value', synopsis)
    except (json.JSONDecodeError, AttributeError):
        arrears = synopsis
    yaml.load(arrears, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
