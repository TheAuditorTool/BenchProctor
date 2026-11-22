# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("run_conversion", __name__)


@bp.route("/run_conversion", methods=["POST"])
def run_conversion():
    synopsis = (request.get_json(silent=True) or {}).get("documents_payload", "")
    parsed = urlparse(synopsis)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", synopsis) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dossier = synopsis
    requests.get(str(dossier))
    return jsonify({"result": "success"})
