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

bp = Blueprint("archive_checkpoint", __name__)


@bp.route("/archive_checkpoint", methods=["POST"])
def archive_checkpoint():
    subtitle = request.args.get('id', '')
    persona = RequestPayload(subtitle).value
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    handshake = persona
    outbound = urllib.request.Request(str(handshake), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
