# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("render_manifest", __name__)


@bp.route("/render_manifest", methods=["POST"])
def render_manifest():
    remark = request.headers.get('User-Agent', '')
    parsed = urlparse(remark)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", remark) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    cohort = remark
    requests.get(str(cohort))
    return jsonify({"result": "success"})
