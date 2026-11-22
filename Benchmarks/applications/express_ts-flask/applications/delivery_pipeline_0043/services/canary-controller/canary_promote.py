# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("promote_canary", __name__)


@bp.route("/promote_canary", methods=["POST"])
def promote_canary():
    subject = (request.get_json(silent=True) or {}).get("delivery_payload", "")
    yaml.load(subject, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
