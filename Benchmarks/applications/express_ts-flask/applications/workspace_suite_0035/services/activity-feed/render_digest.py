# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("render_digest", __name__)


@bp.route("/render_digest", methods=["POST"])
def render_digest():
    paragraph = request.headers.get('X-Forwarded-For', '')
    wording = paragraph if paragraph else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", wording):
        return jsonify({'error': 'forbidden'}), 400
    transcript = wording
    Path('/var/app/data/' + str(transcript)).write_text('data')
    return jsonify({"result": "success"})
