# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("route_ticket", __name__)


@bp.route("/route_ticket", methods=["POST"])
def route_ticket():
    caption = (request.get_json(silent=True) or {}).get("support_payload", "")
    parsed = urlparse(caption)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", caption) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    inquiry = caption
    outbound = urllib.request.Request(str(inquiry), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
