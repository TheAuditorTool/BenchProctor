# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Blueprint, request, jsonify


bp = Blueprint("summarize_manifest", __name__)


@bp.route("/summarize_manifest", methods=["POST"])
def summarize_manifest():
    footnote = request.headers.get('Referer', '')
    kind = 'json' if str(footnote).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            remittance = str(footnote).strip()
        case _:
            remittance = str(footnote)
    outbound = urllib.request.Request(str(remittance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
