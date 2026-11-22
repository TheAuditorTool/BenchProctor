# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("compact_config", __name__)


@bp.route("/compact_config", methods=["POST"])
def compact_config():
    note = request.files['upload'].filename
    cohort = f'{note!s}'
    parsed = urlparse(cohort)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", cohort) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    gauge = cohort
    requests.get(str(gauge))
    return jsonify({"result": "success"})
