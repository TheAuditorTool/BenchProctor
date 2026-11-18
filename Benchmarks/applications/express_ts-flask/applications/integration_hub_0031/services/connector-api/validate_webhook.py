# SPDX-License-Identifier: Apache-2.0
import os
from flask import Blueprint, request, jsonify


bp = Blueprint("validate_webhook", __name__)


@bp.route("/validate_webhook", methods=["POST"])
def validate_webhook():
    snippet = request.args.get('id', '')
    parts = str(snippet).split(',')
    handshake = ' '.join(parts)
    os.unlink('/var/app/data/' + str(handshake))
    return jsonify({"result": "success"})
