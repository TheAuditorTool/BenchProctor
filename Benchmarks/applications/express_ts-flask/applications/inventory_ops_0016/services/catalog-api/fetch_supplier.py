# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("fetch_supplier", __name__)


@bp.route("/fetch_supplier", methods=["POST"])
def fetch_supplier():
    citation = (request.get_json(silent=True) or {}).get('payload', '')
    backorder = f'{citation!s}'
    parsed = urlparse(backorder)
    resolved = socket.gethostbyname(parsed.hostname or backorder)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    restock = backorder
    s = socket.create_connection((str(restock), 80))
    s.close()
    return jsonify({"result": "success"})
