# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enrich_threshold", __name__)


@bp.route("/enrich_threshold", methods=["POST"])
def enrich_threshold():
    remark = request.headers.get('User-Agent', '')
    parsed = urlparse(remark)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remark) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    grievance = remark
    requests.get(str(grievance))
    return jsonify({"result": "success"})
