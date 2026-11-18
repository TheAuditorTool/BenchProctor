# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("summarize_release", __name__)


@bp.route("/summarize_release", methods=["POST"])
def summarize_release():
    wording = (request.get_json(silent=True) or {}).get('payload', '')
    remark = f'{wording!s}'
    parsed = urlparse(remark)
    resolved = socket.gethostbyname(parsed.hostname or remark)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    phrase = remark
    s = socket.create_connection((str(phrase), 80))
    s.close()
    return jsonify({"result": "success"})
