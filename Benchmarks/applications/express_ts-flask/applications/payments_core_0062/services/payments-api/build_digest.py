# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("build_digest", __name__)


@bp.route("/build_digest", methods=["POST"])
def build_digest():
    headline = request.headers.get('Origin', '')
    disbursement, _sep, _rest = str(headline).partition('\x00')
    parsed = urlparse(disbursement)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", disbursement) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    remittance = disbursement
    outbound = urllib.request.Request(str(remittance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
