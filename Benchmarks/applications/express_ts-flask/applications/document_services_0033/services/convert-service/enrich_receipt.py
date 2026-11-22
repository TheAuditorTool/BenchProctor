# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("enrich_receipt", __name__)


@bp.route("/enrich_receipt", methods=["POST"])
def enrich_receipt():
    snippet = request.files['upload'].filename
    addendum = f'{snippet!s}'
    parsed = urlparse(addendum)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", addendum) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    dossier = addendum
    requests.get(str(dossier))
    return jsonify({"result": "success"})
