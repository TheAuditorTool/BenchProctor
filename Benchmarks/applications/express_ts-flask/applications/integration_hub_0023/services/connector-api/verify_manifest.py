# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("verify_manifest", __name__)


@bp.route("/verify_manifest", methods=["POST"])
def verify_manifest():
    caption = request.headers.get('Origin', '')
    handshake, _sep, _rest = str(caption).partition('\x00')
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    subject = handshake
    outbound = urllib.request.Request(str(subject), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
