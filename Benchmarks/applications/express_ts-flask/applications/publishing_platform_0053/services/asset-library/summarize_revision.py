# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("summarize_revision", __name__)


@bp.route("/summarize_revision", methods=["POST"])
def summarize_revision():
    note = request.headers.get('Origin', '')
    byline, _sep, _rest = str(note).partition('\x00')
    parsed = urlparse(byline)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", byline) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    addendum = byline
    outbound = urllib.request.Request(str(addendum), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
