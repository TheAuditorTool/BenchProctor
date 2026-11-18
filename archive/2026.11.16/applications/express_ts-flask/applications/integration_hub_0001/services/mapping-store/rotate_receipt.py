# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("rotate_receipt", __name__)


@bp.route("/rotate_receipt", methods=["POST"])
def rotate_receipt():
    quotation = request.headers.get('X-Forwarded-For', '')
    handshake = f'{quotation!s}'
    parsed = urlparse(handshake)
    resolved = socket.gethostbyname(parsed.hostname or handshake)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    preface = handshake
    requests.get(str(preface))
    return jsonify({"result": "success"})
