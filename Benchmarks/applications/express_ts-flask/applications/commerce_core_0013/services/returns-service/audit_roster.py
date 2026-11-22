# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("audit_roster", __name__)


@bp.route("/audit_roster", methods=["POST"])
def audit_roster():
    wording = request.files['upload'].filename
    backorder = f'{wording!s}'
    parsed = urlparse(backorder)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", backorder) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    voucher = backorder
    requests.get(str(voucher))
    return jsonify({"result": "success"})
