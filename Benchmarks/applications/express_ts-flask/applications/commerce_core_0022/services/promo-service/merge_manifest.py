# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket
import urllib.parse


bp = Blueprint("merge_manifest", __name__)


@bp.route("/merge_manifest", methods=["POST"])
def merge_manifest():
    subject = request.files['upload'].filename
    parts = []
    for token in str(subject).split(','):
        parts.append(token.strip())
    voucher = ','.join(parts)
    s = socket.create_connection((urllib.parse.urlparse(str(voucher)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
