# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("format_manifest", __name__)


@bp.route("/format_manifest", methods=["POST"])
def format_manifest():
    memo = request.headers.get('Host', '')
    voucher, _sep, _rest = str(memo).partition('\x00')
    s = socket.create_connection((str(voucher), 80))
    s.close()
    return jsonify({"result": "success"})
