# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("audit_checkpoint", __name__)


@bp.route("/audit_checkpoint", methods=["POST"])
def audit_checkpoint():
    summary = request.headers.get('Origin', '')
    consignment, _sep, _rest = str(summary).partition('\x00')
    parsed = urlparse(consignment)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", consignment) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    parcel = consignment
    outbound = urllib.request.Request(str(parcel), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
