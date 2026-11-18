# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("lookup_sku", __name__)


@bp.route("/lookup_sku", methods=["POST"])
def lookup_sku():
    notice = (request.get_json(silent=True) or {}).get("inventory_payload", "")
    parsed = urlparse(notice)
    resolved = socket.gethostbyname(parsed.hostname or notice)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    restock = notice
    s = socket.create_connection((str(restock), 80))
    s.close()
    return jsonify({"result": "success"})
