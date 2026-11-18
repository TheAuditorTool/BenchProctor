# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("summarize_digest", __name__)


@bp.route("/summarize_digest", methods=["POST"])
def summarize_digest():
    citation = request.headers.get('X-Forwarded-For', '')
    grievance = f'{citation!s}'
    parsed = urlparse(grievance)
    resolved = socket.gethostbyname(parsed.hostname or grievance)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    inquiry = grievance
    requests.get(str(inquiry))
    return jsonify({"result": "success"})
