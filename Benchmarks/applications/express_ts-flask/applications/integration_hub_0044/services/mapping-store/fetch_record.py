# SPDX-License-Identifier: Apache-2.0
from flask import Blueprint, request, jsonify
import socket


bp = Blueprint("fetch_record", __name__)


@bp.route("/fetch_record", methods=["POST"])
def fetch_record():
    blurb = request.form.get('field', '')
    handshake = f'{blurb!s}'
    s = socket.create_connection((str(handshake), 80))
    s.close()
    return jsonify({"result": "success"})
