# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("normalize_receipt", __name__)


@bp.route("/normalize_receipt", methods=["POST"])
def normalize_receipt():
    wording = request.headers.get('User-Agent', '')
    parsed = urlparse(wording)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", wording) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    voucher = wording
    requests.get(str(voucher))
    return jsonify({"result": "success"})
