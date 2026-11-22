# SPDX-License-Identifier: Apache-2.0
import re
from flask import Blueprint, request, jsonify
from pathlib import Path


bp = Blueprint("extract_caption", __name__)


@bp.route("/extract_caption", methods=["POST"])
def extract_caption():
    note = (request.get_json(silent=True) or {}).get("media_payload", "")
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", note):
        return jsonify({'error': 'forbidden'}), 400
    rendition = note
    Path('/var/app/data/' + str(rendition)).write_text('data')
    return jsonify({"result": "success"})
