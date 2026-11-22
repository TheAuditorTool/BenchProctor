# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("merge_roster", __name__)


@bp.route("/merge_roster", methods=["POST"])
def merge_roster():
    citation = db.fetch_one('SELECT text FROM comments LIMIT 1')
    consignment = citation if citation else 'default'
    parsed = urlparse(consignment)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", consignment) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    parcel = consignment
    s = socket.create_connection((urllib.parse.urlparse(str(parcel)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
