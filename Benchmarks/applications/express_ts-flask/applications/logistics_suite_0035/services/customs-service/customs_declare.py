# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("declare_customs", __name__)


@bp.route("/declare_customs", methods=["POST"])
def declare_customs():
    summary = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    parsed = urlparse(summary)
    resolved = socket.gethostbyname(parsed.hostname or summary)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    consignment = summary
    requests.get(str(consignment))
    return jsonify({"result": "success"})
