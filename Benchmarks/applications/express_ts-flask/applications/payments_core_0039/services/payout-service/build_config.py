# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("build_config", __name__)


@bp.route("/build_config", methods=["POST"])
def build_config():
    memo = request.headers.get('Origin', '')
    ledger, _sep, _rest = str(memo).partition('\x00')
    parsed = urlparse(ledger)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", ledger) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    remittance = ledger
    outbound = urllib.request.Request(str(remittance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
