# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("collect_threshold", __name__)


@bp.route("/collect_threshold", methods=["POST"])
def collect_threshold():
    heading = request.headers.get('X-Forwarded-For', '')
    handshake = heading if heading else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", handshake):
        return jsonify({'error': 'forbidden'}), 400
    persona = handshake
    Path('/var/app/data/' + str(persona)).write_text('data')
    return jsonify({"result": "success"})
