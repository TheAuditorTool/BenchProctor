# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("validate_receipt", __name__)


@bp.route("/validate_receipt", methods=["POST"])
def validate_receipt():
    excerpt = request.headers.get('Origin', '')
    restock, _sep, _rest = str(excerpt).partition('\x00')
    parsed = urlparse(restock)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", restock) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    backorder = restock
    outbound = urllib.request.Request(str(backorder), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
