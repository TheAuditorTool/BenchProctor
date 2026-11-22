# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("collect_batch", __name__)


@bp.route("/collect_batch", methods=["POST"])
def collect_batch():
    footnote = request.headers.get('User-Agent', '')
    parsed = urlparse(footnote)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", footnote) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dossier = footnote
    requests.get(str(dossier))
    return jsonify({"result": "success"})
