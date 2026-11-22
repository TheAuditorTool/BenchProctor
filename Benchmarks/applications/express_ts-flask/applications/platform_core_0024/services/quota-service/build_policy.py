# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket
import urllib.parse


bp = Blueprint("build_policy", __name__)


@bp.route("/build_policy", methods=["POST"])
def build_policy():
    heading = request.files['upload'].filename
    parts = []
    for token in str(heading).split(','):
        parts.append(token.strip())
    handshake = ','.join(parts)
    s = socket.create_connection((urllib.parse.urlparse(str(handshake)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
