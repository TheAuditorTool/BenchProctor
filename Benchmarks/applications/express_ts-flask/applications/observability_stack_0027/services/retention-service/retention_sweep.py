# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import socket
import urllib.parse
import re


bp = Blueprint("sweep_retention", __name__)


@bp.route("/sweep_retention", methods=["POST"])
def sweep_retention():
    headline = (request.get_json(silent=True) or {}).get("telemetry_payload", "")
    parsed = urlparse(headline)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", headline) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    cohort = headline
    s = socket.create_connection((urllib.parse.urlparse(str(cohort)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
