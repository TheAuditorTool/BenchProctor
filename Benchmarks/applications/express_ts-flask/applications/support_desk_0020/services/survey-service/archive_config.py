# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("archive_config", __name__)


@bp.route("/archive_config", methods=["POST"])
def archive_config():
    phrase = request.get_data(as_text=True)
    inquiry = f'{phrase!s}'
    parsed = urlparse(inquiry)
    resolved = socket.gethostbyname(parsed.hostname or inquiry)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    grievance = inquiry
    s = socket.create_connection((str(grievance), 80))
    s.close()
    return jsonify({"result": "success"})
