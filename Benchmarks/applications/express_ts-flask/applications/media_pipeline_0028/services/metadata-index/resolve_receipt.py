# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("resolve_receipt", __name__)


@bp.route("/resolve_receipt", methods=["POST"])
def resolve_receipt():
    citation = request.files['upload'].filename
    rendition = f'{citation!s}'
    parsed = urlparse(rendition)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", rendition) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    montage = rendition
    requests.get(str(montage))
    return jsonify({"result": "success"})
