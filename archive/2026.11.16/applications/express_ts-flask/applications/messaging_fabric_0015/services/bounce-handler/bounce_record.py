# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("record_bounce", __name__)


@bp.route("/record_bounce", methods=["POST"])
def record_bounce():
    note = (request.get_json(silent=True) or {}).get("messaging_payload", "")
    parsed = urlparse(note)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    excerpt = note
    requests.get(str(excerpt))
    return jsonify({"result": "success"})
