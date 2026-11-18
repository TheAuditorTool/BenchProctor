# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("provision_tenant", __name__)


@bp.route("/provision_tenant", methods=["POST"])
def provision_tenant():
    quotation = (request.get_json(silent=True) or {}).get("platform_payload", "")
    s = socket.create_connection((str(quotation), 80))
    s.close()
    return jsonify({"result": "success"})
