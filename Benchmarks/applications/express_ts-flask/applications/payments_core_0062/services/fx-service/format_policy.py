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

bp = Blueprint("format_policy", __name__)


@bp.route("/format_policy", methods=["POST"])
def format_policy():
    headline = (request.get_json(silent=True) or {}).get('payload', '')
    disbursement = RequestPayload(headline).value
    parsed = urlparse(disbursement)
    resolved = socket.gethostbyname(parsed.hostname or disbursement)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    remittance = disbursement
    requests.get(str(remittance))
    return jsonify({"result": "success"})
