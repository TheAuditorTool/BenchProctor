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

bp = Blueprint("export_index", __name__)


@bp.route("/export_index", methods=["POST"])
def export_index():
    transcript = (request.get_json(silent=True) or {}).get('payload', '')
    parcel = RequestPayload(transcript).value
    parsed = urlparse(parcel)
    resolved = socket.gethostbyname(parsed.hostname or parcel)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    consignment = parcel
    requests.get(str(consignment))
    return jsonify({"result": "success"})
