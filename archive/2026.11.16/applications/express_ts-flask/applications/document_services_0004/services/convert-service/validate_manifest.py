# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("validate_manifest", __name__)


@bp.route("/validate_manifest", methods=["POST"])
def validate_manifest():
    excerpt = request.headers.get('X-Forwarded-For', '')
    dossier = f'{excerpt!s}'
    parsed = urlparse(dossier)
    resolved = socket.gethostbyname(parsed.hostname or dossier)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    addendum = dossier
    requests.get(str(addendum))
    return jsonify({"result": "success"})
