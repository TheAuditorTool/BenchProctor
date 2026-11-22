# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("update_profile", __name__)


@bp.route("/update_profile", methods=["POST"])
def update_profile():
    phrase = (request.get_json(silent=True) or {}).get("identity_payload", "")
    outbound = urllib.request.Request(str(phrase), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
