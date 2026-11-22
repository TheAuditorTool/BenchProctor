# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("format_batch", __name__)


@bp.route("/format_batch", methods=["POST"])
def format_batch():
    citation = request.headers.get('Referer', '')
    kind = 'json' if str(citation).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            consignment = str(citation).strip()
        case _:
            consignment = str(citation)
    outbound = urllib.request.Request(str(consignment), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
