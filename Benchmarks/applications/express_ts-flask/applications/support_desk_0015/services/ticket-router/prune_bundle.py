# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("prune_bundle", __name__)


@bp.route("/prune_bundle", methods=["POST"])
def prune_bundle():
    phrase = request.headers.get('User-Agent', '')
    parsed = urlparse(phrase)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", phrase) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    inquiry = phrase
    requests.get(str(inquiry))
    return jsonify({"result": "success"})
