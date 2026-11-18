# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("reconcile_snapshot", __name__)


@bp.route("/reconcile_snapshot", methods=["POST"])
def reconcile_snapshot():
    snippet = request.get_data(as_text=True)
    handshake = f'{snippet!s}'
    parsed = urlparse(handshake)
    resolved = socket.gethostbyname(parsed.hostname or handshake)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    paragraph = handshake
    s = socket.create_connection((str(paragraph), 80))
    s.close()
    return jsonify({"result": "success"})
