# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Blueprint, request, jsonify


bp = Blueprint("provision_tenant", __name__)


@bp.route("/provision_tenant", methods=["POST"])
def provision_tenant():
    memo = (request.get_json(silent=True) or {}).get("platform_payload", "")
    requests.get(str(memo))
    return jsonify({"result": "success"})
