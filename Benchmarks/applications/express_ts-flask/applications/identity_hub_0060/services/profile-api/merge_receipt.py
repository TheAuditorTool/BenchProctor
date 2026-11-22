# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("merge_receipt", __name__)


@bp.route("/merge_receipt", methods=["POST"])
def merge_receipt():
    paragraph = request.files['upload'].filename
    persona = f'{paragraph!s}'
    parsed = urlparse(persona)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", persona) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    blurb = persona
    requests.get(str(blurb))
    return jsonify({"result": "success"})
