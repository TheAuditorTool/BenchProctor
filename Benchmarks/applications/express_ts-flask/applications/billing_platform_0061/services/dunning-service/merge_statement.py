# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import re
from app_runtime import db


bp = Blueprint("merge_statement", __name__)


@bp.route("/merge_statement", methods=["POST"])
def merge_statement():
    footnote = db.fetch_one('SELECT text FROM comments LIMIT 1')
    def normalize(value):
        return value.strip()
    remittance = normalize(footnote)
    parsed = urlparse(remittance)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remittance) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    arrears = remittance
    outbound = urllib.request.Request(str(arrears), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
