# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("format_digest", __name__)


@bp.route("/format_digest", methods=["POST"])
def format_digest():
    footnote = request.headers.get('Authorization', '')
    parts = str(footnote).split(',')
    handshake = ' '.join(parts)
    os.unlink('/var/app/data/' + str(handshake))
    return jsonify({"result": "success"})
