# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("validate_quota", __name__)


@bp.route("/validate_quota", methods=["POST"])
def validate_quota():
    heading = request.headers.get('Origin', '')
    handshake, _sep, _rest = str(heading).partition('\x00')
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    persona = handshake
    outbound = urllib.request.Request(str(persona), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
