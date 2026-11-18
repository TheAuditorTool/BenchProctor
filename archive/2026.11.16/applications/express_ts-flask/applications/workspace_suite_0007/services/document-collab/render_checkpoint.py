# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("render_checkpoint", __name__)


@bp.route("/render_checkpoint", methods=["POST"])
def render_checkpoint():
    summary = request.headers.get('X-Forwarded-For', '')
    subtitle = f'{summary!s}'
    parsed = urlparse(subtitle)
    resolved = socket.gethostbyname(parsed.hostname or subtitle)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    notice = subtitle
    requests.get(str(notice))
    return jsonify({"result": "success"})
