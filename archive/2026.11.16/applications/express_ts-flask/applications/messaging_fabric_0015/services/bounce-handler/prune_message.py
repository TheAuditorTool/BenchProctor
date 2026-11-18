# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("prune_message", __name__)


@bp.route("/prune_message", methods=["POST"])
def prune_message():
    heading = request.headers.get('X-Forwarded-For', '')
    bulletin = f'{heading!s}'
    parsed = urlparse(bulletin)
    resolved = socket.gethostbyname(parsed.hostname or bulletin)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    excerpt = bulletin
    requests.get(str(excerpt))
    return jsonify({"result": "success"})
