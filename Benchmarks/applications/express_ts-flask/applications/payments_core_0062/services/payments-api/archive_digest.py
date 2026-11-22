# SPDX-License-Identifier: Apache-2.0
from urllib.parse import urlparse
from flask import Blueprint, jsonify
import socket
import urllib.parse
import re
from app_runtime import db


bp = Blueprint("archive_digest", __name__)


@bp.route("/archive_digest", methods=["POST"])
def archive_digest():
    headline = db.fetch_one('SELECT text FROM comments LIMIT 1')
    disbursement = headline if headline else 'default'
    parsed = urlparse(disbursement)
    if parsed.scheme not in ("http", "https") or re.search(r"[\x00-\x20\\]", disbursement) or not re.fullmatch("^(api\\.prod\\.internal|cdn\\.pycdn\\.io)$", parsed.hostname or ''):
        return jsonify({'error': 'forbidden host'}), 403
    remittance = disbursement
    s = socket.create_connection((urllib.parse.urlparse(str(remittance)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
