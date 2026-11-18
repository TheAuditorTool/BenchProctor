# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

bp = Blueprint("merge_summary", __name__)


@bp.route("/merge_summary", methods=["POST"])
def merge_summary():
    caption = (request.get_json(silent=True) or {}).get('payload', '')
    gauge = RequestPayload(caption).value
    parsed = urlparse(gauge)
    resolved = socket.gethostbyname(parsed.hostname or gauge)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    cohort = gauge
    requests.get(str(cohort))
    return jsonify({"result": "success"})
