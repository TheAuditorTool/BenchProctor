# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("validate_fulfillment", __name__)


@bp.route("/validate_fulfillment", methods=["POST"])
def validate_fulfillment():
    headline = request.headers.get('User-Agent', '')
    parsed = urlparse(headline)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", headline) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    voucher = headline
    requests.get(str(voucher))
    return jsonify({"result": "success"})
