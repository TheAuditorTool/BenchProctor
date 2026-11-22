# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("fetch_ledger", __name__)


@bp.route("/fetch_ledger", methods=["POST"])
def fetch_ledger():
    memo = request.headers.get('User-Agent', '')
    parsed = urlparse(memo)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", memo) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    restock = memo
    requests.get(str(restock))
    return jsonify({"result": "success"})
