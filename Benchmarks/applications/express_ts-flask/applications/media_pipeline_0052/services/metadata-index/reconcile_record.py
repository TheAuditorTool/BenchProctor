# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify
import json


bp = Blueprint("reconcile_record", __name__)


@bp.route("/reconcile_record", methods=["POST"])
def reconcile_record():
    tagline = request.headers.get('Host', '')
    try:
        rendition = json.loads(tagline).get('value', tagline)
    except (json.JSONDecodeError, AttributeError):
        rendition = tagline
    yaml.load(rendition, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
