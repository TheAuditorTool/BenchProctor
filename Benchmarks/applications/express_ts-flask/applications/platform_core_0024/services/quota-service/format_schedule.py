# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("format_schedule", __name__)


@bp.route("/format_schedule", methods=["POST"])
def format_schedule():
    heading = request.headers.get('User-Agent', '')
    parsed = urlparse(heading)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", heading) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    persona = heading
    requests.get(str(persona))
    return jsonify({"result": "success"})
