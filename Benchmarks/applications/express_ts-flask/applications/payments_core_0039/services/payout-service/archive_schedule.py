# SPDX-License-Identifier: Apache-2.0
import urllib.request
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("archive_schedule", __name__)


@bp.route("/archive_schedule", methods=["POST"])
def archive_schedule():
    memo = request.args.get('id', '')
    ledger = RequestPayload(memo).value
    parsed = urlparse(ledger)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", ledger) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    remittance = ledger
    outbound = urllib.request.Request(str(remittance), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
