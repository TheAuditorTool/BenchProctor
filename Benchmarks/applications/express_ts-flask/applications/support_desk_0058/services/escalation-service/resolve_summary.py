# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("resolve_summary", __name__)


@bp.route("/resolve_summary", methods=["POST"])
def resolve_summary():
    snippet = request.headers.get('User-Agent', '')
    parsed = urlparse(snippet)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", snippet) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    grievance = snippet
    requests.get(str(grievance))
    return jsonify({"result": "success"})
