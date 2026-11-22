# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("dispatch_carrier", __name__)


@bp.route("/dispatch_carrier", methods=["POST"])
def dispatch_carrier():
    paragraph = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    outbound = urllib.request.Request(str(paragraph), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
