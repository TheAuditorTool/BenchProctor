# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("normalize_flag", __name__)


@bp.route("/normalize_flag", methods=["POST"])
def normalize_flag():
    subtitle = request.headers.get('X-Forwarded-For', '')
    persona = subtitle if subtitle else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    handshake = persona
    Path('/var/app/data/' + str(handshake)).write_text('data')
    return jsonify({"result": "success"})
