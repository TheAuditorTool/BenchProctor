# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("summarize_syndication", __name__)


@bp.route("/summarize_syndication", methods=["POST"])
def summarize_syndication():
    heading = request.headers.get('User-Agent', '')
    parsed = urlparse(heading)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", heading) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    byline = heading
    requests.get(str(byline))
    return jsonify({"result": "success"})
