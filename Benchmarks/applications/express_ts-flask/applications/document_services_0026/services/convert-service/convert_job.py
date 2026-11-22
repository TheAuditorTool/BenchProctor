# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("run_conversion", __name__)


@bp.route("/run_conversion", methods=["POST"])
def run_conversion():
    notice = (request.get_json(silent=True) or {}).get("documents_payload", "")
    outbound = urllib.request.Request(str(notice), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
