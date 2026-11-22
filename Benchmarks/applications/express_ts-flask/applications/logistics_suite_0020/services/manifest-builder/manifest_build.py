# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("build_manifest", __name__)


@bp.route("/build_manifest", methods=["POST"])
def build_manifest():
    footnote = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    outbound = urllib.request.Request(str(footnote), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
