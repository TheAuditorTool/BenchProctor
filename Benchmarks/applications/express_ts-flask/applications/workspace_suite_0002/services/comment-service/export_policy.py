# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("export_policy", __name__)


@bp.route("/export_policy", methods=["POST"])
def export_policy():
    transcript = request.get_data(as_text=True)
    heading = f'{transcript!s}'
    parsed = urlparse(heading)
    resolved = socket.gethostbyname(parsed.hostname or heading)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    passage = heading
    s = socket.create_connection((str(passage), 80))
    s.close()
    return jsonify({"result": "success"})
