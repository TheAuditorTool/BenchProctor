# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("index_document", __name__)


@bp.route("/index_document", methods=["POST"])
def index_document():
    note = (request.get_json(silent=True) or {}).get("documents_payload", "")
    outbound = urllib.request.Request(str(note), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
