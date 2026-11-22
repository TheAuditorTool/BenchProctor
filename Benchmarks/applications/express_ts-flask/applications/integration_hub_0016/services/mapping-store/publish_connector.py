# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("publish_connector", __name__)


@bp.route("/publish_connector", methods=["POST"])
def publish_connector():
    wording = request.headers.get('X-Forwarded-For', '')
    handshake = wording if wording else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    subject = handshake
    Path('/var/app/data/' + str(subject)).write_text('data')
    return jsonify({"result": "success"})
