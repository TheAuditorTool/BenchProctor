# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("update_presence", __name__)


@bp.route("/update_presence", methods=["POST"])
def update_presence():
    transcript = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    yaml.load(transcript, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
