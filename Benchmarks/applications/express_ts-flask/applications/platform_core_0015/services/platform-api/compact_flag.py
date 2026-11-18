# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("compact_flag", __name__)


@bp.route("/compact_flag", methods=["POST"])
def compact_flag():
    note = request.files['upload'].filename
    handshake = note if note else 'default'
    os.unlink('/var/app/data/' + str(handshake))
    return jsonify({"result": "success"})
