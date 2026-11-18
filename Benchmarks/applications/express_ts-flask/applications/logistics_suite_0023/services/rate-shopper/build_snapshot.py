# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("build_snapshot", __name__)


@bp.route("/build_snapshot", methods=["POST"])
def build_snapshot():
    caption = (request.get_json(silent=True) or {}).get('payload', '')
    parcel = f'{caption!s}'
    parsed = urlparse(parcel)
    resolved = socket.gethostbyname(parsed.hostname or parcel)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    consignment = parcel
    s = socket.create_connection((str(consignment), 80))
    s.close()
    return jsonify({"result": "success"})
