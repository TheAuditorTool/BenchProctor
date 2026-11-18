# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("authorize_payment", __name__)


@bp.route("/authorize_payment", methods=["POST"])
def authorize_payment():
    disbursement = (request.get_json(silent=True) or {}).get("payments_payload", "")
    parsed = urlparse(disbursement)
    if not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    remittance = disbursement
    requests.get(str(remittance))
    return jsonify({"result": "success"})
