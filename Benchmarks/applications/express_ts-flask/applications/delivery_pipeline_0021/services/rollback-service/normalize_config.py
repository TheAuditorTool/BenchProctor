# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("normalize_config", __name__)


@bp.route("/normalize_config", methods=["POST"])
def normalize_config():
    summary = request.headers.get('Origin', '')
    phrase, _sep, _rest = str(summary).partition('\x00')
    parsed = urlparse(phrase)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", phrase) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    subtitle = phrase
    outbound = urllib.request.Request(str(subtitle), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
