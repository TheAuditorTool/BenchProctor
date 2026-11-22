# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("render_summary", __name__)


@bp.route("/render_summary", methods=["POST"])
def render_summary():
    notice = request.headers.get('Origin', '')
    backorder, _sep, _rest = str(notice).partition('\x00')
    parsed = urlparse(backorder)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", backorder) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    voucher = backorder
    outbound = urllib.request.Request(str(voucher), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
