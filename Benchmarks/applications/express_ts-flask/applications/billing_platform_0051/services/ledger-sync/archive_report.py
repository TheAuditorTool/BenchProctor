# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("archive_report", __name__)


@bp.route("/archive_report", methods=["POST"])
def archive_report():
    synopsis = (request.get_json(silent=True) or {}).get('payload', '')
    arrears = f'{synopsis!s}'
    parsed = urlparse(arrears)
    resolved = socket.gethostbyname(parsed.hostname or arrears)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    dunning = arrears
    s = socket.create_connection((str(dunning), 80))
    s.close()
    return jsonify({"result": "success"})
