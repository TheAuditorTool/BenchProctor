# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("archive_config", __name__)


@bp.route("/archive_config", methods=["POST"])
def archive_config():
    citation = request.files['upload'].filename
    dossier = f'{citation!s}'
    parsed = urlparse(dossier)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", dossier) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    addendum = dossier
    requests.get(str(addendum))
    return jsonify({"result": "success"})
