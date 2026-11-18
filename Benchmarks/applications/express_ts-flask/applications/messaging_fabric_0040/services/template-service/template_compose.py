# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("compose_template", __name__)


@bp.route("/compose_template", methods=["POST"])
def compose_template():
    phrase = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    yaml.load(phrase, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
