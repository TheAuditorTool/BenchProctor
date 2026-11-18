# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("format_receipt", __name__)


@bp.route("/format_receipt", methods=["POST"])
def format_receipt():
    subject = request.headers.get('X-Forwarded-For', '')
    parcel = f'{subject!s}'
    parsed = urlparse(parcel)
    resolved = socket.gethostbyname(parsed.hostname or parcel)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    consignment = parcel
    requests.get(str(consignment))
    return jsonify({"result": "success"})
