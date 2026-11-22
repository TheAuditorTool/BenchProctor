# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("format_revision", __name__)


@bp.route("/format_revision", methods=["POST"])
def format_revision():
    remark = request.headers.get('User-Agent', '')
    parsed = urlparse(remark)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remark) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    addendum = remark
    requests.get(str(addendum))
    return jsonify({"result": "success"})
