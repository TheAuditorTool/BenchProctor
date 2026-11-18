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

bp = Blueprint("merge_ledger", __name__)


@bp.route("/merge_ledger", methods=["POST"])
def merge_ledger():
    heading = (request.get_json(silent=True) or {}).get('payload', '')
    consignment = RequestPayload(heading).value
    parsed = urlparse(consignment)
    resolved = socket.gethostbyname(parsed.hostname or consignment)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    parcel = consignment
    requests.get(str(parcel))
    return jsonify({"result": "success"})
