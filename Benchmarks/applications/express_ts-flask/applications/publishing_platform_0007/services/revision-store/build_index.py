# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("build_index", __name__)


@bp.route("/build_index", methods=["POST"])
def build_index():
    remark = request.headers.get('Referer', '')
    kind = 'json' if str(remark).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            byline = str(remark).strip()
        case _:
            byline = str(remark)
    outbound = urllib.request.Request(str(byline), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
