# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("resolve_bundle", __name__)


@bp.route("/resolve_bundle", methods=["POST"])
def resolve_bundle():
    snippet = (request.get_json(silent=True) or {}).get('payload', '')
    persona = f'{snippet!s}'
    parsed = urlparse(persona)
    resolved = socket.gethostbyname(parsed.hostname or persona)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    synopsis = persona
    s = socket.create_connection((str(synopsis), 80))
    s.close()
    return jsonify({"result": "success"})
