# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("grant_share", __name__)


@bp.route("/grant_share", methods=["POST"])
def grant_share():
    notice = (request.get_json(silent=True) or {}).get("workspace_payload", "")
    parsed = urlparse(notice)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    wording = notice
    requests.get(str(wording))
    return jsonify({"result": "success"})
