# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("query_dashboard", __name__)


@bp.route("/query_dashboard", methods=["POST"])
def query_dashboard():
    quotation = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    os.unlink('/var/app/data/' + str(quotation))
    return jsonify({"result": "success"})
