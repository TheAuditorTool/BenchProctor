# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import Blueprint, request, jsonify


bp = Blueprint("queue_retry", __name__)


@bp.route("/queue_retry", methods=["POST"])
def queue_retry():
    remark = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    yaml.load(remark, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
