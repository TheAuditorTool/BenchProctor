# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("raise_escalation", __name__)


@bp.route("/raise_escalation", methods=["POST"])
def raise_escalation():
    quotation = (request.get_json(silent=True) or {}).get("support_payload", "")
    outbound = urllib.request.Request(str(quotation), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
