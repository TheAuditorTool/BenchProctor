# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("queue_retry", __name__)


@bp.route("/queue_retry", methods=["POST"])
def queue_retry():
    citation = (request.get_json(silent=True) or {}).get("integrations_payload", "")
    parsed = urlparse(citation)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", citation) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    paragraph = citation
    outbound = urllib.request.Request(str(paragraph), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
