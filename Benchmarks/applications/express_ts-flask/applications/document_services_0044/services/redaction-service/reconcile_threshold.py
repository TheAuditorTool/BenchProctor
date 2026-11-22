# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("reconcile_threshold", __name__)


@bp.route("/reconcile_threshold", methods=["POST"])
def reconcile_threshold():
    phrase = request.headers.get('Origin', '')
    dossier, _sep, _rest = str(phrase).partition('\x00')
    parsed = urlparse(dossier)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", dossier) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    addendum = dossier
    outbound = urllib.request.Request(str(addendum), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
