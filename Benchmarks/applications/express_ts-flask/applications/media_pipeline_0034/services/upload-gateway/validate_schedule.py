# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("validate_schedule", __name__)


@bp.route("/validate_schedule", methods=["POST"])
def validate_schedule():
    synopsis = request.headers.get('X-Forwarded-For', '')
    rendition = synopsis if synopsis else 'default'
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", rendition):
        return jsonify({'error': 'forbidden'}), 400
    montage = rendition
    Path('/var/app/data/' + str(montage)).write_text('data')
    return jsonify({"result": "success"})
