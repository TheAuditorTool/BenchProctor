# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("merge_profile", __name__)


@bp.route("/merge_profile", methods=["POST"])
def merge_profile():
    subtitle = request.headers.get('X-Forwarded-For', '')
    ledger = f'{subtitle!s}'
    parsed = urlparse(ledger)
    resolved = socket.gethostbyname(parsed.hostname or ledger)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    remittance = ledger
    requests.get(str(remittance))
    return jsonify({"result": "success"})
