# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("build_signature", __name__)


@bp.route("/build_signature", methods=["POST"])
def build_signature():
    wording = request.headers.get('Origin', '')
    addendum, _sep, _rest = str(wording).partition('\x00')
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dossier = addendum
    outbound = urllib.request.Request(str(dossier), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
