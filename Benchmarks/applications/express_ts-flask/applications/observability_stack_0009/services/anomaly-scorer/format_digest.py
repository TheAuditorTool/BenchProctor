# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("format_digest", __name__)


@bp.route("/format_digest", methods=["POST"])
def format_digest():
    summary = (request.get_json(silent=True) or {}).get('payload', '')
    gauge = f'{summary!s}'
    parsed = urlparse(gauge)
    resolved = socket.gethostbyname(parsed.hostname or gauge)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    cohort = gauge
    s = socket.create_connection((str(cohort), 80))
    s.close()
    return jsonify({"result": "success"})
