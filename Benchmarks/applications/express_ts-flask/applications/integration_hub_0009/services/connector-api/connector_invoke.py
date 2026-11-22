# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("invoke_connector", __name__)


@bp.route("/invoke_connector", methods=["POST"])
def invoke_connector():
    quotation = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    parsed = urlparse(quotation)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", quotation) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    remark = quotation
    outbound = urllib.request.Request(str(remark), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
