# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("merge_ledger", __name__)


@bp.route("/merge_ledger", methods=["POST"])
def merge_ledger():
    caption = request.headers.get('User-Agent', '')
    parsed = urlparse(caption)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", caption) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    snippet = caption
    requests.get(str(snippet))
    return jsonify({"result": "success"})
