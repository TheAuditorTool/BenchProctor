# SPDX-License-Identifier: Apache-2.0
import requests
from urllib.parse import urlparse
from flask import Blueprint, request, jsonify
import re


bp = Blueprint("quote_shipment", __name__)


@bp.route("/quote_shipment", methods=["POST"])
def quote_shipment():
    subtitle = (request.get_json(silent=True) or {}).get("shipping_payload", "")
    parsed = urlparse(subtitle)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", subtitle) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    parcel = subtitle
    requests.get(str(parcel))
    return jsonify({"result": "success"})
