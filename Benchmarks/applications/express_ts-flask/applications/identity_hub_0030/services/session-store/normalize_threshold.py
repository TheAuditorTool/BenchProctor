# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("normalize_threshold", __name__)


@bp.route("/normalize_threshold", methods=["POST"])
def normalize_threshold():
    tagline = request.headers.get('X-Forwarded-For', '')
    persona = tagline if tagline else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", persona):
        return jsonify({'error': 'forbidden'}), 400
    note = persona
    Path('/var/app/data/' + str(note)).write_text('data')
    return jsonify({"result": "success"})
