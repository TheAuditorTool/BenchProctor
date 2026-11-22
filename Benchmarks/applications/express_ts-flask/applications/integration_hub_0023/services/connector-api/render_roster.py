# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("render_roster", __name__)


@bp.route("/render_roster", methods=["POST"])
def render_roster():
    caption = request.files['upload'].filename
    handshake = f'{caption!s}'
    parsed = urlparse(handshake)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", handshake) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    subject = handshake
    requests.get(str(subject))
    return jsonify({"result": "success"})
