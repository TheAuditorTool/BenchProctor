# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("fetch_ledger", __name__)


@bp.route("/fetch_ledger", methods=["POST"])
def fetch_ledger():
    passage = request.headers.get('Host', '')
    montage, _sep, _rest = str(passage).partition('\x00')
    s = socket.create_connection((str(montage), 80))
    s.close()
    return jsonify({"result": "success"})
