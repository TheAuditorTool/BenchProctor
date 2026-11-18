# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
import socket
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("publish_bundle", __name__)


@bp.route("/publish_bundle", methods=["POST"])
def publish_bundle():
    phrase = request.headers.get('X-Forwarded-For', '')
    backorder = f'{phrase!s}'
    parsed = urlparse(backorder)
    resolved = socket.gethostbyname(parsed.hostname or backorder)
    if re.match("^(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.|::1$|::[fF]{4}:(0\\.|10\\.|127\\.|169\\.254\\.|192\\.168\\.|172\\.(1[6-9]|2[0-9]|3[01])\\.)|[fF][cCdD]|[fF][eE]80:)", resolved):
        return jsonify({'error': 'private range blocked'}), 403
    restock = backorder
    requests.get(str(restock))
    return jsonify({"result": "success"})
